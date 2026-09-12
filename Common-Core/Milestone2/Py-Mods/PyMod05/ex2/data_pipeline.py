from typing import Any, Protocol
from typing_extensions import override
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = "{"
        for i, (rank, value) in enumerate(data):
            result += f'"item_{rank}": "{value}"'
            if i < len(data) - 1:
                result += ", "
        result += "}"
        print(f"JSON Output: {result}")


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []
        for _, value in data:
            values.append(value)
        result = ",".join(values)
        print(f"CSV Output: {result}")


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception("No data available")
        value = self._data.pop(0)
        rank = self._rank
        self._rank += 1
        return rank, value

    @property
    def count(self) -> int:
        """Return the number of stored elements.
        count  = lo que todavía no hemos consumido"""
        return len(self._data)

    @property
    def total(self) -> int:
        """Return the total number of processed elements.
        total  = todo lo que ha procesado históricamente"""
        return self._total


class NumericProcessor(DataProcessor):

    @override
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if isinstance(item, bool):
                    return False
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    @override
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, (int, float)):
            self._data.append(str(data))
            self._total += 1
        else:
            for item in data:
                self._data.append(str(item))
                self._total += 1


class TextProcessor(DataProcessor):

    @override
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    @override
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, str):
            self._data.append(data)
            self._total += 1
        else:
            for item in data:
                self._data.append(item)
                self._total += 1


class LogProcessor(DataProcessor):

    @override
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._validate_log(data)
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not self._validate_log(item):
                    return False
            return True
        return False

    def _validate_log(self, data: dict[Any, Any]) -> bool:
        if "log_level" not in data or "log_message" not in data:
            return False

        if not isinstance(data["log_level"], str):
            return False

        if not isinstance(data["log_message"], str):
            return False

        return True

    @override
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, dict):
            self._data.append(
                data["log_level"] + ": " + data["log_message"]
            )
            self._total += 1
        else:
            for item in data:
                self._data.append(
                    item["log_level"] + ": " + item["log_message"]
                )
                self._total += 1


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(data):
                    processor.ingest(data)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            return print("No processor found, no data")
        for processor in self.processors:
            print(
                f"{processor.__class__.__name__}: "
                f"total {processor.total} items processed, "
                f"remaining {processor.count} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data: list[tuple[int, str]] = []
            elements = min(nb, processor.count)
            for _ in range(elements):
                data.append(processor.output())
            if data:
                plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)
    print(
        "Send first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], "
        "[{'log_level': 'WARNING', "
        "' log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', "
        "'log_message': 'User wil is connected'}], "
        "42, ['Hi', 'five']]"
    )
    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42, ["Hi", "five"]
    ]
    stream.process_stream(first_batch)
    stream.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()
    print(
        "Send another batch of data: "
        "[21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], "
        "[{'log_level': ' ERROR', " "'log_message': '500 server crash'}, "
        "{'log_level': 'NOTICE', "
        "'log_message': 'Certificate expires in 10 days'}], "
        "[32, 42, 64, 84, 128, 168], 'World hello']"
    )
    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": " ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]
    stream.process_stream(second_batch)
    stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")

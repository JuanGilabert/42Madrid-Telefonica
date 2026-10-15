from typing import Any
from typing_extensions import override
from abc import ABC, abstractmethod


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


def ft_consume_elements(
    numeric_processor: DataProcessor,
    text_processor: DataProcessor,
    log_processor: DataProcessor
) -> None:
    print()
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric_processor.output()
    for _ in range(2):
        text_processor.output()
    log_processor.output()


def main() -> None:
    stream = [
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
        42,
        ["Hi", "five"]
    ]
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    stream_processor = DataStream()
    stream_processor.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    print()
    numeric_processor = NumericProcessor()
    stream_processor.register_processor(numeric_processor)
    print(f"Send first batch of data on stream: {stream}")
    stream_processor.process_stream(stream)
    stream_processor.print_processors_stats()
    print()
    print("Registering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream_processor.register_processor(text_processor)
    stream_processor.register_processor(log_processor)
    print("Send the same batch again")
    stream_processor.process_stream(stream)
    stream_processor.print_processors_stats()
    ft_consume_elements(
        numeric_processor, text_processor, log_processor
    )
    stream_processor.print_processors_stats()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")

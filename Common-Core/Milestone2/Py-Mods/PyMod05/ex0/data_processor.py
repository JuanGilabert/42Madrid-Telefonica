from typing import Any
from typing_extensions import override
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception("No data available")
        value = self._data[0]
        self._data = self._data[1:]
        rank = self._rank
        self._rank += 1
        return rank, value


class NumericProcessor(DataProcessor):
    @override
    def validate(self, data: Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        if isinstance(data, list):
            for item in data:
                if not (isinstance(item, int) or isinstance(item, float)):
                    return False
            return True
        return False

    @override
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, int) or isinstance(data, float):
            self._data = self._data + [str(data)]
        else:
            for item in data:
                self._data = self._data + [str(item)]


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
            self._data = self._data + [data]
        else:
            for item in data:
                self._data = self._data + [item]


class LogProcessor(DataProcessor):
    @override
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key in data:
                if not isinstance(key, str):
                    return False
                if not isinstance(data[key], str):
                    return False
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for key in item:
                    if not isinstance(key, str):
                        return False
                    if not isinstance(item[key], str):
                        return False
            return True
        return False

    @override
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, dict):
            self._data = self._data + [
                data["log_level"] + ": " + data["log_message"]
            ]
        else:
            for item in data:
                self._data = self._data + [
                    item["log_level"] + ": " + item["log_message"]
                ]


def ft_test_numeric_processor() -> None:
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print("Trying to validate input '42':", numeric.validate(42))
    print("Trying to validate input 'Hello':", numeric.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except Exception as e:
        print("Got exception:", e)
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print("Numeric value", rank, ":", value)
    print()


def ft_test_text_processor() -> None:
    print("Testing Text Processor...")
    text = TextProcessor()
    print("Trying to validate input '42':", text.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text.output()
    print("Text value", rank, ":", value)
    print()


def ft_test_log_processor() -> None:
    print("Testing Log Processor...")
    log = LogProcessor()
    print("Trying to validate input 'Hello':", log.validate("Hello"))
    logs = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]
    print("Processing data:", logs)
    log.ingest(logs)
    print("Extracting 2 values...")
    rank, value = log.output()
    print("Log entry", rank, ":", value)
    rank, value = log.output()
    print("Log entry", rank, ":", value)


def ft_data_processor() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    ft_test_numeric_processor()
    ft_test_text_processor()
    ft_test_log_processor()


if __name__ == "__main__":
    try:
        ft_data_processor()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")

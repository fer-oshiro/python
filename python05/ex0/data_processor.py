#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _store(self, item_convertido: str) -> None:
        self._counter += 1
        self._data.append((self._counter, item_convertido))

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and data:
            for item in data:
                if not (isinstance(item, (int, float))):
                    return False
            return True
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper string data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                if not all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in d.items()
                ):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper dict data")
        if isinstance(data, dict):
            item = ": ".join(data.values())
            self._store(item)
        else:
            for d in data:
                item = ": ".join(d.values())
                self._store(item)


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f" Trying to validate input '42': {np.validate(42)}")
    print(f" Trying to validate input 'Hello': {np.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    data1: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {data1}")
    np.ingest(data1)
    print(" Extracting 3 values...")
    for i in range(3):
        _, value = np.output()
        print(f" Numeric value {i}: {value}")
    print()

    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f" Trying to validate input '42': {tp.validate(42)}")
    data2: list[str] = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data2}")
    tp.ingest(data2)
    print(" Extracting 1 value...")
    for i in range(1):
        _, value = tp.output()
        print(f" Text value {i}: {value}")
    print()

    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f" Trying to validate input 'Hello': {lp.validate('Hello')}")
    data3: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data3}")
    lp.ingest(data3)
    print(" Extracting 2 values...")
    for i in range(2):
        _, value = lp.output()
        print(f" Log entry {i}: {value}")


if __name__ == "__main__":
    main()

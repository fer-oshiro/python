#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    @property
    def stats(self) -> tuple[int, int]:
        return self._counter, len(self._data)

    def _store(self, item_convertido: str) -> None:
        self._data.append((self._counter, item_convertido))
        self._counter += 1

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data left on processor")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def __str__(self) -> str:
        return "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and data:
            for item in data:
                if (not isinstance(item, (int, float))
                        or isinstance(item, bool)):
                    return False
            return True
        return (isinstance(data, (int, float))
                and not isinstance(data, bool))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def __str__(self) -> str:
        return "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return len(data) > 0 and all(
                isinstance(item, str) for item in data
            )
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
    def __str__(self) -> str:
        return "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return len(data) > 0 and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        if isinstance(data, list):
            return len(data) > 0 and all(
                isinstance(d, dict) and self.validate(d) for d in data
            )
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [item[1] for item in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = [f'"item_{idx}": "{val}"' for idx, val in data]
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                print(
                    "DataStream error - " +
                    f"Can't process element in stream: {item}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            total, remaining = proc.stats
            print(f"{proc}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                _, remaining = processor.stats
                if remaining == 0:
                    break
                data.append(processor.output())
            plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")

    data_stream = DataStream()
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    csv_plugin = CSVExportPlugin()
    json_plugin = JSONExportPlugin()

    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    batch = [
            'Hello world',
            [3.14, -1, 2.71],
            [
                {
                    'log_level': 'WARNING',
                    'log_message': 'Telnet access! Use ssh instead'
                },
                {'log_level': 'INFO', 'log_message': 'User wil is connected'}
            ],
            42,
            ['Hi', 'five']
        ]
    print(f"Send first batch of data on stream: {batch}\n")

    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, csv_plugin)

    print()
    data_stream.print_processors_stats()

    batch = [
            21,
            ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [
                {'log_level': 'ERROR', 'log_message': '500 server crash'},
                {
                    'log_level': 'NOTICE',
                    'log_message': 'Certificate expires in 10 days'
                }
            ],
            [32, 42, 64, 84, 128, 168],
            'World hello'
        ]
    print(f"\nSend another batch of data: {batch}")
    data_stream.process_stream(batch)
    print()
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, json_plugin)
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()

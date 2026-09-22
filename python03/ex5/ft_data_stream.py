#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players_name = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb']
    yield (random.choice(players_name), random.choice(actions))


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for num in range(1, 1000):
        (player, action) = next(gen_event())
        print(f"Event {num}: Player {player} did action {action}")

    event_list = []
    for _ in range(1, 10):
        event_list.append(next(gen_event()))

    print(f"Built list of 10 event: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()

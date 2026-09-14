import random
from typing import Generator


players = [
    "alice",
    "bob",
    "charlie",
    "dylan",
]


actions = [
    "move",
    "grab",
    "use",
    "swim",
    "run",
    "climb",
    "release",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        position = random.randrange(len(events))
        event = events.pop(position)
        yield event


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events: list[tuple[str, str]] = []
    for i in range(10):
        event = next(event_generator)
        events.append(event)
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    try:
        ft_data_stream()
    except KeyboardInterrupt:
        print("\nProgram interrupted by student. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")

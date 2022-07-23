#!/usr/bin/env python


# built-in modules
import random

# third-party packages

# local modules


__doc__ = """
"""


def rand_bool():
    return random.choice([True, False])


def create_envelopes(num_rounds, min_possible, max_possible):
    values = (
        random.randint(min_possible, max_possible),
        random.randint(min_possible, max_possible),
    )
    min_value = min(values)
    max_value = max(values)
    return [
        (min_value, max_value) if rand_bool() else (max_value, min_value)
        for x in range(num_rounds)
    ]


def simple_choice(pair):
    return pair if rand_bool() else tuple(reversed(pair))


def switch_choice(pair):
    return tuple(reversed(simple_choice(pair)))


def simulate_simple(envelopes):
    return [simple_choice(pair)[0] for pair in envelopes]


def simulate_switch(envelopes):
    return [switch_choice(pair)[0] for pair in envelopes]


def main():
    envelopes = create_envelopes(int(1e6), 2, 1000)
    simple = simulate_simple(envelopes)
    switch = simulate_switch(envelopes)
    print(f"simple: {sum(simple)}")
    print(f"switch: {sum(switch)}")


if __name__ == "__main__":
    exit(main())

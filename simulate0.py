#!/usr/bin/env python


# built-in modules
import random

# third-party packages

# local modules


__doc__ = """
"""


def rand_bool():
    return random.choice([True, False])


def create_envelopes(num_rounds, min_value, max_value):
    return [
        (min_value, max_value) if rand_bool() else (max_value, min_value)
        for x in range(num_rounds)
    ]


def simulate_simple(envelopes):
    return [
        pair[0] if rand_bool() else pair[1]
        for pair in envelopes
    ]


def simulate_switch(envelopes):
    return [
        pair[0] if not rand_bool() else pair[1]
        for pair in envelopes
    ]


def main():
    envelopes = create_envelopes(1000000, 20, 40)
    simple = simulate_simple(envelopes)
    switch = simulate_switch(envelopes)
    print(f"simple: {sum(simple)}")
    print(f"switch: {sum(switch)}")


if __name__ == "__main__":
    exit(main())

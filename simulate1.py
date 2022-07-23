#!/usr/bin/env python


# built-in modules
import random

# third-party packages

# local modules


__doc__ = """
"""


def rand_bool():
    return random.choice([True, False])


def create_envelopes(num_rounds):
    return [rand_bool() for x in range(num_rounds)]


def simulate_simple(envelopes):
    return [
        int(val) if rand_bool() else int(not val)
        for val in envelopes
    ]


def simulate_switch(envelopes):
    return [
        int(val) if not rand_bool() else int(not val)
        for val in envelopes
    ]


def main():
    envelopes = create_envelopes(1000000)
    simple = simulate_simple(envelopes)
    switch = simulate_switch(envelopes)
    print(f"simple: {sum(simple)}")
    print(f"switch: {sum(switch)}")


if __name__ == "__main__":
    exit(main())

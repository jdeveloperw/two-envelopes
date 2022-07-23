#!/usr/bin/env python


# built-in modules
import random

# third-party packages

# local modules


__doc__ = """
"""


def rand_bool():
    return random.choice([True, False])


def create_envelopes(num_rounds, min_of_max, max_of_max):
    max_value = random.randint(min_of_max, max_of_max)
    min_value = int(max_value / 2)
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


def bad_expected_value_switch(envelopes):
    evs = []
    for pair in envelopes:
        choice = simple_choice(pair)[0]
        ev = sum([choice / 2, choice * 2]) / 2
        evs.append(ev)
    return evs


def main():
    envelopes = create_envelopes(1000000, 2, 1000)
    simple = simulate_simple(envelopes)
    switch = simulate_switch(envelopes)
    evs = bad_expected_value_switch(envelopes)
    print(f"simple: {sum(simple)}")
    print(f"switch: {sum(switch)}")
    print(f"evs: {sum(evs)}")


if __name__ == "__main__":
    exit(main())

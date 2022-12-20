#!/usr/bin/env python3

import argparse
from importlib import import_module


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2022")
    parser.add_argument("-d", "--day", type=int, default=1, help="Which day to run")
    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()

    module_name = f"day{args.day}"
    input_name = "test_input" if args.test else "input"
    input_path = f"{module_name}/{input_name}"

    module = import_module(module_name)

    results = module.main(input_path)

    print(f"Advent of Code 2022 Day {args.day}")
    for i, answer in enumerate(results):
        sep = "\n" if "\n" in str(answer) else " "
        print(f"Part {i + 1} Answer:{sep}{answer}")


if __name__ == "__main__":
    main()

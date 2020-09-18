#! /usr/bin/env python3
""" A simple example program. """

import argparse


def main():
    psr = argparse.ArgumentParser(
        description="A simple example program. Give me a number.")
    psr.add_argument("number", help="A number, any number.", type=int)
    num = psr.parse_args().number

    for exp in range(10):
        print(num ** exp)

    print("Done!")


if __name__ == "__main__":
    main()

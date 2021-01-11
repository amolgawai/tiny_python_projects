#!/usr/bin/env python3
"""
Author : amolgawai <amolgawai@localhost>
Date   : 2021-01-11
Purpose: say ahoy <article><word>
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="say ahoy <article><word>",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "positional", metavar="word", help="tell what object do you see"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.positional
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    article = "a"
    if word.startswith(vowels):
        article = "an"
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()

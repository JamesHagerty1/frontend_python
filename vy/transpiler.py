"""
Converts .vy files to .vue files

Example uses:
% python transpiler.py --target ./vy_samples/App.vy --output ./vue_dump
"""


import argparse


def main():
    parser = argparse.ArgumentParser(description=".vy to .vue transpiler")

    parser.add_argument("-t", "--target", 
                        help="The path of the .vy file to transpile")

    parser.add_argument("-o", "--output", 
                        help="The folder to place the .vue file")

    args = parser.parse_args()

    print(args.target, args.output)


if __name__ == "__main__":
    main()
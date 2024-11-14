"""
Converts .vy files to .vue files

Example uses:
% python transpiler.py --target ./vy_samples/App.vy --output ./vue_dump
"""


from bs4 import BeautifulSoup # TODO: may eventually be good for HTML validation

import argparse


def main():
    # Get CLI-given target file and output folder
    # TODO: validating the files

    args_parser = argparse.ArgumentParser(description=".vy to .vue transpiler")

    args_parser.add_argument("-t", "--target", 
                             help="The path of the .vy file to transpile")

    args_parser.add_argument("-o", "--output", 
                             help="The folder to place the .vue file")

    args = args_parser.parse_args()

    print(args.target, args.output)

    vy_file_path = args.target

    # Get ahold of Python code within a block of <vython></vython>
    # TODO robust / bug-free approach to acquiring what should only be one block
    # of Python

    with open(vy_file_path, "r") as f:
        vy_file_text = f.read()

    # print(vy_file_text)

    open_tag, close_tag = "<vython>", "</vython>"

    open_tag_end_i = vy_file_text.find(open_tag) + len(open_tag)

    close_tag_i = vy_file_text.find(close_tag)

    script_text = vy_file_text[open_tag_end_i:close_tag_i]

    print(script_text)

    
if __name__ == "__main__":
    main()
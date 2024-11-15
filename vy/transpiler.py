"""
Converts .vy files to .vue files

Example uses:
% python transpiler.py --target ./vy_samples/App.vy --output ./vue_dump
"""


import argparse
import os
import shutil


def main():
    # Get CLI-given target file and output folder
    # TODO: validating the files

    args_parser = argparse.ArgumentParser(description=".vy to .vue transpiler")

    args_parser.add_argument("-t", "--target", 
                             help="The path of the .vy file to transpile")

    args_parser.add_argument("-o", "--output", 
                             help="The folder to place the .vue file")

    args = args_parser.parse_args()

    # print(args.target, args.output)

    # Create Vue base app to build off of
    # TODO: unique names, a library that hides all this stuff

    vue_base_app = "./__vue_base_app__"

    shutil.copytree(vue_base_app, args.output, dirs_exist_ok=True)

    # Get ahold of Python code within a block of <vython></vython>
    # TODO robust / bug-free approach to acquiring what should only be one block
    # of Python

    with open(args.target, "r") as f:
        vy_file_text = f.read()

    # print(vy_file_text)

    open_tag, close_tag = "<vython>", "</vython>"

    open_tag_end_i = vy_file_text.find(open_tag) + len(open_tag)

    close_tag_i = vy_file_text.find(close_tag)

    script_text = vy_file_text[open_tag_end_i:close_tag_i]

    # print(script_text)

    # Turn text from .vy file into a .py file that Transcrypt can turn into
    # .js
    # TODO: more robust way of indenting back lines, including tabs and spaces
    # differences

    def num_spaces_line_starts_with(line):
        num = 0

        for c in line:
            if c != " ": 
                break

            num += 1

        return num

    def indent_script_lines_back_by(script_lines):
        indent_back_by = float('inf')

        for line in script_lines:
            if not line:
                continue

            num = num_spaces_line_starts_with(line)
            indent_back_by = min(indent_back_by, num)

        return indent_back_by

    script_lines = script_text.splitlines()
    
    indent_back_by = indent_script_lines_back_by(script_lines)

    for i, line in enumerate(script_lines):
        script_lines[i] = line[indent_back_by:]

    script_text = "\n".join(script_lines)

    # print(script_text)

    temp_file = "./temp.py" # TODO unique name

    try:
        with open(temp_file, "w") as f:
            f.write(script_text)

        # TODO figure out more about this command and customize it
        os.system(f"python -m transcrypt -b -m -n {temp_file}")

    except Exception as e:
        print(e)

    finally:
        os.remove(temp_file)

    
if __name__ == "__main__":
    main()
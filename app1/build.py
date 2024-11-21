

import argparse

from main import app_object


def main():
    # parser = argparse.ArgumentParser(description="")
    # args = parser.parse_args()

    # python -m transcrypt -b -m -n hello.py

    print(app_object.__template__())

    
if __name__ == "__main__":
    main()
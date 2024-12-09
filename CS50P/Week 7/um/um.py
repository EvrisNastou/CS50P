import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern="(^|\W)um($|\W)"
    count=re.findall(pattern, s, re.IGNORECASE)

    if count:
        return len(count)


if __name__ == "__main__":
    main()

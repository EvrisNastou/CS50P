from datetime import date
import inflect
import sys
import operator

p=inflect.engine()

def main():
    try:
        birthday=input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(birthday))
        print(calc_time(difference.days))
    except ValueError:
        sys.exit("Invalid date")

def calc_time(time):
    m=time*24*60
    return f"{(p.number_to_words(m, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()

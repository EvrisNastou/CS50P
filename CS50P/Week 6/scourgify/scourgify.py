import sys
import csv

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:]!=".csv":
            sys.exit("Not a CSV file")
        else:
            convert(sys.argv[1], sys.argv[2])

def convert(input, output):
    try:
        with open(input, "r") as i:
            reader=csv.DictReader(i)
            with open(output,"w") as out:
                headers=["first" , "last", "house"]
                writer=csv.DictWriter(out,fieldnames=headers)
                writer.writeheader()
                for students in reader:
                    last, first=students["name"].split(", ")
                    house=students["house"]
                    writer.writerow({"first": first, "last":last, "house":house})
    except FileNotFoundError:
        sys.exit(f"Could not read {file}")



if __name__ =="__main__":
    main()

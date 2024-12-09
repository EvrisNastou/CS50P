def main():
    str=input("What time is it? ")
    time=convert(str)
    if time>=7.00 and time<=8.00:
        print("breakfast time")
    elif time>=12.00 and time<=13.00:
        print("lunch time")
    elif time>=18.00 and time<=19.00:
        print("dinner time")
    else: print()


def convert(time):
    list=time.split(":")
    min=float(list[1])/60
    return float(list[0])+min



if __name__ == "__main__":
    main()

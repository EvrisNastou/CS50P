import random


def main():
    chance=3
    score=0
    times=10
    lvl=get_level()

    while times!=0:
        if chance==3:
            x,y=generate_integer(lvl)
        try:
            user_answer=int(input(f"{x} + {y} = "))
            answer=x+y
            if user_answer==answer:
                times-=1
                score+=1
                chance=3

            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chance-=1
            pass

        if chance==0:
            print(f"{x} + {y} = {answer}")
            chance=3
            times-=1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:
                return level
        except:
            pass



def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    elif level==3:
        x=random.randint(100,999)
        y=random.randint(100,999)
    return x,y


if __name__ == "__main__":
    main()

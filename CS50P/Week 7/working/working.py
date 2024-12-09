import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    patern="(0?[1-9]|1[0-2]):?\\.?([0-5][0-9])? (AM|PM)"
    match=re.search(r"^" + patern + " to " + patern + "$",s)
    if match:
        star_time=standar(match.group(1),match.group(2),match.group(3))
        end_time=standar(match.group(4),match.group(5),match.group(6))
        return f"{star_time} to {end_time}"
    else :
        raise ValueError


def standar(hr, min, time):
    if hr=="12":
        if time=="PM":
            hour="12"
        else:
            hour="00"
    else:
        if time=="PM":
            hour=f"{int(hr)+12}"
        else:
            hour=f"{int(hr):02}"
    if min==None:
        minute="00"
    else:
        minute=f"{int(min):02}"

    return f"{hour}:{minute}"


if __name__=="__main__":
    main()

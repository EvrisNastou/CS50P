import inflect

p = inflect.engine()
name_list=[]


while True:
    try:
        s=input("Name: ").strip().title()
        name_list.append(s)
    except EOFError:
        print()
        print(f"Adieu, adieu, to {p.join(name_list)}" )
        break



def calculator():
    print("this is the simple calculator for python")
    print("enter your operation ")
    print("1.addition(+)")
    print("2.subtration(-)")
    print("3.multipication(*)")
    print("4.division(/)")

calculator()

def click():
    choice=int(input("enter your choice"))
    x=int(input("enter your x ="))
    y=int(input("enter your y ="))

    

    if choice==1:
        print(f"your additionm is{x+y} ")

    elif choice==2:
        print(f"your subtration is {x-y}")

    elif choice==3:
        print(f"your multipication is {x*y}")
    elif choice==4:
        print(f"your division is {x/y}")
click()        





    







    
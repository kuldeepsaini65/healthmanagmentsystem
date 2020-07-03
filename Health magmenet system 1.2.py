print("******** Health Managment System ********")
print("Version 1.0")
print("****By-Kuldeep Saini****")



def lock():
    def getdate():
        import datetime
        return datetime.datetime.now()

    print("For Whome You Are Here:- ",)
    name = [["Harry", 1], ["Rohan", 2], ["Hammad", 3]]
    for i, num in name:
        print(i, num)
    inp = int(input("Enter Number of Your Choice:-"))
    if inp==1:
        print("What You Want to Lock")
        lock_choice = input("Exercise Or Diet:- ").capitalize()
        if lock_choice=="Exercise":
            take_Excercise = input("Enter Your Excercise Name:- ")
            with open("health exercise harry.txt","a") as e1:

                e1.write(str([str(getdate())])+"-"+take_Excercise+"\n")
            print("Your Excersice Registered Successfully!")
        elif lock_choice == "Diet":
            diet_harry = input("Enter Your Diet Name:- ")
            with open("health diet harry.txt","a") as d1:
                d1.write(str([str(getdate())])+"-"+diet_harry+"\n")
            print("Your Diet Listed Successfully!")
        else:
            print("You Typed Wrong Choice That not Listed In Our System")
    elif inp == 2:
        print("What You Want to Lock")
        lock_choice2 = input("Exercise Or Diet:- ").capitalize()
        if lock_choice2=="Exercise":
            take_Excercise2 = input("Enter Your Excercise Name:- ")
            with open("health excercise rohan.txt","a") as e2:
                e2.write(str([str(getdate())])+"-"+take_Excercise2+"\n")
            print("Your Excersice Registered Successfully!")
        elif lock_choice2 == "Diet":
            diet_rohan = input("Enter Your Diet Name:- ")
            with open("health diet rohan.txt","a") as d2:
                d2.write(str([str(getdate())])+"-"+diet_rohan+"\n")
            print("Your Diet Listed Successfully!")
        else:
            print("You Typed wrong choice that doesnt listed in our system")
    elif inp == 3:
        print("What You Want to Lock")
        lock_choice3 = input("Exercise Or Diet:- ").capitalize()
        if lock_choice3 == "Exercise":
            take_Excercise3 = input("Enter Your Excercise Name:- ")
            with open("health exercise hammad.txt", "a") as e3:
                e3.write(str([str(getdate())])+"-"+take_Excercise3+"\n")
            print("Your Excersice Registered Successfully!")
        elif lock_choice3 == "Diet":
            diet_hammad = ("Enter Your Diet Name:- ")
            with open("health diet hammad.txt", "a") as d3:
                d3.write(diet_hammad)
            print("Your Diet Listed Successfully!")
        else:
            print("You Typed Wrong Choice That not Listed In Our System")
    else:
        print("You Typed Wrong Input. May Be That not Stored In Our System.\nPlease Check Your Input")

def retrive():
    print("List Of Coustmer in Our System:- ")
    l = [["Harry",1],["Rohan",2],["Hammad",3]]
    for i,n in l:
        print(i, n)
    print()
    inp = int(input(" Enter Number Of Your Choice:- "))
    if inp==1:
        print("What You Want to Retrive")
        ret1 = input("Exercise Or Diet:- ").capitalize()
        if ret1=="Exercise":
            with open("health exercise harry.txt","r") as r1:
                for i in r1:
                    print(i, end="")
        elif ret1=="Diet":
            with open("health diet harry.txt","r") as d1:
                for i in d1:
                    print(i, end="")
        else:
            print("Please Check Your Keyword!!!!")
    elif inp==2:
        print("What You Want to Retrive")
        ret2 = input("Exercise Or Diet:- ").capitalize()
        if ret2 == "Exercise":
            with open("health excercise rohan.txt", "r") as r2:
                for i in r2:
                    print(i, end="")
        elif ret2 == "Diet":
            with open("health diet rohan.txt", "r") as d2:
                for i in d2:
                    print(i, end="")
        else:
            print("Please Check Your Keyword!!!!")
    elif inp == 3:
        print("What You Want to Retrive")
        ret3 = input("Exercise Or Diet:- ").capitalize()
        if ret3 == "Exercise":
            with open("health exercise hammad.txt.txt", "r") as r3:
                for i in r3:
                    print(i, end="")
        elif ret3 == "Diet":
            with open("health diet hammad.txt", "r") as d3:
                for i in d3:
                    print(i, end="")
        else:
            print("Please Check Your Keyword!!!!")

    else:
        print("Oops! You Entered Wrong Input")

print("You Want To Lock Or Retrive \nPress 1 for Lock\nPress 2 for Retrive")
print()
choice = int(input("Enter Number of Your Choice:- "))
if choice==1:
    lock()
elif choice==2:
    retrive()
else:
    print("Ops Wrong Input")


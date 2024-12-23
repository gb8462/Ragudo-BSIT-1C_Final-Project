import os

from Code_Challenges import (
    Code_Challenge1, Code_Challenge2, Code_Challenge3, Code_Challenge4,
    Code_Challenge5, Code_Challenge6, Code_Challenge7, Code_Challenge8,
    Code_Challenge9, Code_Challenge10, Code_Challenge11, Code_Challenge12,
    Code_Challenge13, Code_Challenge14, Code_Challenge15, Code_Challenge16_Linux
)
from Code_Activities import (
    Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, Activity7, Activity8,
    Activity9, Activity10, Activity11, Activity12, Activity13, Activity14, Activity15, Activity16,
    Activity17, Activity18, Activity19, Activity20, Activity21, Activity22, Activity23, Activity24, Activity25
)

from Personal_Projects import (
    Hash, Base64_linux, Caesar_Cypher,Loading_linux
)

def clean():
    os.system('clear')

def main():
    while True:
        Loading_linux.load()
        print("=============================")
        print("===== Compiled Projects =====")
        print("=============================")
        print("[1]. School Code Challanges")
        print("[2]. School Activities")
        print("[3]. Personal Projects")
        print("[0]. Exit Program")
        print("=============================\n")
        usr = input("please enter a number from [0-3] : ")
        clean()
        if usr == "1":
            Loading_linux.load()
            Code_challenges()
        elif usr == "2":
            Loading_linux.load()
            School_Activities()
        elif usr == "3":
            Loading_linux.load()
            personal_project()
        elif usr == "0":
            print("Thank you for browsing my compiled programs")
            exit()
        else:
            print("INVALID INPUT! Try Again")

def Code_challenges():
    def menu():
        print("""
|==================================================|
|====================== MENU ======================|
|==================================================|
|         Please enter the number of your choice   |      
|==================================================|
|[ 1 ]. Code Challenge  1   [11]. Code Challenge 11|
|[ 2 ]. Code Challenge  2   [12]. Code Challenge 12|
|[ 3 ]. Code Challenge  3   [13]. Code Challenge 13|
|[ 4 ]. Code Challenge  4   [14]. Code Challenge 14|
|[ 5 ]. Code Challenge  5   [15]. Code Challenge 15|
|[ 6 ]. Code Challenge  6   [16]. Code Challenge 16|
|[ 7 ]. Code Challenge  7                          |
|[ 8 ]. Code Challenge  8                          |
|[ 9 ]. Code Challenge  9                          |
|[ 10 ]. Code Challenge 10                         |
|==================================================|
""")
    menu()
    while True:        
        print("\n=================================")
        print("======== Code Challenges ========")
        print("=================================\n")
        print("[exit]. Exit Code Challenges")
        print("[menu]. Code Challenges Menu\n")
        usr = input("please type [menu] to view Choices : ")
        clean()
        
        if usr == "1":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge1.Code1()
        elif usr == "2":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge2.Code2()
        elif usr == "3":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge3.Code3()
        elif usr == "4":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge4.Code4()
        elif usr == "5":
            Loading_linux.load()
            print("OUTPUT:")
            Loading_linux.load()
            Code_Challenge5.Code5()
        elif usr == "6":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge6.Code6()
        elif usr == "7":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge7.Code7()
        elif usr == "8":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge8.Code8()
        elif usr == "9":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge9.Code9()
        elif usr == "10":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge10.Code10()
        elif usr == "11":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge11.Code11()
        elif usr == "12":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge12.Code12()
        elif usr == "13":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge13.Code13()
        elif usr == "14":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge14.Code14()
        elif usr == "15":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge15.Code15()
        elif usr == "16":
            Loading_linux.load()
            print("OUTPUT:")
            Code_Challenge16_Linux.Code16()
        elif usr.lower() == "menu":
            menu()
        elif usr.lower() == "exit":
            Loading_linux.exiting()
            return
        else:
            print("INVALID INPUT!")

def School_Activities():
    def menu():
        print("""
|==================================================|
|====================== MENU ======================|
|==================================================|
|      Please Enter the Number of Your Choice      |
|==================================================|
| [ 1 ]. Activity  1     [14]. Activity 14         |
| [ 2 ]. Activity  2     [15]. Activity 15         |
| [ 3 ]. Activity  3     [16]. Activity 16         |
| [ 4 ]. Activity  4     [17]. Activity 17         |
| [ 5 ]. Activity  5     [18]. Activity 18         |
| [ 6 ]. Activity  6     [19]. Activity 19         |
| [ 7 ]. Activity  7     [20]. Activity 20         |
| [ 8 ]. Activity  8     [21]. Activity 21         |
| [ 9 ]. Activity  9     [22]. Activity 22         |
| [ 10 ]. Activity 10    [23]. Activity 23         |
| [ 11 ]. Activity 11    [24]. Activity 24         |
| [ 12 ]. Activity 12    [25]. Activity 25         |
| [ 13 ]. Activity 13                              |
|==================================================|
""")
    menu()
    while True:
        print("\n===================================")
        print("========= Code Activities =========")
        print("===================================\n")
        print("[exit]. Exit Code Activities")
        print("[menu]. Code Activities Menu\n")
        usr = input("please type [menu] to view Choices : ")
        clean()

        if usr == "1":
            Loading_linux.load()
            print("OUTPUT:")
            Activity1.act1()
        elif usr == "2":
            Loading_linux.load()
            print("OUTPUT:")
            Activity2.act2()
        elif usr == "3":
            Loading_linux.load()
            print("OUTPUT:")
            Activity3.act3()
        elif usr == "4":
            Loading_linux.load()
            print("OUTPUT:")
            Activity4.act4()
        elif usr == "5":
            Loading_linux.load()
            print("OUTPUT:")
            Activity5.act5()
        elif usr == "6":
            Loading_linux.load()
            print("OUTPUT:")
            Activity6.act6()
        elif usr == "7":
            Loading_linux.load()
            print("OUTPUT:")
            Activity7.act7()
        elif usr == "8":
            Loading_linux.load()
            print("OUTPUT:")
            Activity8.act8()
        elif usr == "9":
            Loading_linux.load()
            print("OUTPUT:")
            Activity9.act9()
        elif usr == "10":
            Loading_linux.load()
            print("OUTPUT:")
            Activity10.act10()
        elif usr == "11":
            Loading_linux.load()
            print("OUTPUT:")
            Activity11.act11()
        elif usr == "12":
            Loading_linux.load()
            print("OUTPUT:")
            Activity12.act12()
        elif usr == "13":
            Loading_linux.load()
            print("OUTPUT:")
            Activity13.act13()
        elif usr == "14":
            Loading_linux.load()
            print("OUTPUT:")
            Activity14.act14()
        elif usr == "15":
            Loading_linux.load()
            print("OUTPUT:")
            Activity15.act15()
        elif usr == "16":
            Loading_linux.load()
            print("OUTPUT:")
            Activity16.act16()
        elif usr == "17":
            Loading_linux.load()
            print("OUTPUT:")
            Activity17.act17()
        elif usr == "18":
            Loading_linux.load()
            print("OUTPUT:")
            Activity18.act18()
        elif usr == "19":
            Loading_linux.load()
            print("OUTPUT:")
            Activity19.act19()
        elif usr == "20":
            Loading_linux.load()
            print("OUTPUT:")
            Activity20.act20()
        elif usr == "21":
            Loading_linux.load()
            print("OUTPUT:")
            Activity21.act21()
        elif usr == "22":
            Loading_linux.load()
            print("OUTPUT:")
            Activity22.act22()
        elif usr == "23":
            Loading_linux.load()
            print("OUTPUT:")
            Activity23.act23(4)
        elif usr == "24":
            Loading_linux.load()
            print("OUTPUT:")
            Activity24.act24(4)
        elif usr == "25":
            Loading_linux.load()
            print("OUTPUT:")
            Activity25.act25()
        elif usr.lower() == "menu":
            menu()
        elif usr.lower() == "exit":
            Loading_linux.exiting()
            return
        else:
            print("INVALID INPUT!")

def personal_project():
    while True:
        print("\n==================================")
        print("======== Personal Project ========")
        print("==================================\n")
        print("Type [exit] to exit program\n\nCurrent Projects Available are: \n[1]. Hashing\n[2]. Base64\n[3]. Caesar Cypher")
        usr = input("Please type enter the number of your choice ")
        clean()
        if usr == "1":
            Loading_linux.load()
            Hash.hash()
        elif usr == "2":
            Loading_linux.load()
            Base64_linux.Encoding_Decoding()
        elif usr == "3":
            Loading_linux.load()
            Caesar_Cypher.caesar_cipher()
        elif usr.lower() == "exit":
            Loading_linux.exiting()
            return
        else:
            print("Invalid input Please Try Again!")
main()
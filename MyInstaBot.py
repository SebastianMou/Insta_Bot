from time import sleep
from logic import MyInstaBot_login, testerr
import tester_file

def main_menu():
    print("1. Instagram Marketing Bot")
    print("2. testerr")
    print("3. funcion")
    print("4. whatsapp")
    print("0. exit")

    option = int(input("entter a number: "))

    if option == 1:
        print("this marketing boy will comment & like on chosen hashtags")
        print("and will comment & like difrent insta accounts")
        op = str(input("do you what to begin (y/n): "))
        if op == "y":
            def main():
                while True:
                    my_bot = MyInstaBot_login()
                    sleep(60*60)

            if __name__ == '__main__':
                main()
        else:
            print("ok bye")

    elif option == 2:
        testerr.tester_print()

    elif option == 3:
        tester_file.just_a_funcion()

    elif option == 4:
        print("4")
    
    elif option == 0:
        print("good bye")
        exit()
main_menu()
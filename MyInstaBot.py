from time import sleep
from logic import MyInstaBot_login, testerr
import tester_file

def main_menu():
    print("1. selenium")
    print("2. testerr")
    print("3. funcion")
    print("0. exit")
    option = int(input("entter a number: "))

    if option == 1:
        def main():
            while True:
                my_bot = MyInstaBot_login()
                sleep(60*60)

        if __name__ == '__main__':
            main()

    elif option == 2:
        testerr.tester_print()

    elif option == 3:
        tester_file.just_a_funcion()
    
    elif option == 0:
        print("good bye")
        exit()
main_menu()
from os import system as os_system

from check_crlf_endings import check_crlf_endings
from delete_temp_files import delete_temp_files


def main():
    running = True

    while running:
        os_system("cls")

        print("1 - Check for CRLF endings")
        print("2 - Delete temp files")
        print("q - Quit")
        user_input = input("> ")

        match user_input:
            case "1":
                os_system("cls")
                check_crlf_endings()
                input("> ")
            case "2":
                os_system("cls")
                delete_temp_files()
                input("> ")
            case "q":
                running = False

        os_system("cls")


if __name__ == "__main__":
    main()

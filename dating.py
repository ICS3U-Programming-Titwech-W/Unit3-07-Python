#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.6. 2022

# this program tell the user if they can
# date someone's grandchild

from colorama import Fore


def main():

    # # try catch
    # try:
    # string into integer
    user_goodlooking = input("Are you good looking type YES or NO: ")
    user_rich = input("Are you rich type YES or NO: ")

    user_goodlooking.upper()
    user_rich.upper()

    # Process of True of False
    if user_goodlooking == "YES" or user_rich == "YES":
        print(Fore.CYAN + "You can date my grandchild")

    else:
        print(Fore.RED + "You can't date my grandchild or enter YES or NO")
        print("")

    # except Exception:
    #     print(Fore.RED + "Please enter YES or NO")
    #     print("")

    # finally:
    #     print(Fore.YELLOW + "Thank you!")


if __name__ == "__main__":
    main()

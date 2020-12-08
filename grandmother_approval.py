#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program tells you if the grandmother approves of the users age(25-40)


import constants


def main():
    # this program tells you if the grandmother approves of the users
    # age(25-40)

    # input
    age = input("Enter your age please: ")
    print("")

    # process & output
    try:
        age = int(age)
        if age <= constants.MAX_AGE and age >= constants.MINIMUM_AGE:
            print("Grandmother approves")
        else:
            print("Grandmother does not approve")
            print("")
    except Exception:
        print("That was not an age. Try again.")


if __name__ == "__main__":
    main()

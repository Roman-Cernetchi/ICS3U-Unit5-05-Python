#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program function formats a mailing address

import math


def mailing(name, srt_num, srt_name, city, province, post_code,
            apt_num=None):
    # This function formats a mailing address

    # process
    mail_address = name
    if apt_num is not None:
        mail_address = (mail_address + "\n" + apt_num + "-" + srt_num +
                        " " + srt_name + "\n" + city + " " + province + " "
                        + post_code)
    else:
        mail_address = (mail_address + "\n" + srt_num + " " + srt_name +
                        "\n" + city + " " + province + "  " + post_code)

    return mail_address


def main():
    # this function receives input

    apt_num = None

    # input
    name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (Y/N): ")
    if question == "Y" or question == "Yes":
        apt_num = input("Enter your apartment number: ")
    srt_num = input("Enter your street number: ")
    srt_name = input("Enter your street name AND type"
                     " (ex: Frank Dr): ")
    city = input("Enter your city: ")
    province = input("Enter your province (Use short version, like"
                     " ON, BC...): ")
    post_code = input("Enter your postal code: ")
    print("")

    # call functions
    if apt_num is not None:
        address = mailing(name, srt_num, srt_name, city,
                          province, post_code, apt_num)
    else:
        address = mailing(name, srt_num, srt_name, city,
                          province, post_code)

    # output
    print(address)


if __name__ == "__main__":
    main()

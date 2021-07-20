# def isLeap(year)-> bool:
#     if year % 4 == 0:
#         return True
#

def dayOfProgrammer(year):
    day = 0
    if 1700 <= year <= 1917:
        print("{} is julian calendar".format(year))
        if year % 4 == 0:
            day = 256 - 244
        else:
            day = 256 - 243
    elif 1918 <= year <= 2700:
        print("{} is gregorian calendar".format(year))
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
           # print("leap")
            day = 256 - 244
        else:
            day = 256 - 243
    else:
        print("Invalid Year")

    return f"{day}.09.{year}"


if __name__ == '__main__':
    print(dayOfProgrammer(1800))

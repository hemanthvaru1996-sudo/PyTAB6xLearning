def check_leap_year(year):
    if (year % 4 == 0 and  year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year= int(input('Enter the year: '))
result=check_leap_year(year)
print(result)


# def check_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
#
# # year = 2024
# year = 2024
# result = check_leap_year(year)
# print(result)
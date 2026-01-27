# cities=("landon","Paris","Los Angeles","Tokyo")
# print(cities)
# print(len(cities))
# print("paris" in cities)
# print(cities.count("paris"))
#
#
# t=(12,34,56)
# #t.append(12)#AttributeError: 'tuple' object has no attribute 'append'



# for i in range(1,4 ):       # Outer loop for rows
#     for j in range(i):             # Inner loop for stars in that row
#         print("*", end=" ")        # end=" " keeps the print on the same line
#     print()
# for i in range(3,0,-1) :
#     for j in range(i):
#         print("*", end=" ")
#     print()
# rows = 6
# for i in range(1,rows+1):
#     # 1. ಮೊದಲು ಸ್ಪೇಸ್ ಪ್ರಿಂಟ್ ಮಾಡಲು ಲೂಪ್
#     for j in range(rows - i):
#         print(" ", end="")
#
#     # 2. ಆಮೇಲೆ ನಕ್ಷತ್ರ ಪ್ರಿಂಟ್ ಮಾಡಲು ಲೂಪ್
#     for k in range(i):
#         print("*", end=" ")
#     print()
# for i in range( rows - 1,0,-1):
#     # 1. ಮೊದಲು ಸ್ಪೇಸ್ ಪ್ರಿಂಟ್ ಮಾಡಲು ಲೂಪ್
#     for j in range(rows - i):
#         print(" ", end="")
#
#     # 2. ಆಮೇಲೆ ನಕ್ಷತ್ರ ಪ್ರಿಂಟ್ ಮಾಡಲು ಲೂಪ್
#     for k in range(i):
#         print("*", end=" ")
#
#     # 3. ಸಾಲು ಮುಗಿದ ಮೇಲೆ ಹೊಸ ಲೈನ್‌ಗೆ ಹೋಗಲು
#     print()

# for i in range(1,4):
#     print("* "*i)
#
# for i in range(4,0,-1):
#     print("* "*i)
rows=4
for i in range(1,rows+1):
    for j in range(i):
        print("* " , end="")
    print()

# for i in range(rows-1,0,-1):
#
#     for j in range(i):
#         print("* " , end="")
#     print()
# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 6/27/2022
# Description: Asks user to enter a positive integer then prints a list of all positive integers that
#              divide that number evenly, including itself and 1, in ascending order.

num = int(input("Please enter a positive integer"))
print("The factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

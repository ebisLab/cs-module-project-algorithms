# implement a function that will calculatethe factorial of n

# understanding
# 5! 5 * 4 * 3 * 2* 1
# n! = n * (n-1) * (n-2) .... * 1

# questions to ask
# what is n? N is a number. N will always be greater than 0
# N will be a whole number, (no 1.2) no decimals
# N will not be more than 900
# return a number, which is the ttal for n!

# PLAN
# Recursion vs Iterative
# n*(n-1)!
# recursion, dont forget base case
# n<=1
# 1!=1


def rec_factorial(n):
    if n <= 1:
        return 1
    return n * rec_factorial(n-1)
    # recursive factorial time complexity O(n) --> multiplication runs n number of times


# tested and excecutted
print(rec_factorial(5))  # should be 120
print(rec_factorial(100))  # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


# another test case
print(rec_factorial(1) == 1)
print(rec_factorial(899))  # it will break, limiting in the input we want

# we have to redo implementation --change 2

# change 2

# try iterative method


def it_factorial(n):
    # simple loop from 1 to n
    # keep track of total product, keep multiplying
    total_product = 1  # end result
    for i in range(1, n+1):
        total_product += i * total_product
        #total_product *= 1

    return total_product
# time complexity (O(n)) -->linear


print(it_factorial(5))  # should be 120
print(rec_factorial(100))  # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# another test case
print(it_factorial(1) == 1)
print(it_factorial(999))  # it works!!


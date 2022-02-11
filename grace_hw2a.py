# +---------------------+
# | hw2a - Isaiah Grace |
# +---------------------+

# Part a - even checker

def isEven(in_num):
    return(int(in_num) % 2 == 0)

usr_in = input("Input number: ")

print("Your number is ", end="")
print("even!" if isEven(usr_in) else "odd!")

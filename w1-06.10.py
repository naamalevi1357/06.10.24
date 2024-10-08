# start

# a = Keeps a program that won't crash and catch the error
# b = This keeps the program from crashing while an error could be in progress
# c:
#
c: int = 88
try:
    if c / 0:
        print("good")
except:
    print("not good")

# d:
ol:int = 98
try:
    gre:int= int (input("what is gre ?"))
    if gre < ol:
        raise Exception("not good")
except Exception as error:
    print(error)




# e:
e: list[int] = [1, 6, 9, 23]
ol: int = 0
while True:
    try:
        num: int = int(input("what is numbers?"))
        if num == -999:
            break
        print(e[num])
    except ValueError:
        print("not good, Due to the need for a number.")
    except IndexError:
        print(" not good , Because it is not in the range of the list ")

# stop

import random
# All of the code is developed by your instructor! have fun!


def checks(num1, l1, rnum):  # takes as inputs the keyboard num and cowbulls list, should return cowbulls list checked
    for number1,number2 in zip(num1,str(rnum)):  # syntax for simultaneous iteration!
        if number1 == number2:
            l1[0]+= 1  # if the numbers are equal cows += 1
        else:
            l1[1] += 1  # if the numbers are not equal bulls += 1
    return l1  # return checked list


cowsbulls = [0, 0]  # first value are the cows, second are the bulls
rnum = random.randint(1111, 9999)

while cowsbulls[0] != 4:  # A loop indicating that the game won't stop until cows are 4.
    num = raw_input("Please enter a number : ")  # input from the keyboard, it's always a string type (str()).
    cowsbulls = checks(num, cowsbulls, rnum) # should return a list
    print " num: " + num + " rnum: " + str(rnum) + " cows: " + str(cowsbulls[0]) + " bulls: " + str(cowsbulls[1])
    if cowsbulls[0] != 4:  # if cows are not 4 nullify the list!
        cowsbulls = [0, 0]

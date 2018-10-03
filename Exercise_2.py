def find(l,s):
    for i in l:
        if i == int(s):
            return True
    return False


l1 = [2, 4, 6, 8, 10]

search = raw_input("Give me a number: ")  # input from keyboard always str type

print find(l1,search) # print returned result

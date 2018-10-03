

l1 = [1, 2, 2, 4, 5, 4, 9, 1, 2]

if __name__ == '__main__':

    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    print l2
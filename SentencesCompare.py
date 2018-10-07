def string_check(s1, s2):
    cnt = 0
    s3 = s1.split()
    s4 = s2.split()

    for i in s3:
        if i in s4:
            cnt += 1
    return cnt


s1 = "Hey there how are you today"
s2 = "Hello there are you fine today"

print string_check(s1, s2)  # print the result!
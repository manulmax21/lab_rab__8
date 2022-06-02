def test():
    answer = 1
    while 1:
        num = int(input())
        if not num: break
        answer *= num
    return(answer)
print(test())
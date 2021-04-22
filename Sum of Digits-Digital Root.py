def digital_root(n):
    while n>=10:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return n
    

def rec_n (n):
    if n == 1:
        return 1
    else:
        print(n)
        return rec_n(n-1)
    
n=8
rec_n(n)
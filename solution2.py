def natural_numbers(a,i=1):
    if i > a:
        return
    else:
        print(i)
        natural_numbers(a,i+1)

natural_numbers(8)
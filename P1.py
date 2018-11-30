def naturales(x):
    if x<101:
        print(x)
        x=x+1
        return naturales(x)
print(naturales(1))


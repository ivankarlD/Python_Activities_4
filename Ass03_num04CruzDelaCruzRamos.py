# 1 3 6 10 15 21 28
def triangle(num) :
    y=1
    for x in range(num-1) :
        x+=2
        y+=x
    return y

print(triangle(1))
print(triangle(6))
print(triangle(215))

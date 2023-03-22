# 1 3 6 10 15 21 28
def triangle(num) :
    y=1
    for x in range(num-1) :
        x+=2
        y+=x
    print(y)

triangle(1)
triangle(6)
triangle(215)

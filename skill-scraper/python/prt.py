
lh=2
rh=102
def add(lh, rh):
    return lh+rh
def div(lh, rh):
    return lh / rh
def mul(lh, rh):
    return lh*rh
def subtract(lh, rh):
    return lh-rh

def square(lh):
    return lh * lh

# maths = (lh*rh)-(lh+rh)
maths = subtract(mul(lh, rh),add(lh,rh))

# square = (maths*maths)

square = square(maths)
print(square)



# print("Hello Alex")
#
#
# lh = 1
# rh = 5
# print (lh - rh)
# print(subtr(lh, rh))
# subpr(lh, rh)


# 1. create functions for the 4 maths operations
# 2. create a function to do this expression: lh x rh - (lh +rh)
# 3. create a 3 function that takes the output of 2 and squares it
# 4. put in lh = 2, rh = 102, print the answer



# lh = lh + 6
#
# print (lh - rh)
#
# print("----")
# for f in range(1, 15):
#     print (lh + f)
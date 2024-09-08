# write a factorial function

# calculates n! = 1x2x ... x (n-1) x n
# unfortunately it has some bugs.
# find 'em and fix 'em

def fact(n):
    product = 0
    for j in range(1,n):
        product *= j
    return product

print(fact(5))

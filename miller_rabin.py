import random

def power(x, y, p):
     
    # Initialize result
    res = 1;
     
    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;

def Miller_rabin(n):
    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    m = n - 1;
    k = 0
    while (m % 2 == 0):
        m //= 2;
        k += 1

    a = random.randint(1, n-1)
    b = power(a, m, n)
    #b = (a ** m) % n

    if (b % n) == 1:
        return True

    for i in range(k):
        if (b % n) == n - 1:
            return True
        else:
            b = (b ** 2) % n
    return False

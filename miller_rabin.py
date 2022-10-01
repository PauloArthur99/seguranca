import random

def miller_rabin(n):
    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    m = n - 1;
    k = 0
    while (m % 2 == 0):
        m //= 2;
        k += 1

    a = random.randint(1, n-1)
    b = (a ** m) % n

    if (b % n) == 1:
        return True

    for i in range(k):
        if (b % n) == n - 1:
            return True
        else:
            b = (b ** 2) % n
    return False

print(miller_rabin(597))
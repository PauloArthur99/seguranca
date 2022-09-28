import random

class Linear_congr_gen:
    def __init__(self, m, x0, a, c):
        self.m = m
        self.x = x0
        self.a = a
        self.c = c

    def next_x(self):
        self.x = (self.a * self.x + self.c) % self.m

    def get_random_num(self, num_bits):
        random_num = ""
        bits_rand = 0
        while bits_rand < num_bits:
            self.next_x()
            new_x = bin(self.x)[2:]
            if bits_rand + len(new_x) > num_bits:
                diff = num_bits - (bits_rand + len(new_x))
                new_x = new_x[:diff]
            random_num = new_x + random_num
            bits_rand = bits_rand + len(new_x)
            
        return int(random_num, 2)

objs = list()
for i in range(1):
    x0 = random.randint(0, 123)
    c  = random.randint(0, 101)
    objs.append(Linear_congr_gen((2**31)-1, x0, 16807, c))
    print(objs[i].get_random_num(4096))


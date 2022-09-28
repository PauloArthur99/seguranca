import random

class Linear_feedback_shift_register:
    def __init__(self):
        self.state = (1 << 127) | 1

    def get_random_num(self, num_bits):
        random_num = ""
        for i in range(num_bits - 1):
            random_num =  str(self.state & 1) + random_num
            newbit = (self.state ^ (self.state >> 1) ^ (self.state >> 2) ^ (self.state >> 7)) & 1
            self.state = (self.state >> 1) | (newbit << 127)
        random_num =  "1" + random_num
        return int(random_num, 2)


lfsr = Linear_feedback_shift_register()
#for i in range(200):
while True:
    print(lfsr.get_random_num(40))


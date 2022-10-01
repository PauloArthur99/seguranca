from miller_rabin import Miller_rabin
import lfsr

def main():
    lfsr_obj = lfsr.Linear_feedback_shift_register()
    while True:
        random_number = lfsr_obj.get_random_num(512)
        if Miller_rabin(random_number):
            print(random_number)
            break


if __name__ == "__main__":
    main()
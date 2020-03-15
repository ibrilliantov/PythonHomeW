import string
import random

def rsting(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(size))

if __name__ == "__main__":
    print(rsting(100))
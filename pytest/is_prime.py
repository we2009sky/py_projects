# encoding=utf8
import math

def is_prime(scope=30):
    prime_list = []
    for i in range(2, scope):
        for num in range(2, i):
            if i % num == 0:
                break
            if i == num + 1:
                prime_list.append(i)

    # not use else , 2 must insert
    prime_list.insert(0, 2)
    return prime_list


def is_prime2(scope=50):
    prime_list = []
    for i in range(2, scope):
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


def is_prime3(scope=50):
    prime_list = []
    for i in range(2, scope):
        for num in range(2, int(math.sqrt(i) + 1)):
            if i % num == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


a = is_prime()
b = is_prime2()
c = is_prime3()

print(a)
print(b)
print(c)

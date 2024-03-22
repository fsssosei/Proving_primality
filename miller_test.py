from itertools import takewhile
from gmpy2 import mpz, ceil, log, is_strong_prp

initial_prime_number_list = [2, 3, 5, 7, 11, 13]
strong_pseudoprime_list = [2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 341550071728321, 3825123056546413051, 3825123056546413051, 3825123056546413051, 318665857834031151167461, 3317044064679887385961981]  #https://arxiv.org/pdf/1207.0063.pdf; https://oeis.org/A014233
strong_pseudoprime = strong_pseudoprime_list[len(initial_prime_number_list) - 1]  #ψ6

def miller_test(n):
    if n <= initial_prime_number_list[-1]:
        if n in initial_prime_number_list:
            return True
        else:
            return False
    elif n <= initial_prime_number_list[-1] ** 2:
        if all(map(lambda p: (n % p) != 0, takewhile(lambda x: x * x <= n, initial_prime_number_list))):
            return True
        else:
            return False
    elif any(map(lambda p: (n % p) == 0, initial_prime_number_list)):
        return False
    elif n < strong_pseudoprime:
        if all(map(lambda a: is_strong_prp(n, a), initial_prime_number_list)):
            return True
        else:
            return False
    else:
        m = mpz(ceil((log(n)**2)*2))
        if all(map(lambda a: is_strong_prp(n, a), range(2, m))):
            return True
        else:
            return False

n = int(input('请输入一个要检验的正整数：'))
if miller_test(n):
    print(f'{n}是质数')
else:
    print(f'{n}是非质数')

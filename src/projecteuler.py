import itertools
from math import sqrt


def problem1():
    print(sum([i for i in range(0,1000) if i % 3 == 0 or i % 5 == 0]))


def problem2():
    print(sum([i for i in fibonacci() if i % 2 == 0]))


def fibonacci():
    x = [1, 2]
    for i in range(2,100000000000): # arbitrarily large
        val = x[i-1] + x[i-2]
        if val >= 4000000:
            break
        x.append(val)
    return x


def problem3():
    n = 600851475143
    high = 0
    for i in range(2, int(sqrt(n))):
        if n % i == 0 and is_prime(i) and i > high:
            high = i
    print(high)


def is_prime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def problem4():
    prod = 0
    for i, j in itertools.product(range(100, 1000), range(100, 1000)):
        val = i * j
        if str(val) == str(val)[::-1]:
           if val > prod:
               prod = val
    print(prod)


def problem5():
    i = 20
    while True:
        if not div_by_1to20(i):
            i += 20
        else:
            print(i)
            break


def div_by_1to20(n):
    for j in range(1, 21):
        if not n % j == 0:
            return False
    return True


def problem6():
    sum_normal = sum([i for i in range(1,101)])
    sum_square = sum([i*i for i in range(1,101)])
    print(sum_normal ** 2 - sum_square)


def problem7():
    print(get_n_primes(10001)[-1])


def get_n_primes(n):
    x = [2]
    i = 3
    while len(x) < n:
        if is_prime(i):
            x.append(i)
        i += 1
    return x


def problem8():
    highest_number = 0
    number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    val = 1
    for i, j in itertools.product(range(0, len(number) - 12), range(0, 13)):
        val *= int(number[i + j])
        if j == 12:
            highest_number = max(highest_number, val)
            val = 1
    print(highest_number)


def problem9():
    return


problem9()

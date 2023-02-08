def genFib():
    fibn1 = 1
    fibn2 = 0
    while True:
        next = fibn1 + fibn2
        yield next
        fibn2 = fibn1
        fibn1 = next


fibMachine = genFib()
# print(fibMachine.__next__())
# print(fibMachine.__next__())
# print(fibMachine.__next__())
# print(fibMachine.__next__())
# print(fibMachine.__next__())
# print(fibMachine.__next__())


# def genPrimes():
#     x = 2
#     primes = [2]
#     yield 2
#     while True:
#         for p in primes:
#             if x % p != 0:
#                 isPrime = True
#             else:
#                 isPrime = False
#                 break
#         if isPrime == True:
#             primes.append(x)
#             next = x
#             yield next
#         x += 1

# Tidy version of above from TA:
def genPrimes():
    prime = 2
    primes = []
    while True:
        for p in primes:
            if prime % p == 0:
                break
        else:
            primes.append(prime)
            yield prime
        prime += 1


primeMachine = genPrimes()
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())
print(primeMachine.__next__())

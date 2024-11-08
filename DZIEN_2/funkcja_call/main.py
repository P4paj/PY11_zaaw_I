"""
Trzy przypadki użycia funckji __call__
1. licznik wywołań funckji
2. walidacja danych wejściowych
3. implementacja z pamięcią podręczną  (caching)
"""
from libcalls.counter import CallCounter
from libcalls.validator import RangeValidator
from libcalls.cache import CacheFunction

print("*"*70)
counter = CallCounter()
counter()
counter()
counter()
counter()

print("*"*70)
valid = RangeValidator(2,28)
valid(3)
valid(17)
valid(0)
valid(44)

print("*"*70)

def efunction(x,y):
    return x**y+y**x
ce_func = CacheFunction(efunction)
print(ce_func(2,3))
print(ce_func(2,2))
print(ce_func(2,3))
print(ce_func(13,1))
print(ce_func(13,3))
print(ce_func(13,3))
print(ce_func(2,3))

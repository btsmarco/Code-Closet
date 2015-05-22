# Halloween Party
# HackerRank.com
# Marco Botros
from math import ceil, floor

T = int(input())

def FindMaxProduct(num):
    FirstNum = ceil(num/2)
    SecondNum = floor(num/2)

    Product = FirstNum * SecondNum
    return Product


for i in range(T):
    K = int(input())

    Result = FindMaxProduct(K)

    print(Result)

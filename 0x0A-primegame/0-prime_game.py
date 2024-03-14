#!/usr/bin/python3
"""prime game module"""


def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPrimesSet(num):
        primes = [n for n in range(1, num + 1) if isPrime(n)]
        return set(primes)

    def playGame(num):
        primesSet = getPrimesSet(num)
        isMariaTurn = True
        while primesSet:
            if isMariaTurn:
                nextMove = min(primesSet)
            else:
                nextMove = max(primesSet)
            primesSet -= set(range(nextMove, num + 1, nextMove))
            isMariaTurn = not isMariaTurn
        return isMariaTurn

    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        if playGame(num):
            mariaWinsCount += 1
        else:
            benWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif mariaWinsCount < benWinsCount:
        return "Ben"
    else:
        return None

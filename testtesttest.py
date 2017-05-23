from __future__ import division
from itertools import compress
from itertools import starmap
from operator import mul
import fractions


def convertMatrix(transMatrix):
    probMatrix = []
    for i in range(len(transMatrix)):
        row = transMatrix[i]
        newRow = []
        rowSum = sum(transMatrix[i])
        if all([v == 0 for v in transMatrix[i]]):
            for j in transMatrix[i]:
                newRow.append(0)
            newRow[i] = 1
            probMatrix.append(newRow)
        else:
            for j in transMatrix[i]:
                if j == 0:
                    newRow.append(0)
                else:
                    newRow.append(j / rowSum)
            probMatrix.append(newRow)
    return probMatrix


def answer(m):
    # convert matrix numbers into probabilities
    probMatrix = convertMatrix(m)

    # find terminal states
    terminalStateFilter = []
    for row in range(len(m)):
        if all(x == 0 for x in m[row]):
            terminalStateFilter.append(True)
        else:
            terminalStateFilter.append(False)

    # multiply matrix by probability vector
    oldFirstRow = probMatrix[0]
    probVector = None
    for i in range(3000):
        probVector = [sum(starmap(mul, zip(oldFirstRow, col))) for col in zip(*probMatrix)]
        oldFirstRow = probVector

    # generate numerators
    numerators = []
    for i in probVector:
        numerator = fractions.Fraction(i).limit_denominator().numerator
        numerators.append(numerator)

    # generate denominators
    denominators = []
    for i in probVector:
        denominator = fractions.Fraction(i).limit_denominator().denominator
        denominators.append(denominator)

    # calculate factors to multiply numerators by
    factors = [max(denominators) / x for x in denominators]
    # multiply numerators by factors
    numeratorsTimesFactors = [a * b for a, b in zip(numerators, factors)]
    # filter numerators by terminal state booleans
    terminalStateNumerators = list(compress(numeratorsTimesFactors, terminalStateFilter))

    # append numerators and denominator to answer
    answerlist = []
    for i in terminalStateNumerators:
        answerlist.append(i)
    answerlist.append(max(denominators))
    return list(map(int, answerlist))

m= [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print answer(m)
m1 =  [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print answer(m1)
m1 =  [[0, 4, 2], [0, 0, 0], [0, 0, 0]]
print answer(m1)
m1 =  [[0, 0,0], [0, 0,0], [0, 0,0]]
print answer(m1)
m= [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 2, 0, 0, 3, 0], [1, 1, 3, 0, 0, 0], [0, 0, 0, 1, 0, 2], [0, 0, 0, 0, 0, 0]]
print answer(m)
m1 =  [[0]]
print answer(m1)
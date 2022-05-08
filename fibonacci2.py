def fib(noOfTerms, startTerm):
    # fibonacci series starting from startTerm and ending at noOfTerms
    firstTerm = 0
    secondTerm = 1
    fibonacciList = [firstTerm, secondTerm]
    # we need to generate atleast startTerm+noOfTerms to get our key
    for i in range(startTerm+noOfTerms):
        fibonacciList.append(fibonacciList[-1]+fibonacciList[-2])

    # we need only the first noOfTerms terms from the start term
    return fibonacciList[startTerm:startTerm+noOfTerms+1]

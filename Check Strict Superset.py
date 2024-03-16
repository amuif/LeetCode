# Enter your code here. Read input from STDIN. Print output to STDOUT

setA = list(input().split())
n = int(input())
set1 = list(input().split())
set2 = list(input().split())

def checkOccurance(A, B):
    for element in A:
        if element not in B:
            return False
    return True
result = checkOccurance(set1, setA) and checkOccurance(set2, setA)
print(result)

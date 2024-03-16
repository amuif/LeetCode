# Enter your code here. Read input from STDIN. Print output to STDOUT

eng = int(input())
engSub = set(map(int, input().split()))
french = int(input())
frenchSub = set(map(int, input().split()))
print(len(engSub.difference(frenchSub)))

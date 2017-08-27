#Input a number and the second number means how many times we can take out a number from
#the first number. The output is the largest number we can get
#For example: The number is 325, the second number is 1, then ouputs 35.
import sys

num = sys.stdin.readline().strip()
cnt = sys.stdin.readline().strip()
numlist = []
newnumber = ''
if len(num) >= 1 and len(num) <= 1000:
    if len(cnt)>= 1 and len(cnt) <= len(num):
        for i in num:
            numlist.append(int(i))
        for i in range(int(cnt)):
            min_value = min(numlist)
            numlist.remove(min_value)
        numlist = [str(x) for x in numlist]
        for i in numlist:
            newnumber += i
        print int(newnumber)













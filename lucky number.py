import sys
import time

n = int(sys.stdin.readline())

start_time = time.clock()
i = 1
count = 0
if n <= 100000:
    while i <= n:
        dec_total = 0
        binary_total = 0
        dec = str(i)
        binary = "{0:b}".format(i)
        bi = str(binary)
        for num1 in dec:
            dec_total += int(num1)
        for num2 in bi:
            binary_total += int(num2)
        if dec_total == binary_total:
            count += 1
        i += 1
    print count
    print time.clock() - start_time, "seconds"









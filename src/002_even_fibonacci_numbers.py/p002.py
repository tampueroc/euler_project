fib = [1, 2]
sum_value = 2
stopper = True
while(stopper):
    tail = fib[-1] + fib[-2]
    if 4000000 < tail:
        stopper = False
        break
    if tail % 2 == 0:
        sum_value += tail
    fib.append(tail)

print(sum_value)

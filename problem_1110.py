N = int(input())

n = 0 # initial number of rounds

M = N

while True:
    a = M // 10 #getting the tens digit
    b = M % 10 #getting the remainder
    c = (a + b) % 10 #sum and the remainder
    e = (10 * b) + c #the next sum
    n += 1 #adding 1 to n to show that the round is done

    if e == N:
        break
    M = e
print(n)

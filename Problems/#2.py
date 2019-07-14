#Project Euler #2

max = 4000000

def main():
    global max
    sum = 0
    a = 1; b = 1; c = 2
    while b < max:
        a = b
        b = c
        c = a + b
        if a % 2 == 0:
            sum += a
    print(sum)

if __name__ == '__main__':
    main()

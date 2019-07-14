#Project Euler #5

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def main():
    a = 1
    for i in range (2, 21):
        a = lcm(a, i)

    print(a)

if __name__ == '__main__':
    main()


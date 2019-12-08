#Project Euler #3

def divs(x):
    div = []
    if (x % 2 == 0):
        return 0
    for i in range(3, int(x ** 0.5) + 1, 2):
        if (x % i == 0):
            div.append(i)
    return (div == [])

def main():
    max = 2
    x = 600851475143
    list = divs(x)
    for i in range(3, int(x ** 0.5) + 1, 2):
        if divs(i):
            max = i
    print (max)

if __name__ == '__main__':
    main()

#Project Euler #7

def divs(x):
    div = []
    if (x % 2 == 0):
        return 0
    for i in range(3, int(x ** 0.5) + 1, 2):
        if (x % i == 0):
            div.append(i)
    return (div == [])

def main():
    count = 1 #i == 2
    i = 1
    while count < 10001:
        i += 2
        if divs(i):
            count += 1

    print(i)

if __name__ == '__main__':
    main()


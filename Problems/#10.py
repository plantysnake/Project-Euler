#Project Euler #10

def divs(x):
    div = []
    if (x % 2 == 0):
        return 0
    for i in range(3, int(x ** 0.5) + 1, 2):
        if (x % i == 0):
            div.append(i)
    return (div == [])


def main():
    sum = 2
    for i in range(3, 2000000, 2):
        if divs(i):
            sum += i

    print(sum)

if __name__ == '__main__':
    main()

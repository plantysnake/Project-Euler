#Project Euler #7

def divs(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i == 0):
            div.append(i)
    return div

def main():
    count = 0
    i = 1
    while count < 10001:
        i += 1
        if divs(i) == []:
            count += 1

    print(i)

if __name__ == '__main__':
    main()


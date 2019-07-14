#Project Euler #3

x = 600851475143

def divs(x):
    div = []
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i == 0):
            div.append(i)
    return div

def main():
    max = 2
    list = divs(x)
    for i in list:
        tmp = divs(i)
        if tmp == []:
            max = i
    print (max)

if __name__ == '__main__':
    main()

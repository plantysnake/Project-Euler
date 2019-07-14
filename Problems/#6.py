#Project Euler #6

def main():
    sum = 0; summ = 0
    for i in range (1, 101):
        sum += i
        summ += i ** 2
    sum = sum ** 2
    print(abs(summ - sum))

if __name__ == '__main__':
    main()


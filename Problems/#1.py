#Project Euler #1

def main():
    count = 0
    for i in range(1000):
        if ((i % 3 == 0) or (i % 5 == 0)):
            count += i
    print (count)

if __name__ == '__main__':
    main()

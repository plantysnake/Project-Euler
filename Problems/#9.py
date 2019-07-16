#Project Euler #9

def triplet(a, b, c):
    return (a ** 2 + b ** 2 == c ** 2)

def main():
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            if triplet(a, b, c):
                print(a * b * c)

if __name__ == '__main__':
    main()


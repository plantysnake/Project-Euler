#Project Euler #4

def pal(x):
    x = str(x)
    return (x == x[::-1])

def main():
    list = []
    for i in range (999, 99, -1):
        for j in range (999, 99, -1):
            x = i * j
            if pal(x):
                list.append(x)
            j -= 1
        i -= 1
    print(max(list))

if __name__ == '__main__':
    main()

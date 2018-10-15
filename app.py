import methods

def main():
    f = open('entrada.txt', 'r')
    for line in f:
        cmd = line.split()
        method = getattr(methods, cmd[0])
        method(cmd[1:len(cmd)])

if __name__ == '__main__':
    main()
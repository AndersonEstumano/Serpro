import sys

def main():
    counter = 0
    n1 = 0
    n2 = 1
    number = int(input("Enter a number: "))
    if number == 1:
        print(n1)
        sys.exit(0)
    while counter < number:
        print(n1)
        next = n1 + n2
        n1 = n2
        n2 = next
        counter += 1
    

if __name__ == "__main__":
    main()
def main ():
    number = int(input("Enter a number: "))

    print(fatorial(number))
    
def fatorial(number):
    if number == 0:
        return 1
    else:
        return number * fatorial(number - 1)
    

if __name__ == '__main__':
    main()
#factorial of given number
#fact
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial of negative numbers is not defined.")
    else:
        print("Factorial of", num, "is", factorial(num))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
FizzBuzz program with intentional mistakes
"""

def fizzbuzz():
    """FizzBuzz implementation with bugs"""
    
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

def main():
    """Main function"""
    counter = 0
    
    print("Starting FizzBuzz...")
    fizzbuzz()  # このインデントが間違っている
    
    print("FizBuzz completed!")

if __name__ == "__main__":
    main() 
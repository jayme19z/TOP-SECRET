'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''
import time
import math

def sqrtInvoke():
    num = int(input())
    wait = int(input())
    time.sleep(wait / 1000)
    print(f"Square root of {num} after {wait} miliseconds is {math.sqrt(num)}")

sqrtInvoke()
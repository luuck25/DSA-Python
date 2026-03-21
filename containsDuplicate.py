
import sys


def main():
    print("Hello from main!")


def containsDuplicate(nums):
    num_freq = {}
    for num in nums:
        if num in num_freq:
            return True
        else: num_freq[num] =1
    return False

print(containsDuplicate([1,3,4,3]))


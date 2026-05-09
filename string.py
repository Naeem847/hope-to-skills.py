# # # # 1. The string in reverse order.
text=str(input("enter your text:"))

reverse_text=text[::-1]
print("reversed string is:",reverse_text)


vowels="aeiouAEIOU"
vowels_count  =0

for char in text:
    if char in vowels:
        vowels_count  +=1

print("reversed string:",reverse_text)
print("number of vowels in the string:",vowels_count)

# # #  2: Hands-on Coding Project

num=int(input("enter a number:"))
if num%2==0:
    print(f"the number {num} is even:")
else:
    print(f"the number{num} is odd:")
# # # # 3: Hands-on Coding Project
import numpy as np

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

#6: Sort the list using numpy.sort()
sorted_numbers = np.sort(numbers)

#7: Print the sorted list
print("Sorted list:", sorted_numbers)

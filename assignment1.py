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
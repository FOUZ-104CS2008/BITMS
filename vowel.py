name=input("enter the name:")
vowels="aieou"
result=[char for char in name if char in vowels]
print("this is vowel letter",result)


result=[char for char in name if char  not in vowels]
print("this not vowels letter",result)


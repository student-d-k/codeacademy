
s = "Learning Python is Fun!"

print(s.count("n"))

print(len(s.split()))

# import re 
  
# def is_vowel(char): 
#     if re.match(r'[aeiouAEIOU]', char): 
#         return True
#     return False
  
# print(is_vowel('a'))  # Output: True 
# print(is_vowel('b'))  # Output: False 

# def isVowel2(ch): 
#     switcher = { 
#         'a': "*", 
#         'e': "*", 
#         'i': "*", 
#         'o': "*", 
#         'u': "*", 
#         'A': "*", 
#         'E': "*", 
#         'I': "*", 
#         'O': "*", 
#         'U': "*"
#     } 
#     return switcher.get(ch, ch) 
  
# # Driver Code 
# print('a is '+isVowel2('a')) 
# print('x is '+isVowel2('x')) 

print(s.translate(str.maketrans("aeiouAEIOU", "*"*10)))
# s= "malaykalam"
# a = 0
# for i in range(len(s)):
#     if s[i] != s[len(s) -i-1]:
#         a = 1
#         break
# if a == 0:
#     print("palindrome")
# else:
#     print("not a palindrome")

def isPalindrome(s):
    return s == s[::-1]

s= "malaykalam"
print(isPalindrome(s))
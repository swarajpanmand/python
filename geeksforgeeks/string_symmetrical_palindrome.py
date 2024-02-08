s= "khokho"
half = int(len(s)/2)

if s[:half] == s[half:]:
    print("symmetrical")
else:
    print("not symmetrical")

if s == s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
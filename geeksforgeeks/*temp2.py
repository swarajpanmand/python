def binary(s):
    count = 0
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[i] != s[j] and s[j] != s[k]:
                    count += 1
    return count

def number(n):
    s = str(n)
    parts = []
    for i in range(0, len(s), 6):
        part = s[i:i+6]
        parts.append(part)
    return parts

n = input()
print(binary(n))


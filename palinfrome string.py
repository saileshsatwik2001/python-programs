s = "Madam"
s = s.lower()
is_palindrome = True
n = len(s)

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_palindrome = False
        break

print("Is Palindrome?" , is_palindrome)
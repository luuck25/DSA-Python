

def vowels(s):
    if len(s) <= 0:
        return 0
    count = 1 if s[0] in 'aieou' else 0
        

    return count + vowels(s[1:])

print(vowels("acdee"))
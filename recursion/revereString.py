



# lakesh


def reverse_string(s):
    # Base case
    if s == "":
        return ""

    # Recursive call
    return reverse_string(s[1:]) + s[0]
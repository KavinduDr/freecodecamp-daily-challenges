test_string = "Hell World 12"

def is_balanced(s):
    s_no_spaces = s.replace(" ", "") # remove spaces
    s = s_no_spaces.lower() # convert to lowercase
    vowels = "aeiou"
    
    i=0
    j=len(s)-1

    no_of_vowerls_lower=0
    no_of_vowerls_upper=0

    while i < j:
        if s[i] in vowels:
            no_of_vowerls_lower += 1
        if s[j] in vowels:
            no_of_vowerls_upper += 1
        i += 1
        j -= 1

    return no_of_vowerls_lower == no_of_vowerls_upper

print(is_balanced(test_string))  # Output: False
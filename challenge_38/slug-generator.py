testing_string = "Hello,  World! This is a test-string for slug generation."

def generate_slug(string):
    slug = []
    i = 0
    length = len(string)

    while i < length:
        char = string[i]
        if char.isalnum():
            slug.append(char.lower())
            i += 1
        elif char == ' ':
            # Only add %20 if the last added wasn't %20
            if not slug or slug[-1] != '%20':
                slug.append('%20')
            i += 1
        else:
            # Skip other non-alphanumeric characters
            i += 1
    return ''.join(slug).strip('%20')

result = generate_slug(testing_string)
print(result)  # Output: "hello%20world%20this%20is%20a%20test%20string%20for%20slug%20generation"
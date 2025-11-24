def is_validate_message(message, validation):
    
    firstLetters = [word[0].lower() for word in message.split(' ') if word]
    validation = validation.lower()
    
    if len(firstLetters) != len(validation):
        return False
    for i in range(len(validation)):
        if firstLetters[i] != validation[i]:
            return False
    
    return True

print(is_validate_message("Hello world", "hw"))
print(is_validate_message("ALL CAPITAL LETTERS", "acl"))
print(is_validate_message("Coding Challeng are boring", "cca"))
print(is_validate_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
print(is_validate_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))
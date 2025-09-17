paragraph = "hello world.? this is a test paragraph. let's see how it works!"

def capitalize_sentences(paragraph):
    sentences = []
    i = 0
    
    while i < len(paragraph):
        # Find the start of current sentence
        start = i
        # Skip any leading whitespace
        while i < len(paragraph) and paragraph[i].isspace():
            i += 1

        # Find the end of current sentence
        while i < len(paragraph) and paragraph[i] not in '.?!':
            i += 1

        # Include the punctuation marks
        while i < len(paragraph) and paragraph[i] in '.?!':
            i += 1

        # Extract the sentence
        sentence = paragraph[start:i]

        # Capitalize first letter if sentence is not empty
        if sentence.strip():
            # Find first alphabetic character
            for j, char in enumerate(sentence):
                if char.isalpha():
                    sentence = sentence[:j] + char.upper() + sentence[j+1:]
                    break

        sentences.append(sentence)

    return ''.join(sentences)

result = capitalize_sentences(paragraph)
print(result)
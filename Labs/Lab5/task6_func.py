# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

user_input = input()
reversed_sentence = reverse_words(user_input)
print(reversed_sentence)
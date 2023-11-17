
def longest_words(file):
    with open('poem.txt', 'r', encoding='utf-8') as f:

        words = f.read().split()
        max_length = max(len(word) for word in words)
        longest_word = [word for word in words if len(word) == max_length]
        print(longest_word)


longest_words('poem.txt')

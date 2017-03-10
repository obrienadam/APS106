def word_count(filename):
    with open('article.txt', 'r') as f:
        text = f.read().replace('\n', ' ').replace('-', ' ')

    # We may want to remove any non-alphabetic characters, eg punctuation
    processed_text = ''
    for ch in text:
        if ch.isalpha() or ch == ' ':
            processed_text += ch.lower()

    word_freq = {}
    for word in processed_text.split():
        if word.isalpha(): # Make sure it's a word, we may have missed special cases
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq

if __name__ == '__main__':
    word_freq = word_count('article.txt')

    max_freq = 0

    for word, freq in word_freq.items():
        if freq > max_freq and len(word) >= 4:
            max_freq = freq
            max_freq_word = word

    print('The most common four letter word was "{}", which appeared {} times.'.format(max_freq_word, max_freq))
    print('In total, there were {} words, with {} unique words.'.format(sum(word_freq.values()), len(word_freq)))
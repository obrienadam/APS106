from wiki_article import article

if __name__ == '__main__':
    words = article.replace('\n', ' ').split(' ')
    print('There are', len(words), 'words in the article,', len(words) - len(set(words)), 'of which are unique.')
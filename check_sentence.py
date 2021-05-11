def get_dictionary() -> list:
    """Write words from dictionary to list

    Args:
        None.

    Returns:
        List of words that contains dictionary.txt.
    """
    dictionary = []
    with open('data/dictionary.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dictionary.append(line[:-1])
    return dictionary


def find_errors(list_of_words: list, dictionary: list) -> list:
    """"Find incorrect words in input list.

    Args:
        list_of_words: List that contains words from input sentences.
        dictionary: Dictionary that contains all words.

    Returns:
        List of incorrect words.
    """
    error_words = []
    for word in list_of_words:
        if word.lower() not in dictionary:
            error_words.append(word)

    return error_words


def print_errors(error_list: list) -> None:
    """"Print errors.

    Args:
        error_list: List of incorrect words.

    Returns:
        None.
    """
    error_word = 'Incorrect words: '
    if error_list:
        for index, _ in enumerate(error_list):
            if index == (len(error_list) - 1):
                error_word = error_word + error_list[index] + '.'
            else:
                error_word = error_word + error_list[index] + ', '
        print(error_word)
        print('\n\n')
    else:
        print('All is correct! Great work!')
        print('\n\n')


def preprocessing_sentence(sentence: str) -> str:
    """"Remove all punctuation from input sentence.

    Args:
        sentence: Input sentence.

    Returns:
        Sentences without punctuation.
    """
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in sentence:
        if item in punctuation:
            sentence = sentence.replace(item, "")

    return sentence


def check() -> None:
    """"Start check input sentence.

    Args:
        None.

    Returns:
        None.
    """
    sentence = input('Enter the sentence to check: ')

    new_sentence = preprocessing_sentence(sentence)
    list_of_words = new_sentence.split(' ')
    dictionary = get_dictionary()
    error_list = find_errors(list_of_words, dictionary)
    print_errors(error_list)


def main() -> None:
    """Start point.

    Args:
        None.

    Returns:
        None.
    """
    switch_dict = {'1': check,
                   '2': exit
                   }
    while True:
        print('-------------------------')
        print('MENU                    |')
        print('1. Enter the sentence.  |')
        print('2. Exit.                |')
        print('-------------------------')
        value = input('Enter the value: ')
        print('\n')

        try:
            switch_dict[value]()
        except KeyError:
            print('Error! Try again enter the value!')
            print('\n')


if __name__ == '__main__':
    main()

import re
import string


# --- File Operations --- #

def read_file(file_name):
    """
    Reads the file, converts all text to lowercase, and tokenizes the words.
    
    :param file_name: Path to the text file.
    :return: List of words from the file.
    """
    with open(file_name, 'r') as f:
        file_content = f.read().lower()
    words = re.findall(r'\w+', file_content)
    return words


# --- Word Count --- #

def count_words(word_list):
    """
    Counts the frequency of each word in the list.
    
    :param word_list: List of words.
    :return: Dictionary with word counts.
    """
    word_count_dict = {}
    for word in word_list:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
    return word_count_dict


# --- Probability Calculation --- #

def calculate_probabilities(word_count_dict):
    """
    Calculates the probability of each word based on its frequency.
    
    :param word_count_dict: Dictionary with word counts.
    :return: Dictionary with word probabilities.
    """
    total_count = sum(word_count_dict.values())
    probabilities = {word: count / total_count for word, count in word_count_dict.items()}
    return probabilities


# --- Word Manipulation --- #

def delete_letter(word):
    """
    Deletes one letter from each position in the word.
    
    :param word: The word to be modified.
    :return: List of words with one letter deleted.
    """
    return [word[:i] + word[i+1:] for i in range(len(word))]


def switch_letters(word):
    """
    Switches adjacent letters in the word.
    
    :param word: The word to be modified.
    :return: List of words with adjacent letters switched.
    """
    switch_l = []
    for i in range(len(word) - 1):
        swapped = list(word)
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
        switch_l.append("".join(swapped))
    return switch_l


def replace_letter(word):
    """
    Replaces each letter in the word with every other letter from the alphabet.
    
    :param word: The word to be modified.
    :return: List of words with each letter replaced by others.
    """
    letters = string.ascii_lowercase
    replace_l = set()
    for i in range(len(word)):
        for letter in letters:
            if word[i] != letter:
                replace_l.add(word[:i] + letter + word[i+1:])
    return sorted(list(replace_l))


def insert_letter(word):
    """
    Inserts each letter of the alphabet into each position of the word.
    
    :param word: The word to be modified.
    :return: List of words with letters inserted.
    """
    insert_l = []
    for i in range(len(word) + 1):
        for letter in string.ascii_lowercase:
            insert_l.append(word[:i] + letter + word[i:])
    return insert_l


# --- Main Program --- #

def main(file_name):
    """
    Main program to read the file, calculate word frequencies, and generate word variations.
    
    :param file_name: Path to the text file.
    """
    print("Reading file and processing words...\n")
    word_list = read_file(file_name)
    
    print(f"Total words found: {len(word_list)}")
    print(f"Unique words: {len(set(word_list))}\n")
    
    word_count_dict = count_words(word_list)
    print(f"Word count for the word 'the': {word_count_dict.get('the', 0)}\n")
    
    word_probabilities = calculate_probabilities(word_count_dict)
    print(f"Probability of the word 'the': {word_probabilities.get('the', 0):.4f}\n")
    
    sample_word = "cat"  # You can change this to any word you want to manipulate
    
    print(f"Word Manipulations for '{sample_word}':\n")
    print("Deleting letters:")
    print(delete_letter(sample_word))
    
    print("\nSwitching adjacent letters:")
    print(switch_letters(sample_word))
    
    print("\nReplacing letters with alphabet:")
    print(replace_letter(sample_word))
    
    print("\nInserting letters:")
    print(insert_letter(sample_word))


# --- Run the Program --- #
if __name__ == "__main__":
    file_name = 'your_text_file.txt'  # Replace with the actual file path
    main(file_name)

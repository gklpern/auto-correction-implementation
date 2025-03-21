# Word Transformer

This Python project allows you to transform and analyze words from a text file. The tool provides functionality for:
- Reading a text file and extracting words
- Counting word frequencies and calculating probabilities
- Generating word variations by deleting, switching, replacing, and inserting letters.

It is designed to work with any plain text file and can be customized further for NLP tasks or text analysis.

## Features

- **Word Counting**: Counts the frequency of each word in the given text.
- **Probability Calculation**: Calculates the probability of each word based on its frequency.
- **Word Manipulations**: 
    - Delete a letter from each position in a word.
    - Switch adjacent letters in a word.
    - Replace each letter in a word with every letter from the alphabet.
    - Insert each letter from the alphabet into each position of a word.

## Requirements

- Python 3.x
- `re` module (Standard Library)
- `string` module (Standard Library)

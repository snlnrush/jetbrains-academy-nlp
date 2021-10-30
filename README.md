# JetBrains Academy, track "Natural Language Processing" (NLP)

Embark upon this track to get the essential skills of working with text data. Texts constitute the lion's share of all information stored on the Internet and beyond. This track will equip you with the right tools to process text data and extract useful information from it.


## Project: Text Generator

### About

Machine learning is getting crazy smart these days. You've probably read texts or scripts written by machine learning algorithms, some of them even mimicking styles of certain people! If you ever wondered how it works and what are the secrets behind machine learning, this project is for you! You will have a chance to understand and implement a simple text generator using Markov chains.

### Learning outcomes
You will create a program that can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model. You will get a deeper understanding of natural language processing, string operations, and the application of statistics in your code.

#### Stage 1: Preprocess the text corpus

Open the given text corpus, break the text into separate words, and obtain some properties of the corpus.

#### Stage 2: Break the dataset into bigrams

Bigrams are sequences of two consecutive words from the dataset. Transform the preprocessed corpus into a list of bigrams.

#### Stage 3: Create a Markov chain model

Create a Markov chain model that shows the probability of certain words appearing after a given chain of words.

#### Stage 4: Generate random text

Use the Markov model to generate a text starting with a user-specified word and handle exceptions.

#### Stage 5: Generate full sentences

Modify the algorithm so that sentences always start with capital letters and end with punctuation marks.

#### Stage 6: Generate sentences based on trigrams

Extend the program to create a Markov model based on trigrams in order to generate more sensible sentences.


## Project: Regex Engine

### About

Regular expressions are a fundamental part of computer science and natural language processing. In this project, you will write an extendable regex engine that can handle basic regex syntax, including literals (a, b, c, etc.), wild-cards (.), and metacharacters (?, *, +, ^, $).

### Learning outcomes

Learn about the regex syntax, practice working with parsing and slicing, and get more familiar with boolean algebra and recursion.

#### Stage 1: Single character strings

Implement a program that compares two single character strings (including the wildcard) and determines if there's a match.

#### Stage 2: Matching two equal length strings

Extend your engine to compare two equal length strings using recursion.

#### Stage 3: Working with strings of different length

Add the ability to compare a regex to strings that vary in length.

#### Stage 4: Implementing the operators ^ and $

Extend the engine to handle the operators ^ and $ that control the position of the regex within a string.

#### Stage 5: Controling repetition

Support the additional operators ?, *, and + that control the repetition of a character within a string.

#### Stage 6: Escaping

Finally, implement the backslash \ as an escape symbol that allows to use metacharacters as literals.
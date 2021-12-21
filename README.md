# JetBrains Academy, track "Natural Language Processing" (NLP)

Embark upon this track to get the essential skills of working with text data. Texts constitute the lion's share of all information stored on the Internet and beyond. This track will equip you with the right tools to process text data and extract useful information from it.


## 1. Project: Text Generator

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


## 2. Project: Regex Engine

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


## 3. Project: Key Terms Extraction

### About

Extracting keywords can help you get to the text meaning. Also, It can help you with splitting texts into different categories. In this project, you will learn how to extract relevant words from a collection of news stories. There are many different ways to do it, but we will focus on frequencies, part-of-speech search, and TF-IDF methods. Note that each method can yield the results with varying degrees of accuracy for different texts. In reality, it is always good to try various methods and choose the best.

### Learning outcomes

By completing this project, you will get to know and implement crucial text preprocessing stages, use an essential NLP library, and program maths formulas! Along the way, you will create a useful tool and learn how to handle reading and writing files with confidence.

#### Stage 1: Most frequent words

Read a file containing news articles, lowercase the text, tokenize it with the NLTK tokenizer's help, and create a token frequency list.

#### Stage 2: Text preprocessing pipeline

Improve the results by applying lemmatization and deleting stop-words, digits, and punctuation.

#### Stage 3: Nouns are keywords

Discover how to use part-of-speech tagging to extract the most frequent nouns and refine your keywords.

#### Stage 4: Modifying frequencies for better results

Find out how to identify words with the highest TF-IDF score.


## 4. Project: Web Scraper

### About

You will create a function that takes a website address and a number of webpages as input arguments and then goes all over the website saving every news article on the page to a separate .txt file on your computer.

### Learning outcomes

After finishing the project, you’ll know how to send HTTP-requests and process the responses, how to work with an external library, library documentation, and how to use it for parsing the website data. You will also find out how to make your program save results to a file with the help of Python.

#### Stage 1: Wanna Talk to the Internet?

Send an HTTP request, process the results, and learn about response status codes.

#### Stage 2: The Beautiful Soup Ingredients

Get familiar with the BeautifulSoup library. Learn how to parse simple data from a webpage.

#### Stage 3: What the file?

Learn to work with files.

#### Stage 4: The Soup is Real

Create a function that scrapes every article on a page with a for loop.

#### Stage 5: Soup, Sweet Soup

Improve the function by adding ‘webpage number’ and 'article type' parameters.

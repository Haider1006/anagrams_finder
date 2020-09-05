# Anagram Finder Programming

An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

## Getting Started

Download the anagrams_finder.py file and you are good to go.

## Prerequisites

python 3 (preferably)
jupyter notebook (optional)
Dictionary.txt file
Libraries Needed: time, collection, test 

## Code Explained:
1. Define a function word_sort
--This takes one word input and sorts that word alphabetically, removing spacing(\n) and converting it to the lower case.

2. Define a function load_words
---This takes the "Dictionary.txt" filepath as input.
To time the function process, calculate time using start time at the starting and stop time at the end of this function.
Next, a blank dictionary wordlist is taken. 
The iterate the whole txt file fetching one line each time, sorting the word and putting it to the Python Dictionary (wordlist).
Print the length of the word list to see how many words have been loaded. It should load 235886 words from the text file to the user defined dictionary.
Also, print the time it took to load the dictionary.

3. Driver function
--- Load the wordlist defined, take a blanklist(anagrams), iterate over the dictionary using enumeration and check the sorted_input word with the
value in the dictionary, wherever it finds, it adds to the blanklist. Otherwise, prints no anagram found, exit only when prompted. 

## Installing

run from command prompt
python anagram_finder.py 

## Demo:
![s1](https://user-images.githubusercontent.com/66070119/92314270-349e9980-ef9b-11ea-9c92-3befc7687202.png)
![s2](https://user-images.githubusercontent.com/66070119/92314274-3c5e3e00-ef9b-11ea-9e20-020eeab3007a.png)


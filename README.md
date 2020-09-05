# Anagram Finder Programming

An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing urposes. See deployment for notes on how to deploy the project on a live system.
Download the py file and upload it to your jupyter notebook and you are good to go.

## Prerequisites

What things you need to install the software and how to install them
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

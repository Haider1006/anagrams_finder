# Anagram Finder Programming

An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

## Getting Started

Download the anagrams_finder.py file and you are good to go.

## Prerequisites

python 3 (preferably)<br/>
jupyter notebook (optional)<br/>
Dictionary.txt file<br/>
Libraries Needed: time, collection, test <br/>

## Code Explained:
1. Define a function word_sort<br/>
--This takes one word input and sorts that word alphabetically, removing spacing(\n) and converting it to the lower case.<br/>

2. Define a function load_words<br/>
---This takes the "Dictionary.txt" filepath as input.<br/>
To time the function process, calculate time using start time at the starting and stop time at the end of this function.<br/>
Next, a blank dictionary wordlist is taken. <br/>
Then iterate the whole txt file fetching one line each time, sorting the word and putting it to the Python Dictionary (wordlist).<br/>
Print the length of the word list to see how many words have been loaded. It should load 235886 words from the text file to the user defined dictionary.<br/>
Also, print the time it took to load the dictionary.<br/>

3. Driver function<br/>
--- Load the wordlist defined, take a blanklist(anagrams), iterate over the dictionary using enumeration and check the sorted_input word with the
value in the dictionary, wherever it finds, it adds to the blanklist. Otherwise, prints no anagram found, exit only when prompted. <br/>

## Installing

- Open the terminal/command prompt
- Navigate to the directory where you downloaded anagrams_finder/src
- run from command prompt<br/>
    python anagram_finder.py <br/>

## Demo:
![image](https://user-images.githubusercontent.com/66070119/92318733-3b96cd80-efd6-11ea-955c-0b705217bf6e.png)
![image](https://user-images.githubusercontent.com/66070119/92318810-2b332280-efd7-11ea-99c7-7ac39a7e4efc.png)


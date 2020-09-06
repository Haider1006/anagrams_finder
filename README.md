# **Anagram Finder Programming**

An anagram is a word, phrase, or name formed by rearranging letters of the original word to make a new word. Examples of an anagram are below:

1. State : Taste
2. Cinema : Iceman

The purpose of this anagram finder is to find if the search word has anagrams or not.

## Getting Started

Download the anagram.py file and the dictionary.txt file and you are good to go.

## Prerequisites

To setup the project to run locally on your system, you need to install/download the following softwares and files:
1. python 3 (preferably)<br/>
2. jupyter notebook or spyder (optional)<br/>
3. Dictionary.txt file<br/>
4. Python Libraries Needed: time, collection, test <br/>

## Code Explained:
###### 1. Define a python function word_sort<br/>
This takes one word input and sorts that word alphabetically, removing spacing(\n) and converting it to lower case.<br/>

###### 2. Define a function load_words<br/>
This takes the "Dictionary.txt" filepath as input.<br/>
To time the function process, calculate time using start time at the starting and stop time at the end of this function.<br/>
Next, a blank dictionary wordlist is taken. <br/>
Then iterate the whole txt file fetching one line each time, sorting the word and putting it to the Python Dictionary (wordlist).<br/>
Print the length of the word list to see how many words have been loaded. It should load 235886 words from the text file to the user defined dictionary.<br/>
Also, print the time it took to load the dictionary.<br/>

###### 3. Driver function<br/>
Load the wordlist defined, take a blanklist(anagrams), iterate over the dictionary using enumeration and check the sorted_input word with the
value in the dictionary, wherever it finds, it adds to the blanklist. Otherwise, prints no anagram found, exit only when prompted. <br/>

## Installing

- Open the terminal/command prompt
- Navigate to the directory where you have downloaded anagrams_finder/src
- Run the below command from command prompt<br/>
    python anagram_finder.py <br/>

## Demo:
![image](https://user-images.githubusercontent.com/66070119/92318733-3b96cd80-efd6-11ea-955c-0b705217bf6e.png)
![image](https://user-images.githubusercontent.com/66070119/92318810-2b332280-efd7-11ea-99c7-7ac39a7e4efc.png)

## Optimization Future Scope
To further optimize the present technique, the dictionary can be sorted based on the length of words. Given the length of the word to be searched, we can extract only the words that have the same length as the searched string from the dictionary. This will enhance the speed of finding the anagram as we will only iterate over the section of words which match the length of the search word.

## Author

- Yadullah Haider <br/>
    Contact- yadhaider@gmail.com


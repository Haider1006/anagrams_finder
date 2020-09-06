# **Anagram Finder Programming**

An anagram is a word, phrase, or name formed by rearranging letters of the original word to make a new word. Examples of an anagram are below:

1. State : Taste
2. Cinema : Iceman

The purpose of this anagram finder is to find if the search word has anagrams or not.

## Getting Started

Download the anagram.py file and the dictionary.txt file in your local and you are good to go.

## Prerequisites

To setup the project to run locally on your system, you need to install/download the following softwares and files:
1. python 3 (preferably)<br/>
2. jupyter notebook or spyder (optional)<br/>
3. Dictionary.txt file<br/>
4. Python Libraries Needed: time, collection, test <br/>

## Code Explained:
###### 1. Define a python function word_sort<br/>
This function takes one word input and sorts that word alphabetically, removing spacing(\n) and converting it to lower case.<br/>

###### 2. Define a function load_words<br/>
This function accepts a single parameter which is the filepath of the "Dictionary.txt" file as input.<br/>

To include the output timings of the time taken to load the dictionary and the time taken to check if the search word is anagram or not, calculate the time using start-time at the starting and stop-time at the end of this function.<br/>

Next, an empty dictionary wordlist is initialized. The function then, iterates over the complete "dictionary.txt" file fetching one line each time, sorting the word and putting it to the Python Dictionary (wordlist).<br/>

To keep a track of the count of words in the dictionary, the function prints the length of the word list to see how many words have been loaded. It should load 235886 words from the text file to the user defined dictionary.<br/>

In the end, the function prints the time taken to load the dictionary.<br/>

###### 3. Driver function<br/>
Load the wordlist created, take a blanklist(anagrams), iterate over the dictionary using enumeration and check the sorted_input word with the
value in the dictionary. Wherever there is a match, it adds the word to the blanklist. 

Else, it prints no anagram found along with the time taken, or it exits the application when exit is prompted. <br/>

## Installing

- Open the terminal/command prompt
- Navigate to the directory where you have downloaded anagrams_finder/src
- Run the below command from command prompt<br/>
    python anagram_finder.py <br/>

## Demo:

When the anagram finder application is initialized, the user sees the below welcome page: <br/>

![image](https://user-images.githubusercontent.com/66070119/92318733-3b96cd80-efd6-11ea-955c-0b705217bf6e.png) <br/>

The user can input the search word into the terminal and check if the word has anagrams or not. <br/>

To exit the application, the user can type in 'exit' as input. The application will exit. 

![image](https://user-images.githubusercontent.com/66070119/92318810-2b332280-efd7-11ea-99c7-7ac39a7e4efc.png) <br/>

The output of the anagram finder application:

1. Displays the anagrams when found along with the time taken
2. Displays no anagrams found when anagrams do not exist along with the time taken

## Future Optimization Scope
To further optimize the present technique, the dictionary can be sorted based on the length of words. Given the length of the word to be searched, we can extract only the words that have the same length as the searched string from the dictionary. This will enhance the speed of finding the anagram as we will only iterate over the section of words which match the length of the search word.

## Author

- Yadullah Haider <br/>
    Contact- yadhaider@gmail.com


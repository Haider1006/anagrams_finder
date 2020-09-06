import time
import unittest

def word_sort(word):
    
    return ''.join(sorted(word)).lower().strip('\n')

def load_words(filepath):
    start_time = time.time()
    wordlist = {}
       # 'with' can automate finish 'open' and 'close' file
    with open("dictionary.txt") as f:
            # fetch one line each time, include '\n'
            for line in f:
                wordlist[line] = {}
                wordlist[line]=word_sort(line)
    print("Welcome to the Anagram Finder")
    print("--------------------------")
    print ("Initialized in %s ms" %int((time.time() - start_time)*1000))
      
    return wordlist

wordlist = load_words('dictionary.txt')
new = True
while True:
    word = input("Anagram Finder>")
    if (word != 'exit'):
        start_time = time.time()
        anagrams = []
        sorted_input = word_sort(word)
        
        for index, (key, value) in enumerate(wordlist.items()):
            if (sorted_input==value):
                anagrams.append(key.rstrip('\n'))
        if not anagrams:
            print("No anagrams found for %s" %word)
        else:
            print( "%d Anagram(s) found for %s in %s ms"
                      %(len(anagrams), word, int((time.time() - start_time)*1000)))
            print (anagrams)

    elif (word == 'exit'):
        break

#UnitTest
class testAnagram(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        result=word_sort('zygospore\n')
        expected='egooprsyz'
        self.assertEqual(result,expected,msg='Equal')
  
if __name__ == '__main__': 
    unittest.main()
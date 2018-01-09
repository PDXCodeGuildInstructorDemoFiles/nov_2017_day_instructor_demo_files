# PYTHON:
1.  ari
2.  case converter
3.  change return
4.  distance-converter
5.  random dice
6.  hammer time
7.  phonebook
8.  madlib
9.  pig latin
10. Road Trip
11. i before e
12. word count
13. python weather using openweather api

# JAVACRIPT
14. angry_dice
15. change return
16. weather app
17. is a vowel
18. capstone mvp


# 1 Lab: Compute Automated Readability Index

##### Delivery Method: Prompt Only

----------------------------------

#### Goal

Compute the ARI for a given body of text loaded in from a file.  The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text.

----------------------------------


##### Automated Readability Index Formula

The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

In plain English, the score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up.

Scores correspond to the following ages and grad levels:

```
    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
```

----------------------------------

#### Instructions


1. Create a new directory called `ari` in your code repo
1. Create a file called `main.py` file in the `ari` directory

When the user runs `main.py`, they should be presented with a menu of choices of the above files to choose from that looks something like the following:

    To compute its automated readability index,
    pick from one of the files below:

    1) geneology-of-morals.txt
    2) gettysburg-address.txt
    3) jack-and-jill.txt

    or

    q) Quit

The list of files should be generated from the files in the `ari` directory that have `.txt` for their extension.

After choosing one of the files, the output should look something like the following:

    --------------------------------------------------------

    The ARI for the file, gettysburg-address.txt, is 12.
    This corresponds to a 11th Grade level of difficulty
    that is suitable for an average person 16-17 years old.

    --------------------------------------------------------

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level:

    ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

# 2 Lab: Case Conversion

###### Delivery Method: Doctests

##### Goal

Write a program that prompts the user for a word.
Print out either  `snake_case` or `CamelCase` depending case convention it is!.

--------------------

##### Instructions

Use substring membership with the `in` operator

-------------------
#### Documentation

1. [PEP8](https://www.python.org/dev/peps/pep-0008/)
1. [Stack Overflow](http://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names)

---------------------
#### Key Concepts:

- Python social conventions for variable and function naming


# 3 Lab: Change Return

###### Delivery Method: Doctests

------------------------------

##### Goal

Write a python script that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.

---------------------------------------------------------

##### Instructions

Some supermarkets have automatic change dispensers.

*   Ask for the amount of change to dispense _in cents_.
    Assume that the amount input will be less than 100 cents.

*   Calculate the number of quarters necessary first.

*   Then calculate the number of dimes, nickels, and pennies.
    If you do it in that order, you will minimize the number of coins.

This is easiest done by updating a _running total_ of number of cents left to be put into coins.

Also remember that the `//` operator divides and removes any remainder.

------------------

#### Documentation

##### [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

-----------------

#### Advanced

* Expand this problem to work on an amount of cents greater than 100 and include bills.
* Print out the total number of coins and bills dispensed.

--------------------
#### Super Advanced

* Store how many of each coin is in the cash register, then allow the change algorithm to deal with when you don't have enough coins to optimally give change.

------------------

#### Key Concepts

- Operators
- Variables
- Data Types
- PEP8

# 4 Lab: Distance Converter

###### Delivery Method: Prompt Only

--------------

##### Goal

Write a function to convert between `mi`, `km`, `ft`, and `m`.

--------------------

##### Instructions

Ask the user for a distance, then the units of that distance, then the target units.
Then print out the conversion as below.

```
> Enter a distance:
> 100
> Enter units:
> mi
> Enter target units:
> km
> 100 mi is 160.93440000000115 km
```

Support converting between `mi`, `km`, `ft`, and `m`.


-------------------

#### Documentation

1. [Python Official: Built-In Functions](https://docs.python.org/3.6/library/functions.html)

1. [Python Official: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

----------------------


## Advanced

*   Also support converting between `in` and `cm`.

*   Also support converting between `gal` and `L`.
    Error if someone tries to convert between volume and distance. Use `raise`.

-------------------


## Super Advanced

* Also support converting between all [metric prefixes](https://en.wikipedia.org/wiki/Metric_prefix) of meters.


------------------------
#### Key Concepts

- Variables
- Function definition
- User input
- Built-In functions
- Logic Problems

# 5 Lab: Random Dice

###### Delivery Method: Prompt Only

##### Goal

Write a simple program that, when run, prompts the user for input then prints a result.

--------------------

##### Instructions

Program should ask the user for the number of dice they want to roll as well as the number of sides per die.

1. Open Atom
1. Create a new file and save it as `dice.py`
1. Follow along with your instructor

-------------------
#### Documentation

1. [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
1. [Python Std. Library: Random Module random.randint()](https://docs.python.org/3/library/random.html#random.randint)

----------------------
#### Key Concepts

- Importing
- The Random Module
- `for` looping
- `input()` function
- programmatic logic




# 6 Lab: Hammer Time

###### Delivery Method: Doctests

------------------------------

##### Goal

Write a function that returns the meal for any given hour of the day or night in respect to the following schedule:

```
Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM
```

---------------------------------------------------------

##### Instructions

1. Open Atom
1. Create a new file and save it as `hammer.py`
1. Implement the program, ideally without peeking at the solution

------------------

#### Documentation

1. [Python Official Docs: Operators](https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions)

------------------

#### Key Concepts

- Function Definition
- `if` Expressions
- `elif` Expressions
- Operators



# 7 Lab: Phonebook

'''
Create a program that uses a dictionary to store phonebook
entries. Must have user interaction.
Include ability to:
1. Search
2. Add Entry
3. Chage Entry
4. Delete Entry
5. Exit Program
'''

# 8 Lab: madlib.py

------
#### Goal

Write a simple program that, when run, prompts the user for several inputs then
 prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.

-------
#### Instructions

  1. Search the interwebs for an example Mad Lib
  1. Open Atom
  1. Create a new file and save it as `madlib.py`

Example:

```
>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.
```
------


#### Documentation

1. [Common string operations](https://docs.python.org/3.1/library/string.html)

-------

#### Advanced
* Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
* Add randomness! Use the random module, rather than selecting which adjective goes where in the story.


#### Super Advanced
* Not satisfied yet? Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.

#### Key Concepts

- Variables
- String formatting¹
- Handling user input

------

# 9 Lab: Pig Latin

#### Goal

Create a program asks for a _single_ English word and translates
it to **Pig Latin**.
It prints out the input word and the resulting translation like
the example below.
---------------------------------
#### Instructions
1. If the first letter is a consonant, move it to the end.
1. Add "ay" to the end of that.
1. If the first letter is a vowel, just ad "yay" to the end.


# get a word from user
word = input('What word would you like translated?: ')
# split first letter from word so we have two parts
vowels = 'aeiou'
consonant = -1

for letter in word:
    if letter.lower() in vowels:
        break
    else:
        consonant += 1

first_letter = word[0:consonant + 1]
left_over = word[consonant + 1:]

# list vowels
# compare first letter to list of vowels
if first_letter.lower() in vowels:
    # if true add word + 'yay'
    print('{0} in Pig Latin is {0}yay'.format(word))
# else move first letter to the end of word and add 'ay'
else:
    if first_letter[0].isupper():
        print('{0} in Pig Latin is {1}{2}ay.'.format(word, left_over.capitalize(), first_letter.lower()))
    else:
        print('{0} in Pig Latin is {1}{2}ay.'.format(word, left_over, first_letter))


# 10 Practice: Road Trip


In a faraway land, nearby cities are connected by roads.
We've mapped what cities are directly connected by roads and stored them in a dict:


```python
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
```


Traveling from one city to an adjacent one is called a **hop**.

For this sort of problem, you'll want to iteratively visit cities you know you can access while updating:
1. Cities you can access.
1. Cities you've been to.
1. Cities you haven't been to.

* Let the user enter a city.
Print out all the cities connected to that city.
* Let the user enter a city.
Print out all cities that could be reached through two hops.



## Advanced
* Let the user enter a city and a number of hops.
Print out all cities that could be reached through that number of hops.
* We've also mapped the travel time of each hop:


```python
city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
```


When the user enters a city and a number of hops, print out the shortest travel times to each city.
Paths with fewer hops are not necessarily those with the shorter travel times.

# 11 Lab: I before E except after C.

From wikipedia:
"The i before e except after c rule is not worth teaching. It applies only to words in which the ie or ei stands for a clear /ee/ sound and unless this is known, words such as 'sufficient', 'veil' and 'their' look like exceptions."

###### Delivery Method: Prompt

------------------------------

#### Goal

Create a program that asks for a _single_ English word and checks if it follows the rule **"I before E except after C".**


---------------------------------------------------------

#### Instructions

1. Create a file named `spelling.py`
1. Write a function that searches for the index of any instances of `ie` in the string, then see if the preceding letter is `c`.


------------------

#### Documentation


-----------------

#### Advanced

* Find a list of exceptions to use and check if the word given is an exception to the rule.


------------------

#### Key Concepts

- string lookup with `in`

# 12 Lab: Word Count

###### Delivery Method: Prompt Only

------------------------------------

#### Goal

Write a python module to analyze a given text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.

------------------------

#### Instructions

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.

1. Open the file and deal with any decoding errror that arise.

1.  Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.

1.  Count how often each unique word is used, then print the most frequent top 10 out with their counts.

1. Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.



--------------------------------------------------------

#### Advanced

1. Make a command line tool with the `sys.argv`.  Allow the the user to pass in the filename to a `.txt` file when execiting your program.  Use the `sys.argv` to parse the filename to use for the analysis.


---------------------------------------------------------

#### Super Advanced

1. Allow the user to enter a word and get the most likely words to follow the given word.  Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.
    ```
    Enter Query Word > Mr.
    The most likely bi-gram pair starting with "Mr." is "Mr. Darcy".
    ```

1. Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

1. Chain together that ability to generate random sentences, one word at a time, from a given starting word.
This is a language model.

# 13 Lab: PyWeather

Create a program that will propt a user for city name or zip code.
Use that information to get the current weather. Display that information
to the user in a clean way.
## Advanced

* Also ask the user if they would like to see the results in C or F.


# 14 Angry Dice

_An assignment to create the game Angry Dice with Javascript, HTML, and CSS._

This project allows a user to play Angry Dice in the web browser.
The browser enforces the rules of the game, progressing through the three stages for the user, and moving them back to
Stage 1 when they roll double Angry faces.

The full rules of the game are below:

## The Battle
The player has 2 dice and tries to get from 1 to 6 in as few rolls as possible.

## The Details
A player needs two Angry Dice. Player rolls the dice, looking to complete
Stage 1, then Stage 2, then Stage 3.

### Stage 1
One die showing 1 pip, another showing 2 pips.

### Stage 2
One die showing the Angry face (which represents a 3), another showing 4 pips.

### Stage 3
One die showing 5 pips, another showing 6 pips.

A player does not have to perfectly roll each Stage; if a die shows one face in a
set, that die is locked (left the same) and the player now rolls the other die
to complete the set.

## The Anger
If the dice ever show both Angry Faces, the player must START OVER from **Stage 1**.



# 15 Exercise: Return of Change Return!

_Note: This is the same exercise we did in Python only now we’re implementing it in JavaScript!_

## Objective

Some supermarkets have automatic change dispensers. Let’s write code that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.

1. Fork [this pen](http://codepen.io/segdeha/pen/LZNvMV) & name it “Change Return”
1. Implement a simple program that satisfies the following requirements:
    * Ask for the amount of change to dispense _in cents._ Assume that number will be less than or 100.
    * Calculate the number of quarters necessary first.
    * Then calculate the number of dimes, nickels, and pennies. If you do it in that order, you will minimize the number of coins.

**Hint:** This is easiest done by updating a _running total_ of number of cents left to be put into coins.

_Note: The `//` operator in JavaScript does not do what it does in Python, so you’ll need to find another way, e.g., using the `Math.floor` method._

------

## Extra Credit

* Instead of assuming your “cash register” has an unlimited number of coins of each type, randomly generate how many of each type of coin you have to work with before computing the change to give and adjust what coins you return based on what’s available; experiment with how many to generate, but start with 0 to 9 of each type

------

Sources:

1. [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) on Mozilla Developer Network


# 16 Lab: Build a Weather Station

Create a webapp using the open weather map api that can:

1. Tell me the weather in my location by zip or city name.

1.  Change the background image depending on current conditions.

1. Tell me the current temperature in Celsius or Fahrenheit.

Advanced:
1. Use [getCurrentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) to get my current location automatically.

# 17 Exercise: Is it a vowel?

## Objective

Get familiar with basic JavaScript constructs by writing a program that prompts the user for a character and tells them whether or not it’s a vowel.

1. Create a new file called `vowels.html` based on [this template](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/2.%20HTML%20%26%20CSS/solutions/structure-with-inline-css-and-javascript.html?token=AAAQ0sNxHlhyXhaAZLGeWybrKtZIAd68ks5XZzmgwA%3D%3D)
1. Add your JavaScript inside the `<script></script>` tag
1. To run your program, you will need to load `vowels.html` in a web browser

------

## Helpful hints

#### prompt

Use the built-in function `prompt` to ask the user for input. The result of `prompt` should be assigned to a variable.

Example:

    var input = prompt('Enter a character');

#### alert

Use the built-in function `alert` to tell the user the result.

Example:

    alert('The character you entered is a vowel');

#### indexOf

Similar to the `index` method on Python lists, JavaScript arrays have a method called [indexOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf) that returns the array index of the value or `-1` if the value is not present.

Example:

    ['a'].indexOf('a') // 0
    ['a'].indexOf('b') // -1

You could use the `indexOf` method to detect whether the user’s input is one of the items in an array of vowels.

------

## Extra Credit

- Handle upper and lower case input
- Handle the case of `y`
- Handle common accented characters (consider using the [charCodeAt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt) method and this [reference of character codes](https://en.wikipedia.org/wiki/ISO/IEC_8859-1#Codepage_layout))
- Write your program in such a way that the user will continue to be prompted until they enter an empty string

# 18 Capstone Requirements

A satisfactory capstone **demonstrates personal understanding** of all of the topics in the course, incorporated into a _cohesive_ single web app:

* Python language basics
* Use of Django templating and views
* Design of Django routes
* Incorporating user input to and from views
* Isolated Python logic layer
* Django models for persistent storage
* Proper Python application and repo packaging
* Semantic HTML structure
* CSS style
* JavaScript language basics
* jQuery DOM manipulation and event handling
* Code structuring techniques throughout
* Documentation via relevant comments, docstrings, and a readme.
* Proper language style throughout
* Maintain a living proposal document

_Merely using_ a topic does not automatically constitute "understanding";
the use must contribute to the project meaningfully, be produced by you personally, show why the topic is useful, and demonstrate its usage via the methods taught in this class.

Your goal is to demonstrate to me that you understand and can use the skills taught in the class.
If I look at your provided code and can't see that, then that does not constitute a satisfactory capstone.

Code based upon external sources (StackOverflow, blog post snippets, etc.) is not exempt from all of the above
requirements (e.g. code structuring techniques and proper style).

You are encouraged to go beyond "understanding" towards **mastery** in areas of your interest.
Commitment and striving for mastery in a topic area is appreciated by prospective employers.
# Nested Obect Function Using Python

## Problem Statement
Having a Nested Object - Get function where we can pass in the object and a key and get back the value. 

## Solution
This function takes two arguments: the nested dictionary to search, and the key to retrieve the value for. It first splits the key into parts using the separator character (/). It then traverses the dictionary using the key parts, checking if each part exists as a key in the current dictionary. If a key is found, the function updates the current dictionary to the value of that key. If a key is not found, the function returns None

Once the function has traversed all the key parts, it returns the value at the final key. 

### Requirements to Run the Code 
1. Insatll Python
2. No Liberay Decpendecny 
3. To run use Command 'Python3 NestedObj.py'

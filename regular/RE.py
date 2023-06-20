##Access numeric in stirng
import re

text = "Hello 123456789!"
pattern = r"\d+"  # Matches one or more digits

matches = re.findall(pattern, text)
print(matches)

####extrating email
import re

text = "Contact us at info@example.com or support@example.com"
pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"  # Matches email addresses

matches = re.findall(pattern, text)
print(matches)
##
####changing the string
import re

text = "Hello, world! How are you?"
pattern = r"world"
replacement = "Python"

new_text = re.sub(pattern, replacement, text)
print(new_text)
##
##
####Access the alphabetic words
import re

text = "Hello 123 World 456"
pattern = r"[A-Za-z]+"  # Matches one or more alphabetic characters

matches = re.findall(pattern, text)
print(matches)



import re

text = "Hello, world! How are you?"
pattern = r"\w+"  

matches = re.findall(pattern, text)
print(matches)  
##
##
import re

text = "Hello, world! How are you?"
pattern = r"[aeiou]+"  

matches = re.findall(pattern, text)
print(matches)


import re

text = "Hello, World!"

# Using re.match()
pattern = r"Hello"
match = re.match(pattern, text)
if match:
    print("Match found with re.match():", match.group())
else:
    print("No match found with re.match()")

# Using re.search()
pattern = r"World"
match = re.search(pattern, text)
if match:
    print("Match found with re.search():", match.group())
else:
    print("No match found with re.search()")


##using (.)
import re
text = "cat, mat, hat"
pattern = r"c.t"  # Matches 'cat', 'cot', 'cut', etc.
matches = re.findall(pattern, text)
print(matches)

##using(*)
import re
text = "abcde abbbcde abbbbbcde"
pattern = r"a*bcde"  # Matches 'abcde', 'abbbcde', 'abbbbbcde', etc.
matches = re.findall(pattern, text)
print(matches)  # Output: ['abcde', 'abbbcde', 'abbbbbcde']

##using spilt
##For example:
import re
text = "apple,banana,orange,grape"
pattern = r","  # Matches a comma
substrings = re.split(pattern, text)
print(substrings) 

import re
text = "apple,banana orange grape"
pattern = r"[,\s]"  # Matches a comma or whitespace
substrings = re.split(pattern, text)
print(substrings)

                                                                     







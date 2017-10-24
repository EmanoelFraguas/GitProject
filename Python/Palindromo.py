"""
Author: Scott C Gramig
Program: Palindrome
"""

print "-------- Palindrome --------"

word = raw_input("Enter a word to check: ")

if word == word[::-1]:
	print "%s is a palindrome!" % word
else:
	print "%s is not a palindrome!" % word
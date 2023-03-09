# Python Code Challenge #3: Sort a String
from collections import deque

def sort_string(text):
  text = input()
  text = text.replace(' ', '')
  text = deque(text)
  print(text)

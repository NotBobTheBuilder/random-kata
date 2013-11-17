import string

def isPangram(sentence):
  return all(i in sentence.lower() for i in list(string.lowercase))

def isPalindrome(word):
  return len(word) == 0 or (word[-1] == word[:1]) and isPalindrome(word[1:-1])

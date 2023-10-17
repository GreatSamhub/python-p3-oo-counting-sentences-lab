#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) != str:
      print("The value must be a string.")
    self._value = value
  value = property(get_value, set_value)

  def is_sentence(self):
        return self._value.endswith('.')

  def is_question(self):
      return self._value.endswith('?')

  def is_exclamation(self):
      return self._value.endswith('!')

  def count_sentences(self):
        # Split the string into sentences based on '.', '?', and '!'
      sentences = self._value.split('.') or self._value.split('?') or self._value.split('!')
        
        # Filter out empty strings (resulting from consecutive punctuation marks)
      for sentence in sentences:
        if sentence == '':
          sentences.remove(sentence)
      return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
sentence_count = string.count_sentences()
print(sentence_count)

      
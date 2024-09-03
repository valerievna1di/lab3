# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 00:38:24 2024

@author: Диана
"""

# Запит речення у користувача
sentence = input("Введіть речення: ")

# Перетворення кожного символу в його ASCII код
ascii_sentence = ' '.join(str(ord(char)) for char in sentence)

# Виведення результату
print("Речення у вигляді ASCII кодів:")
print(ascii_sentence)

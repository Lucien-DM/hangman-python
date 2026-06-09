#!/usr/bin/env python3
import random
import logger as log
FILE_WORDS = "words.txt"
ENCODING = 'utf-8'

def does_file_exist(file):
    """Checks if file exists, and if you have permission to read it"""
    try:
        with open(file, 'r'):
            pass
    except FileNotFoundError:
        log.error(f'"{file}": File Not Found!')
        return False
    except PermissionError:
        log.error(f'"{file}": No Permission to Read File!')
        return False
    else:
        return True

def import_words(path):
    """Imports Works from file"""
    with open(path, 'r', encoding=ENCODING) as f:
        x = 0
        words = []
        for line in f:
            word = [x, line.read()]
            words.append(word)
            x += 1
        return words

def letter_in_word(word, letter):
    if letter in word:
        

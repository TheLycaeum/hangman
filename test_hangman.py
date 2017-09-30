import os

import pytest

import hangman

def test_choose_word():
    # First create a dummy file
    f = open("/tmp/fake_dict.txt", "w")
    for i in ["cat", "dog", "bull", "elephant", "mouse",  "chimpanzee"]:
        f.write(i+"\n")
    f.close()

    selected_word = hangman.choose_word("/tmp/fake_dict.txt")
    os.unlink("/tmp/fake_dict.txt")

    assert selected_word in ["elephant", "chimpanzee"]

def test_choose_word_no_valid_words():
    # First create a dummy file
    f = open("/tmp/fake_dict.txt", "w")
    for i in ["cat", "dog", "bull", "mouse", "personage's", "Barclays"]:
        f.write(i+"\n")
    f.close()

    with pytest.raises(ValueError):
        selected_word = hangman.choose_word("/tmp/fake_dict.txt")

    os.unlink("/tmp/fake_dict.txt")

    
    

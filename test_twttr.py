# put this file in the same folder as twttr.py, name folder twtrr
# run a test with terminal command    pytest test_twttr.py

from twttr import shorten

def test_vowels_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

def test_vowels_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("HeLLo") == "HLL"
    assert shorten("AeIoU") == ""

def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg"
    assert shorten("rhythm") == "rhythm"

def test_numbers_and_punctuation():
    assert shorten("123") == "123"
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("AEIOU, aeiou.") == ", ."

def test_empty_string():
    assert shorten("") == ""

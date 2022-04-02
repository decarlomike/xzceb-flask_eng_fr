import unittest
from translator import english_to_french, french_to_english, init_translator
#initialize Watson translator connection
translator_instance = init_translator()
class TestEnglishToFrench(unittest.TestCase):
   def test1(self):
       self.assertEqual(english_to_french("hello",translator_instance), "Bonjour")
       self.assertEqual(english_to_french("",translator_instance), "Invalid Text")
class TestFrenchToEnglish(unittest.TestCase):
   def test1(self):
      self.assertEqual(french_to_english("Bonjour",translator_instance), "Hello")
      self.assertEqual(french_to_english("", translator_instance), "Invalid Text")
unittest.main()
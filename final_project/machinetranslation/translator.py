import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def init_translator():
    #initialize connection to IBM Translator Service
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
         version='2018-05-01',
         authenticator=authenticator
        )
    language_translator.set_service_url(url)
    return language_translator

def english_to_french (english_text, language_translator):
    #Translate English to French, check for null string
    english_translate_text = english_text
    if len(english_translate_text):
        translation = language_translator.translate(
        text=english_translate_text,
        model_id='en-fr').get_result()
        french_text = translation["translations"][0]["translation"]
    else:
        french_text = "Invalid Text"
    return french_text

def french_to_english (french_text, language_translator):
   #Translate French to English, check for null string
    french_translate_text = french_text
    if len(french_translate_text):
        translation = language_translator.translate(
        text=french_translate_text,
        model_id='fr-en').get_result()
        english_text = translation["translations"][0]["translation"]
    else:
        english_text = "Invalid Text"
    return english_text

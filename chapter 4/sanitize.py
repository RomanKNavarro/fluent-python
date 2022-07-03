import unicodedata
import string


def shave_marks(txt):
   '''Remove all diacritic marks'''
   norm_txt = unicodedata.normalize('NFD', txt)                # txt is decomposed with NFD so that composed characters are expanded into base characters
   shaved = ''.join(c for c in norm_txt                        # remove all non-combined characters from string 
                    if not unicodedata.combining(c))
    
   print(unicodedata.normalize('NFC', shaved))                 # The text was decomposed, so recompose it with NFC   
   
         
shave_marks('São Paulo ß')
 

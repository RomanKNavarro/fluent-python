import unicodedata
import string 


def shave_marks_latin(txt):
   '''Remove all diacritic marks from Latin base characters'''
   norm_txt = unicodedata.normalize('NFD', txt)                            # any composed characters are decomposed to base characters and diacritics.
   latin_base = True
   keepers = []
   for c in norm_txt:
      if unicodedata.combining(c) and latin_base:                          # ignore combining marks if base character is latin 
         continue
      keepers.append(c)                                                    
      # If it isn't combining char, it's a new base char
      if not unicodedata.combining(c):                                     # if the character is not a combining mark (from non-latin character)
         latin_base = c in string.ascii_letters                             
   shaved = ''.join(keepers)
   print(unicodedata.normalize('NFC', shaved)) 
                                
shave_marks_latin('εβδομάδα São Paulo') 
   

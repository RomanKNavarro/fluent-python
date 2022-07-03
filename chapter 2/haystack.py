import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'                               # The format to print the number (0), position(1), and vertical lines (2)

def demo(bisect_fn):
   for needle in reversed(NEEDLES):                                     # The demo function uses bisect_fn (bisect.bisect) to get the position available  
      position = bisect_fn(HAYSTACK, needle)                            # for the current needle. The position number determines the amount of | to print. 
      offset = position * '  |'                                         # All the variables are then inserted into the format to be printed
      print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':                                               

   if sys.argv[-1] == 'left':
      bisect_fn = bisect.bisect_left
   else:
      bisect_fn = bisect.bisect

   print('DEMO:', bisect_fn.__name__)
   print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
   demo(bisect_fn)                                                      # when the module (source file) is run as the main program, "__main__" is assigned
                                                                        # to __name__. When the module (e.g haystack.py) is imported by another module,
                                                                        # the value of __name__ changes to "haystack"


   
 

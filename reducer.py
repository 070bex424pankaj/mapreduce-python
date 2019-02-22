#!/usr/bin/env python
 
import sys, errno
 
last_key = None
running_total = 0
dict = {}
 
for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key= input_line.split(";")
   key, value = this_key
   try:
       value = float(value)
   except Exception:
       pass
    #print(value)
   try:
       if last_key == key:
           running_total += value
       else:
           if last_key:
               print("{} {}".format(last_key, running_total) )
           running_total = value
           last_key = key
        #print(last_key) 
   except Exception:
       pass
'''if last_key == key:
   print("{} {}".format(last_key, running_total) )'''
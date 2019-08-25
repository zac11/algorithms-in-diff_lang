'''
Easiest way I can find
'''
import re

test_string="Ge;ek *4 s:fo ! 7r;Ge * 4e*k:s !"
clean_string = "".join(e for e in test_string if e.isalnum())
print(clean_string)


"""
This is also good - fails for underscore
"""
cleanstring = re.sub('\W','',test_string)
print(cleanstring)
#!/usr/bin/python

import re
#within a radius of 1 kilometre from the premises in paragraph 4
startend = r'.+Places of worship within a radius of 1 kilometre from the premises in paragraph 4.'
footer = "\n.6\n\nNo. 105\n\nPROVINCIAL GAZETTE EXTRAORDINARY, 24 APRIL 2013\n\n"

with open ("testy.txt", "r") as myfile:
    data=myfile.read()
    data2 = re.sub(startend, '', data, flags=re.DOTALL+re.MULTILINE)
    data3 = re.sub(footer, '', data2, count=0, flags=re.DOTALL+re.MULTILINE)
    print(data3)

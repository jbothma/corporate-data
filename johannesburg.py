#!/usr/bin/python

import re
#within a radius of 1 kilometre from the premises in paragraph 4
startend = r'.+Places of worship within a radius of 1 kilometre from the premises in paragraph 4.'
footereng = "\n.\d+\n\nNo. \d+\n\nPROVINCIAL GAZETTE EXTRAORDINARY, \w+ \w+ \w+\n\n"
footerafr = "\n\n.BUITENGEWONE PROVINSIALE KOERANT, \w+ \w+ \w+\n\nNo. \d+\n\n\d+\n\n"
tail = "Printed by the Government Printer, Bosman Street.+"

with open ("../pdftotext/105_24-4-2013_GautengLiquor.txt", "r") as myfile:
    data=myfile.read()
    data2 = re.sub(startend, '', data, flags=re.DOTALL)
    data3 = re.sub(footereng, '', data2, count=0, flags=re.DOTALL)
    data4 = re.sub(footerafr, '', data3, count=0, flags=re.DOTALL)
    data5 = re.sub(tail, '', data4, count=0, flags=re.DOTALL)
    print(data5)

#!/usr/bin/python

import re
import json

def parse(item):
    notice = {}
    parts = re.split("(\(\d\))\s*", item)
    parts.reverse()
    notice['applicant_name'] = parts.pop()
    while len(parts) > 0:
        part = parts.pop()
        if part == "(2)":
            notice['trading_name'] = parts.pop()
        elif part == "(3)":
            notice['identity_number'] = parts.pop()
        elif part == "(4)":
            notice['premises_location'] = parts.pop()
        elif part == "(5)":
            notice['license_type'] = parts.pop()
        elif part == "(6)":
            notice['nearby_educational'] = parts.pop()
        elif part == "(7)":
            notice['nearby_liquor'] = parts.pop()
        elif part == "(8)":
            notice['nearby_religious'] = parts.pop()
    return notice

startend = r'.+Places of worship within a radius of 1 kilometre from the premises in paragraph 4.'
footereng = "\n.\d+\n\nNo. \d+\n\nPROVINCIAL GAZETTE EXTRAORDINARY, \w+ \w+ \w+\n\n"
footerafr = "\n\n.BUITENGEWONE PROVINSIALE KOERANT, \w+ \w+ \w+\n\nNo. \d+\n\n\d+\n\n"
tail = "Printed by the Government Printer, Bosman Street.+"
split = "([A-Z ʼ]+\n)?[A-Z/ 0-9.-]+$\n^(\(1\))\s*"

#with open ("../testy.txt", "r") as myfile:

notices = []

with open ("../pdftotext/105_24-4-2013_GautengLiquor.txt", "r") as myfile:
    data=myfile.read()
    # Clean
    data2 = re.sub(startend, '', data, flags=re.DOTALL)
    data3 = re.sub(footereng, '', data2, count=0, flags=re.DOTALL)
    data4 = re.sub(footerafr, '', data3, count=0, flags=re.DOTALL)
    data5 = re.sub(tail, '', data4, count=0, flags=re.DOTALL)
    # Split
    data6 = re.split(split, data5, flags=re.DOTALL+re.MULTILINE)
    data6.reverse()
    while len(data6) > 0:
        item = data6.pop()
        if item == "(1)":
            item2 = data6.pop()
            notices.append(parse(item2))

print(json.dumps(notices))

#!/usr/bin/python

import json
import sys
import colorama
from colorama import Fore,Style

with open(sys.argv[1], "r") as f:
	data = json.load(f)
print ("----------------------------------------------------")

print(f"Total Hash Count : {len(data)}")
print ( "Showing Suspicious and Malicious Entries Only")
print ("----------------------------------------------------")

for x in data:
	if all(s not in x['rating'] for s in ('unknown', 'clean')):
		if 'malicious' in x['rating']:	
			print(
				Fore.RED
				+ f"{x['hash']} has been detected by {x['result']} AVs and rated as {x['rating']}, Possible Filenames include {x['filenames']}."
			)

			print(Style.RESET_ALL, end='')
		else:
			print(
				f"{x['hash']} has been detected by {x['result']} AVs and rated as {x['rating']}."
			)




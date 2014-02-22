import sys
import re

errorStrings = sys.argv
	
print "Before parsing"
for j in errorStrings:
	print j

#Add a bunch of 'junk patterns' here in which we will need to remove
pattern1  = re.compile (".+\..+") #This pattern should match file names

print "After Parsing"
for i in range(len(sys.argv)):
	if re.match(pattern1,errorStrings[i]):
		errorStrings[i] = ""

for j in errorStrings:
	print j
# ======================================================
# Prerequisite:
# Have text file InputFile.txt in cwd, 
# containing odd and even numbers,
# each on separate line
# ======================================================
#

with open("InputFile.txt") as f:
	odds = []
	evens = []
	for num in f:
		num = int(num)
		if num % 2: # if there is remainder, num is odd
			odds.append(num)
		else: # else it must be even
			evens.append(num)


print("All even numbers: {}".format(evens))
print("All odd numbers: {}".format(odds))
#
print("")
#
print("Total number of even numbers: {}".format(len(evens))) #length will be total evens
print("Total number of odd numbers: {}".format(len(odds)))

# Close the file
f.close()

#====================================================
# Description:
# Script searches for all files in a given category
# matching given pattern
#
# Author: Tomas Nemeth
#====================================================
#
# Import Python modules
#
import os
import fnmatch
import sys
#
print('========================================')
print('Search all files matching given pattern ')
print('========================================')
print('')
rootpath = '/Users/tomasnemeth'
pattern = raw_input('>>> Insert file pattern: ')
#
# Search for files in directory and add the selection into list
#
List = []
for root, dors, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        List.append(os.path.join(root, filename))
#
print('')
print('=====================================')
print('List of files matching the criteria')
print('=====================================')
print('')
#
# Print files matching the criteria one by one
#
count = 0
for item in List:
    print(item)
    count += 1
print('')
print(str(count) +' files retrieved')
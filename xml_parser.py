##==============================================================================
## Description:
## Search for XML files in defined
## directory and matching pattern, then prints results into .csv file
##
## Author: Tomas Nemeth
##
## Requirements
## A CSV file containing the following columns should be generated: UID, TITLE,
## ACTOR, DIRECTOR, COUNTRY, FILEPATH (Should be a merge of 
## PATH, UID and FORMAT), BITRATE, FRAMES_PER_SHIFT,
## ASPECT_RATIO;
##
## Check also:
## http://stackoverflow.com/questions/15990530/os-walk-to-find-path-to-file-issue-python-2-7
## http://www.tutorialspoint.com/python/python_xml_processing.htm
## http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
##===============================================================================
##
# Import Python modules
#
import os
import fnmatch
import sys
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.dom.minidom import parse
#
# Define rootpath and pattern
#
#rootpath = raw_input('Insert root path: ')
#pattern = raw_input('Insert file pattern: ')
#
rootpath = '/Users/tomasnemeth/Documents/002 Python/XML_Test_Data'
pattern = 'data-*'
#
# Sample rootpath:
# /Users/tomasnemeth/Documents/002 Python/XML_Test/ScriptTest
#
# Sample pattern:
# data*
#
#
# Search for files in directory and add the selection into list
#
List = []
for root, dors, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        List.append(os.path.join(root, filename))
##print(List)
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
#
print('')
print('=====================================')
print('System now extracts data from XML files above into .CSV file')
print('=====================================')
##
## Get current Time
curr_time = str(datetime.datetime.now())
##
## Open a file - file gets created in CWD
outfile = "XML-Output-"+curr_time+".CSV"
fo = open(outfile, "a")
#
# Write field names
fo.write('UID;TITLE;ACTOR;DIRECTOR;COUNTRY;FORMAT;BITRATE;FPS;ASPECT RATIO;PATH'+'\n')
#
for item in List:
    ## Set Variables for XML parsing
    tree = ET.parse(item)
    root = tree.getroot()
    xmldoc = minidom.parse(item)
    product = xmldoc.documentElement
    ##    
    ## Set Node variables   
    node = xmldoc.firstChild
    assetnode = node.childNodes[9]
    ##
    ##
    if product.hasAttribute('uid'):
        uid = product.getAttribute('uid')
    ##    print("UID : %s" % uid)
    ##
    ## Get title
    title = root[0].text
    ##print ('Title : %s' % title)
    ##
    ## Get actor
    actor = root[1].text
    ##print ('Actor : %s' % actor)
    ##
    ## Get director
    director = root[2].text
    ##print ('Director : %s' % director)
    ##
    ## Get country
    country = root[3].text
    ##print ('Country : %s' % country)
    ##
    ## Get elements inside ASSET node
    ##
    ## Get Format
    format_raw = assetnode.childNodes[1]
    format = format_raw.firstChild.data
    ##print ('Format : %s' % format)
    ##
    ## Get Bitrate
    bitrate_raw = assetnode.childNodes[3]
    bitrate = bitrate_raw.firstChild.data
    ##print ('Bitrate : %s' % bitrate) 
    ##
    ## Get fps
    fps_raw = assetnode.childNodes[5]
    fps = fps_raw.firstChild.data
    ##print ('FPS : %s' % fps)
    ##    
    ## Get Aspect ratio
    aspect_r_raw = assetnode.childNodes[7]
    aspect_r = aspect_r_raw.firstChild.data
    ##print ('Aspect ratio : %s' % aspect_r)
    ##
    ## Path = merge of Filepath + uid + format
    filepath = item
    #
    # Define extract + ignore ascii encoding
    line_extr = (uid + ';' + title + ';' + actor + ';' + director + ';' + country + ';' + format + ';' + bitrate + ';' + fps + ';' + aspect_r+ ';' + filepath + '-' + uid + '-' + format).encode('ascii', 'ignore').decode('ascii')
    ##
    ## Write output with line end character
    fo.write(line_extr + '\n')
    ##
fo.close()
print('')
print('*** Data extracted successfully! ***')
print('*** Check results in: '+ outfile + ' ***')

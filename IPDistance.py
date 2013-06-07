###############################################################################
#                                                                             #
#                            I P   D i s t a n c e                            #
#                                                                             #
###############################################################################

"""
Class find distance in real world between two IP addresses. 

Script take two arguments, two IP addresses.
Find the city and country of each IP address using geody.com's service.
Look up the city in pre existing table for long and lat coordinates.
Calculate the distance between coordinates.

If city is not already in the table, use google's service to find long and lat.

"""

import re
import sys
import urllib2
import BeautifulSoup
 
usage = "Run the script: ./IP_Distance.py IPAddress1 IPAddress2 "

def get_geody(IP):
    # Fetch location data from geody
    geody = "http://www.geody.com/geoip.php?ip=" + IP
    html_page = urllib2.urlopen(geody).read()
    soup = BeautifulSoup.BeautifulSoup(html_page)
    return soup('p')[3]

def get_countries():
    # Get a list of all countries from file.
    # Is used for comparison later. File written in ISO standard
    countries = []
    lines = open("countries.txt", 'r').readlines()
    for line in lines:
        countries.append(line.strip().split('\t',1))
    return countries

def city_country(data, countries):
    # Seperate city and country into two str's
    # Strip all else and return
    geo_txt = re.sub(r'<.*?>', '', str(data))
    geo_txt = geo_txt[32:].upper().strip()
    stripped_data = geo_txt.strip("IP: ").partition(': ')
    city_country = stripped_data[2]
    for i, key in enumerate(countries):
        if  normalize_whitespace(countries[i][1]) in normalize_whitespace(city_country):
            print haystack[i][1]
            break

def normalize_whitespace(str):
    # Strip leading and trailing whitespace.
    # Make all remaining whitespace (tabs, etc) to spaces.
    # import re
    return re.sub(r'\s+', ' ', str.strip())

# Script starts
if len(sys.argv)!=3:
    print(usage)
    sys.exit(0)
else:
    IP1 = sys.argv[1]
    IP2 = sys.argv[2]

raw_data1 = get_geody(IP1)
raw_data2 = get_geody(IP2)
countries = list(get_countries())
city1, country1 = city_country(raw_data1, countries)
city2, country2 = city_country(raw_data2, countries)
print(city1 + ", " + country1 + " | " + city2 + "' " + country2)

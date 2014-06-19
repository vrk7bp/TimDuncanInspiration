import urllib2
import json
from random import randint

#List that will hold all of the links to the pictures
listOfLinks = []

#Since Google only lets me search in groups of 10, I must query 10 times to get 100 images
firstTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image").read())
secondTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=11").read())
thirdTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=21").read())
fourthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=31").read())
fifthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=41").read())
sixthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=51").read())
seventhTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=61").read())
eighthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=71").read())
ninthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=81").read())
tenthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=AIzaSyAHsYO-8aVmXF2lT5BzLdlKb7U_QynnBjg&cx=007217991029971963183:gi2ooudfslu&searchType=image&start=91").read())

#Put all of the image URLs into one list
for element in firstTen["items"]:
	listOfLinks.append(element["link"])

for element in secondTen["items"]:
	listOfLinks.append(element["link"])

for element in thirdTen["items"]:
	listOfLinks.append(element["link"])

for element in fourthTen["items"]:
	listOfLinks.append(element["link"])

for element in fifthTen["items"]:
	listOfLinks.append(element["link"])

for element in sixthTen["items"]:
	listOfLinks.append(element["link"])

for element in seventhTen["items"]:
	listOfLinks.append(element["link"])

for element in eighthTen["items"]:
	listOfLinks.append(element["link"])

for element in ninthTen["items"]:
	listOfLinks.append(element["link"])

for element in tenthTen["items"]:
	listOfLinks.append(element["link"])


# print listOfLinks
# print

# print len(listOfLinks)
# print

# print listOfLinks[0]
# print
# print listOfLinks[99]
# print

randomInt = randint(0,99)
imageOfTheDay = listOfLinks[randomInt]
# print randomInt
# print
# print listOfLinks[randomInt]
# print
# print "done"




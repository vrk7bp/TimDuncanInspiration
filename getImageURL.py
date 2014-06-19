import urllib2
import json
from random import randint
import xml.parsers.expat
import sendgrid

########### Function to get rid of XML content coming from Quote API
def unescape(s):
    want_unicode = False
    if isinstance(s, unicode):
        s = s.encode("utf-8")
        want_unicode = True

    # the rest of this assumes that `s` is UTF-8
    list = []

    # create and initialize a parser object
    p = xml.parsers.expat.ParserCreate("utf-8")
    p.buffer_text = True
    p.returns_unicode = want_unicode
    p.CharacterDataHandler = list.append

    # parse the data wrapped in a dummy element
    # (needed so the "document" is well-formed)
    p.Parse("<e>", 0)
    p.Parse(s, 0)
    p.Parse("</e>", 1)

    # join the extracted strings and return
    es = ""
    if want_unicode:
        es = u""
    return es.join(list)

############## End XML Function ########################3



############# GOOGLE CUSTOM SEARCH PART: FOR IMAGE RETRIEVAL ######################

#List that will hold all of the links to the pictures
listOfLinks = []

#Since Google only lets me search in groups of 10, I must query 10 times to get 100 images
firstTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image").read())
secondTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=11").read())
thirdTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=21").read())
fourthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=31").read())
fifthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=41").read())
sixthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=51").read())
seventhTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=61").read())
eighthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=71").read())
ninthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=81").read())
tenthTen = json.loads(urllib2.urlopen("https://www.googleapis.com/customsearch/v1?q=tim+duncan&key=zzz&cx=yyy&searchType=image&start=91").read())

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

randomInt = randint(0,99)
imageOfTheDay = listOfLinks[randomInt]

############# END IMAGE RETRIEVAL ######################

############# I HEART QUOTES: FOR QUOTE RETRIEVAL ######################

quote = urllib2.urlopen("http://www.iheartquotes.com/api/v1/random").read()
quote.replace("&quot;", "\"")
linedQuote = quote.split('\n')
linedQuote.pop()
del linedQuote[-1]
edittedQuote = ""
for element in linedQuote:
	edittedQuote = edittedQuote + element + "\n"
finalQuote = unescape(edittedQuote)

############# END QUOTE API ######################

############# SEND GRID API: FOR SENDING THE EMAILS ######################

sg = sendgrid.SendGridClient('xxx', 'yyy')
message = sendgrid.Mail()
message.add_bcc(['zzz <zzz@zzz>', 'zzz <zzz@zzz>'])
message.set_subject('Your Tim Duncan Inspiration for the Day')
message.set_html('<html><body><img src=\"' + imageOfTheDay + '\" alt=\"Tim Duncan doing cool stuff\"><p></p><p></p><bold>' + finalQuote + '</bold></body></html>')
message.set_from('Tim Duncan <tim@duncan.com>')
status, msg = sg.send(message)

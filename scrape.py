from urllib.request import urlopen
import bs4
'''
web scraping negative words
'''
handle = open("words.txt",'w')
def parseSite(website):
    myList = []
    req = urlopen(website)
    sauce = req.read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")
    container = soup.find_all('p')

    for objects in container:
        for sentence in objects:
            myStr = ""
            if '\n' in sentence:
                sentence = str(sentence).split()
                if len(sentence) == 1 and sentence[0] != "":
                    myStr = sentence[0]
                    print(myStr.lower())
                    #myList.append(myStr.lower())

    return myList


list1 = parseSite("http://eqi.org/fw_neg.htm")
list2 = parseSite("http://eqi.org/cnfs.htm")
#list3 = parseSite("http://dreference.blogspot.com/2010/05/negative-ve-words-adjectives-list-for.html")
#finalList = list(set(list1 + list2))
#finalList.sort()

#for words in finalList:
    #handle.write(words + "\n")

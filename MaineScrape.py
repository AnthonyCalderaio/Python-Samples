import requests
import urllib.request as ur
import re

from bs4 import BeautifulSoup

def main():
    #Base Url For Parsing Bids
    bidBaseUrl = 'https://asp.portlandmaine.gov/purchasing/'

    #Parse main page
    html_doc = requests.get('https://www.portlandmaine.gov/1034/BidsRFP-Search')
    doc = html_doc.content
    soup = BeautifulSoup(doc,'lxml')

    #Find the iframe in the soup
    iframexx = soup.find_all('iframe')

    #Get the src CLEAN LINK from the iframe in the form of an array element
    bids_url = re.findall('src="([^"]+)"', str(iframexx))

    #Turn that link into a string
    bids_url_str = bids_url[0]

    #Start parsing the iframe link
    bids_doc = requests.get(bids_url_str)
    bids_content = bids_doc.content
    bids_soup = BeautifulSoup(bids_content,'lxml')
    #print(bids_soup)
    #print(bidNums)

    #List of source Urls to parse for data YAY
    bid_url_with_nums = []
    for a in bids_soup.find_all('a', href=True):
        ##Testing Purposes
        #print("Found the URL:", a['href'])
        ##Testing Purposes
        word = str(a)
        if 'mailto' in word:
            continue
        else:
            bid_url_with_nums.append(a['href'])
    #print(bid_url_with_nums)
   
    ###############################################################
    #Level 2
    ###############################################################

    #For testing reasons
    #practiceAddress = bidBaseUrl+bid_url_with_nums[2]
    #For testing reasons

    bid_index = 0
    for bid in bid_url_with_nums:
        print("______________Begining____________")
        practiceAddress = bidBaseUrl+bid
        ##Begin parsing
        parse_doc = requests.get(practiceAddress)
        parse_content = parse_doc.content
        parse_soup = BeautifulSoup(parse_content,'lxml')
        #print(parse_soup)
        #print(practiceAddress)
        bidNumber = practiceAddress[-5:]

        #Begin Date Extraction
        pollutedDateUrl = parse_soup.find_all('td')
        pollutedDateUrlTest = str(pollutedDateUrl)
        re.findall('', pollutedDateUrlTest)

        #Testing purposes
        #aExtract = soup.find_all('a',href=True)
        #Testing purposes

        seq = ['Bid Num',
                    'Description',
                    'Open Date',
                    'Open Time', 
                    'Notice Type',
                    'Legal Desc', 
                    'Pre-Bid Conf',
                    'Conf Desc:',
                    'Plan Charges',
                    'Charge Amount',
                    'Engineer',
                    'Est. Cost',
                    'Bid Agenda' ]
        

        bidInfoList = { }
        
        bid_form_size = 13

        indexNum = 0
        for hit in parse_soup.findAll(attrs={'align' : 'left'}):
            if (indexNum != bid_form_size):
                #Hit is the value we care about
                hit = hit.text.strip()

                #Here we are adding the key's value
                bidInfoList[seq[indexNum]] = hit
                indexNum = indexNum+1

            #print(practiceAddress)

        #print(bidInfoList)
        ###################
        indexNum2 = 0
        for bid in bidInfoList:
            if (indexNum2 != bid_form_size):
                print(bid + ':' + bidInfoList[seq[indexNum2]])
                indexNum2 = indexNum2 + 1
            else:
                indexNum2 = indexNum2 + 1

        ###################        
           
        #print(bidInfoList)
        print('______________End____________')

        #For Testing Purposes
        #indexNum = 0
        #for hit in parse_soup.findAll(attrs={'align' : 'left'}):
            #print(hit.text.strip())
        #print(attrList2)
        #For Testing Purposes

main()

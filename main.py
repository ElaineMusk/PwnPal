import requests
from bs4 import BeautifulSoup


# source code of main domain page organized by HTML tags<>
def CreateSoup(URL: str):
    Soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
    return Soup


# URL --> List
# This Function gathers all the links embedded in html anchor tags<a> in URL page source into a list: Links
def HrefFinder(Soup: BeautifulSoup):
    Links = []
    AnchorTags = Soup.find_all('a')
    for i in AnchorTags:
        if i.has_attr('href'):
            Links.append(i['href'])
    return Links


# List --> List
# This function gathers all links from list Links, and parses out only the accessible links to the requested
# domain and stores them inside list FilteredLinks, i.e. no instagram references or photo links
def CleanList(Links):
    FilteredLinks = []
    for i in Links:
        if URL == i[0:len(URL)] or URLshort == i[0:len(URLshort)]:
            FilteredLinks.append(i)
        elif "/" == i[0:1]:
            FilteredLinks.append(URL + i)
    return list(dict.fromkeys(FilteredLinks))


# List --> String(s)
# This function takes the list FilteredLinks and filters only parts of the domain that commit URL based web requests
# which can later be tested for injections
def FindQuery(FilteredLinks):
    FilteredLinks2 = []
    for str in FilteredLinks:
        for char in str:
            if char == "=":
                FilteredLinks2.append(str)
                for i in FilteredLinks2:
                    print(i)
    return list(dict.fromkeys(FilteredLinks2))


# def MakeParts(FilteredLinks2):
#     for Link in FilteredLinks2:
#         Link = Link.split('&')
#         RefinedParts = []
#         for part in Link:
#             POC = "$$$$$$$$$$$$$PPPPOOOOCCCC$$$$$$$$$$$"
#             refinedpart = part[:part.find("=") + 1] + POC
#             RefinedParts.append(refinedpart)
#         return RefinedParts, Link
#
#
# def MaliciousLinks(RefinedParts: list, Parts: list):
#     OriginalParts = Parts.copy()
#     for index, x in enumerate(RefinedParts):
#         Parts[index] = x
#         MalLink = "&".join(Parts)
#         print(MalLink)
#         Parts = OriginalParts.copy()

def MakeParts(FilteredLinks2):
    RefinedLinks = []  # Create an empty list to store the processed links
    for Link in FilteredLinks2:
        Parts = Link.split('&')
        RefinedParts = []
        for part in Parts:
            refinedpart = part[:part.find("=") + 1] + POC
            RefinedParts.append(refinedpart)
        RefinedLinks.append((RefinedParts, Parts))  # Append the processed parts and original parts to RefinedLinks
    return RefinedLinks


def MaliciousLinks(RefinedLinks):
    for RefinedParts, Parts in RefinedLinks:
        OriginalParts = Parts.copy()
        for index, x in enumerate(RefinedParts):
            Parts[index] = x
            MalLink = "&".join(Parts)
            print(MalLink)
            Parts = OriginalParts.copy()

        # for i in RefinedParts:
        #     FuckyParts = Parts
        #     x = RefinedParts.index(i)
        #     FuckyParts[x] = RefinedParts[x]
        #     MalLink = "&".join(FuckyParts)
        #     print(MalLink)
        # while total >= 0:
        #     FuckyParts = Parts
        #     MalLink = "&".join(FuckyParts)
        #     print(MalLink)
        #     total = total - 1  # Decrement the accumulator
        #     if total < 0:
        #         break


# if __name__ == "__main__":
#     main()


# for y in RefinedParts:
# MalLink = "&".join(Parts.replace(Parts[RefinedParts.index(y)], y))
# print(MalLink)


# GUN = []
# POC = "balls"
# Endings = []
# index = str.find('=')
# index2 = str.find('&')
# if index2 != -1:
#     MaliciousLink = str[:index + 1] + POC + str[index2:]
#     GUN.append(MaliciousLink)
#     Endings.append(str[index2:])
#     LoadTheChamber(str[index2:])
#
# elif index2 == -1:
#     MaliciousLink = "".join(Endings) + str[:index + 1] + POC
#     GUN.append(MaliciousLink)
# print(GUN)

#
while True:
    try:
        URL = input("Please insert a URL in the exact form of \"https://www.example.xyz\" for accurate results ")
        requests.get(URL)
        URLshort = "https://" + URL[12:len(URL)]
        POC = input("Please insert an injectable payload to be tested in the URL parameters ")
        MaliciousLinks(MakeParts(FindQuery(CleanList(HrefFinder(CreateSoup(URL))))))
    except requests.exceptions.RequestException as e:
        print("This link is unreachable for some reason, try again")
        continue
    break
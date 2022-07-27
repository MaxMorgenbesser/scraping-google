import firebase


#allows me to search google without a certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from googlesearch import search


# to search
def searchGoogle():
    query = input('Please enter what you would like to search google for:\n')
    urlList=[]
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        urlList.append(j)
    return urlList
searchGoogle()




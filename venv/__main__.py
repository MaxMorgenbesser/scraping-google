

#importing modules for firebase in python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#module required to collect data from each individual link
from requests_html import HTMLSession

#connects to firebase
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred)
db=firestore.client()
#firebase = firebase.FirebaseApplication('https://scraping-google-mm-py.firebaseio.com', None)


#allows me to search google without a certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from googlesearch import search


# function that searches google
def searchGoogle():
    query = input('Please enter what you would like to search google for:\n')
    urlList=[]
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        urlList.append(j)
    return urlList

#collectname=input("Please enter a name for the collection you would like to add. \n")
def addToFireStore(URLlist):
    #lets user add a name to a collection
    collectName=input("Please enter a name for the collection you would like to add. \n")
    #adds every item in the URL list to firestore database
    for i in URLlist:
        url=i
        #connects to html
        session = HTMLSession()
        response = session.get(url)
        #gets specific information from
        title = response.html.find('title', first=True).text
        description = response.html.xpath("//meta[@name='description']/@content")
        canonical = response.html.xpath("//link[@rel='canonical']/@href")
        author = response.html.xpath("//meta[@name='author']/@content")
        image = response.html.xpath("//meta[@property='og:image']/@content")
        db.collection(collectName).document(title).set(
                {'Title': title,
                'Author': author,
                'Description': description,
                'Image': image,
                'Canonical link': canonical
                }
            )


#list=['https://medium.com/theleanprogrammer/connecting-firebase-6102ef4eca08','https://nadinbrzezinski.medium.com/logistics-collapse-945984f5d48e']
#addToFireStore(list)
#searchGoogle()

def main():
    urlArr=searchGoogle()
    addToFireStore(urlArr)

main()
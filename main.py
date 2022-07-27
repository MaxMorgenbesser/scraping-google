


#allows me to search google without a certificate
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from googlesearch import search


# to search
query = input('Please enter what you would like to search google for.:\n')

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
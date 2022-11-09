import requests
from bs4 import BeautifulSoup
from Module.filter_link import filter_link
import time
from requests.adapters import HTTPAdapter, Retry
import colorama

class join():
    def finder(__search):
        mailto=[]
        s = requests.Session()

        retries = Retry(total=1,
                backoff_factor=1,
                status_forcelist=[ 500, 502, 503, 504,404 ])
        for k in range(len(__search)):
            #code discord_boku_bot
            url_now = __search[k]
            print(colorama.Fore.GREEN + url_now)

            try:
                
                time.sleep(2)
                s.mount('https://', HTTPAdapter(max_retries=retries))
                response = s.get(url_now,allow_redirects=False)
                soup = BeautifulSoup(response.text,'lxml')
                quotes = soup.find_all('a')
                for i in range(len(quotes)):
                    if str(quotes[i]).find("compose?To") != -1:
                        mailto.append(quotes[i])
                    if str(quotes[i]).find("mailto:") != -1:
                        mailto.append(quotes[i])
            except Exception as  e:

                try:
                    print(colorama.Fore.YELLOW +"error: " [k], e)
                    print(colorama.Fore.CYAN +"Trying to play through port 80...")
                    time.sleep(2)
                    s.mount('http://', HTTPAdapter(max_retries=retries))
                    filter_link.join(url_now)
                    response = s.get(url_now,verify=False,allow_redirects=False)
                    soup = BeautifulSoup(response.text,'lxml')
                    quotes = soup.find_all('a')
                    for i in range(len(quotes)):
                        if str(quotes[i]).find("compose?To") != -1:
                            mailto.append(quotes[i])
                        if str(quotes[i]).find("mailto:") != -1:
                            mailto.append(quotes[i])
                except Exception as  e:
                    print(colorama.Fore.RED +"error: ",e)
                
                
            
        return mailto



            


    def filter(_base):
        __out = []
        for f in range(len(_base)):
            mail = str(_base[f])
            try:
                mail = mail.split('mailto:')[1]
                mail = mail.split('"')[0]
            except:
                mail = mail.split("compose?To=")[1]
                mail = mail.split('"')[0]
            if mail.find('@') != -1:
                __out.append(mail)
                
            
        return __out




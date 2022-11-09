import requests
from bs4 import BeautifulSoup
from Module.filter_link import filter_link

class join():
    def finder(__search):
        mailto=[]
        for k in range(len(__search)):
            #code discord_boku_bot
            url_now = __search[k]
            
            
            try:
                response = requests.get(url_now)
                soup = BeautifulSoup(response.text,'lxml')
                quotes = soup.find_all('a')
                for i in range(len(quotes)):
                    if str(quotes[i]).find("compose?To") != -1:
                        mailto.append(quotes[i])
                    if str(quotes[i]).find("mailto:") != -1:
                        mailto.append(quotes[i])
            except Exception as  e:
                print("error: " [k], e)
                print("Пробуем запустить через 80 порт...")
                try:
                    filter_link.join(url_now)


                    response = requests.get(url_now,verify=False)
                    soup = BeautifulSoup(response.text,'lxml')
                    quotes = soup.find_all('a')
                    for i in range(len(quotes)):
                        if str(quotes[i]).find("compose?To") != -1:
                            mailto.append(quotes[i])
                        if str(quotes[i]).find("mailto:") != -1:
                            mailto.append(quotes[i])
                except Exception as  e:
                    print("error: "[k],e)
                
                
            
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




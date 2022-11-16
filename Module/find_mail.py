import requests
from bs4 import BeautifulSoup
from Module.filter_link import filter_link
import time
from requests.adapters import HTTPAdapter, Retry
import colorama
import warnings


class join():
    def finder(__search):
        warnings.simplefilter("ignore")
        mailto = []
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        retries = Retry(connect=3,
                        total=1,
                        backoff_factor=0.5,
                        status_forcelist=[500, 502, 503, 504, 404])
        for k in range(len(__search)):
            # code discord_boku_bot
            url_now = __search[k]
            print(colorama.Fore.GREEN, k+1, url_now)

            try:

                time.sleep(2)
                s.mount('https://', HTTPAdapter(max_retries=retries))
                response = s.get(url_now, allow_redirects=False)
                soup = BeautifulSoup(response.text, 'lxml')
                quotes = soup.find_all('a')
                for i in range(len(quotes)):
                    if str(quotes[i]).find("compose?To") != -1:
                        mailto.append(quotes[i])
                    if str(quotes[i]).find("mailto:") != -1:
                        mailto.append(quotes[i])
            except Exception as e:

                try:
                    if str(e).find("Max retries exceeded with url:") != -1:
                        pass
                    else:
                        print(colorama.Fore.YELLOW + "error: ", k, e)
                    print(colorama.Fore.CYAN +
                          "[1 method] Trying to play through port 80...")
                    time.sleep(2)
                    s.mount('http://', HTTPAdapter(max_retries=retries))
                    filter_link.join(url_now)
                    response = s.get(url_now, verify=False,
                                     allow_redirects=False)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('a')
                    for i in range(len(quotes)):
                        if str(quotes[i]).find("compose?To") != -1:
                            mailto.append(quotes[i])
                        if str(quotes[i]).find("mailto:") != -1:
                            mailto.append(quotes[i])
                except Exception as e:
                    try:
                        if str(e).find("Max retries exceeded with url:") != -1:
                            print(
                                colorama.Fore.CYAN + "[2 method] Adding a deceptive browser to read cookies")
                            time.sleep(2)
                            s.mount('https://', HTTPAdapter(max_retries=retries))
                            try:
                                response = s.get(url_now, verify=False,
                                                 allow_redirects=False, headers=headers)
                            except Exception as e:
                                if str(e).find("(Caused by SSLError(SSLError(1, '[SSL: TLSV1_ALERT_ACCESS_DENIED] tlsv1 alert access denied (_ssl.c:997)')))") != -1:
                                    filter_link.join(url_now)
                                    response = s.get(url_now, verify=False,
                                                     allow_redirects=False, headers=headers)

                            soup = BeautifulSoup(response.text, 'lxml')
                            quotes = soup.find_all('a')
                            for i in range(len(quotes)):
                                if str(quotes[i]).find("compose?To") != -1:
                                    mailto.append(quotes[i])
                            if str(quotes[i]).find("mailto:") != -1:
                                mailto.append(quotes[i])
                        else:
                            print(colorama.Fore.RED + "error: ", e)
                    except Exception as e:
                        if str(e).find("list index out of range") != -1:
                            print(colorama.Fore.YELLOW + "Mail was not find")
                        else:
                            print(colorama.Fore.RED + "Error:", e)

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

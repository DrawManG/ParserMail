from Module import send_google, find_mail, export_mail
from os.path import abspath
import colorama


'''
CHANGE IT TO THE ONE YOU NEED:
text     = Insert a query into the search engine here (the words for which the mail will be located)
how_many = Insert the number of links you need here (If there are 10, then there will be 10 links = 10 mails (if there are no errors))
txt_file = True\False switch, if necessary, download the received information immediately to a txt file (will be saved in the root of the "[Your request].txt" repository)
'''

text = 'Геотехническая лаборатория'
how_many = 250
txt_file = True


_send_google = send_google.join.search(text, how_many)
print(colorama.Fore.LIGHTBLUE_EX + "link google: ", _send_google, "\n")
print("")
print(colorama.Fore.LIGHTBLUE_EX +
      "how many link search: ", len(_send_google), "\n")
out_mail = find_mail.join.finder(_send_google)
result_mailto = find_mail.join.filter(out_mail)
print(colorama.Fore.LIGHTBLUE_EX + "result: ", result_mailto)
if txt_file == True:
    export_mail.join.export_to_txt(
        result_mailto, text, abspath(__file__).replace("index.py", ""))

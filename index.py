from Module import send_google,find_mail,export_mail
from os.path import abspath
import colorama

text = 'We make custom music from $10'
how_many = 10
txt_file = False

_send_google = send_google.join.search(text,how_many)
print(colorama.Fore.LIGHTBLUE_EX +"link google: ", _send_google,"\n")
out_mail = find_mail.join.finder(_send_google)
result_mailto = find_mail.join.filter(out_mail)
print(colorama.Fore.LIGHTBLUE_EX  +"result: ",result_mailto)
if txt_file == True:
    export_mail.join.export_to_txt(result_mailto, text, abspath(__file__).replace("index.py",""))

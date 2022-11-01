from Module import send_google,find_mail


text = 'Путёвки в питер'
how_many = 10

_send_google = send_google.join.search(text,how_many)
out_mail = find_mail.join.finder(_send_google)
result_mailto = find_mail.join.filter(out_mail)
print(result_mailto)
import datetime 
entries = []
user_selection = input('Entry --> a \n Quit--> q')

while user_selection != 'q':
    entries.append({'content': entry_content, 'date':datetime.datetime.today().strftime("%b %d")})
    user_selection = input('Entry --> a \n Quit--> q')

print(entries)
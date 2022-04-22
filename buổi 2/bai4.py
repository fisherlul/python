from datetime import datetime as d
date_str = input("Enter today's date: ")
date_obj = d.strptime(date_str, "%m/%d/%Y")
date = d.strftime(date_obj, "%d/%m/%Y")
print(f'Date in MM/DD/YYYY: \033[1m{date_str}\033[0m\nDate in DD/MM/YYYY: {date}')
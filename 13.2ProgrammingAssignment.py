##13.2 & 13.3

from datetime import date

today_string = date(2024,2,19)
fmt = "%B %d, %Y"
print(today_string.strftime(fmt))
"""Main script for daily_market download"""

import daily_market

YEAR = raw_input("Year: ")
MONTH = raw_input("Month: ")
DAY = raw_input("Day:  ")


print("Data from: "+ DAY + " - " + MONTH + " - " + YEAR + "\n")

try:
    daily_market.download_file(DAY, MONTH, YEAR)
    daily_market.read_prices()
except:
    print("ERROR: Not a valid date")

import pyshorteners

url = input("Enter Url: ")

print("Url after shortening: ", pyshorteners.Shortener().tinyurl.short(url))

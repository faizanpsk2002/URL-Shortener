import pyshorteners

print("\n")

link = input("Enter Your URL or LINK :  ")

print("\n")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print("Your Shorted URL or LINK is :  ", x)

print("\n")

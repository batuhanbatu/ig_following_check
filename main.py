import locale

# Finding language of the operating system
print(locale.getdefaultlocale())

# Opening a saved html file
file = open("file.html", "r")
print (file.read())
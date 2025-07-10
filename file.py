f = open("strfile.txt")
data = f.read()
f.close()

emails = []
words = data.split()

for word in words:
    if "@gmail.com,org" in word:
        emails.append(word)

if emails:
    print("Gmail Addresses:")
    for email in emails:
        print(email)
else:
    print("No Gmail addresses found")

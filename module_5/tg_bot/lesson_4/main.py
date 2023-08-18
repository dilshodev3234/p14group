


with open("index.html" , "r") as f:
    data = f.read()

for i in data.split("<h1>")[1:]:
    print(i[:i.find("</h1>")])
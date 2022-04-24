import requests

for i in range(213): # it has 212 pages but the first i is 0
    response = requests.get("https://online.fliphtml5.com/kzpyj/tdpm/files/large/" + str(i) + ".jpg")
    with open("Slike/" + str(i) + ".jpg", 'wb') as f:
        f.write(response.content)
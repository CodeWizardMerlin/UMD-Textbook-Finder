from libgen_api_enhanced import LibgenSearch
import webscrape
import requests
import json

print("Paste URL")
user_url = input()
ISBNs = webscrape.find_isbn(user_url)

# api calls
mobi_file = False
search_url = "https://annas-archive-api.p.rapidapi.com/search"
download_url = "https://annas-archive-api.p.rapidapi.com/download"
api_key = json.load(open("key.json", "r"))["private_key"]
headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "annas-archive-api.p.rapidapi.com"
}
for isbn in ISBNs:
    querystring_find = {"q":isbn,"skip":"0","limit":"2","ext":"pdf, epub, mobi","source":"libgenLi, libgenRs"}
    response = (requests.get(search_url, headers=headers, params=querystring_find))
    data = json.load(response)[0]["books"][0]

    print(data["title"] + " (" + data["size"] + ")" + " (" + data["year"] + ")")
    print("By: " + data["author"])
    if (data["format"] == "mobi"):
        mobi_file = True

    s = LibgenSearch()
    results = s.search_title(data["title"])
    print("Direct Download Link: " + results[0]["Direct_Download_Link"])
    print()

if (mobi_file):
    print("Convert mobi filetype to pdf here: https://www.adobe.com/uk/acrobat/online/convert-pdf.html")
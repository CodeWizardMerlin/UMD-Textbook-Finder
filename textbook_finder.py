from isbnF import ISBN
import requests
import json

print("Paste URL")
user_url = "https://umcp.bncollege.com/course-material-listing-page?utm_campaign=storeId=15551_langId=-1_courseData=CMSC_216_0401_202501%7CCMSC_250_0303_202501%7CHIST_187_0102_202501%7CMATH_240_0332_202501&utm_source=wcs&utm_medium=registration_integration"
#user_url = input()
ISBNs = ISBN.get(user_url)

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
    querystring_find = {"q":isbn,"skip":"0","limit":"1","ext":"pdf, epub, mobi"}
    response = requests.get(search_url, headers=headers, params=querystring_find)

    

    print("Title:" + response.json()["title"] + "-" + response.json()["year"])
    print("Author(s):" + response.json()["author"])
    print(response.json()["format"] + "-" + response.json()["size"])
    if (response.json()["format"] == "mobi"):
        mobi_file = True

    querystring_download = {"md5":response.json()["md5"]}
    response = requests.get(download_url, headers=headers, params=querystring_download)
    print("Link:" + response.json()["0"])
    print()

if (mobi_file):
    print("Convert mobi filetype to pdf here: https://www.adobe.com/uk/acrobat/online/convert-pdf.html")
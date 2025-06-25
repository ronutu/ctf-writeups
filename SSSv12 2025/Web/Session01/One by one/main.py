from http.cookiejar import MozillaCookieJar
import requests
import re

cookies = MozillaCookieJar('cookies.txt')
cookies.load()

session = requests.Session()
session.cookies = cookies

flag = ""
for _ in range(1, 100):
    r = session.get("http://141.85.224.70:8090/one-by-one/").text
    pattern = re.compile(r'(?<=<p>).(?=</p>)')
    match = pattern.search(r)
    if match:
        flag += match.group()

print(flag)
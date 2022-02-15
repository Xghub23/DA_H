# Perform a “get” request on the given website

import requests as req

resp = req.get("http://www.webcode.me")

print(resp.text)

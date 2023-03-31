#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email
"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("utf-8")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

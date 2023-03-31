#!/usr/bin/python3
""" sends a request to the url and displays 
the value of the x-Request-ID
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))

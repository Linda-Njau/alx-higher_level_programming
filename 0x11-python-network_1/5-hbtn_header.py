#!/usr/bin/python3
""" displays the value of variable X-Request-Id
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))

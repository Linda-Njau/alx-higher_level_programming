#!/usr/bin/python3
"""
sends POST request with email as a parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    value = {"email": agrv[2]}
    response = requests.post(argv[1], data=value)
    print(response.text)

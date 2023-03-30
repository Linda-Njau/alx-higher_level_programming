#!/bin/bash
#Get length in bytes of the body of response
curl -s "$1" | wc -c

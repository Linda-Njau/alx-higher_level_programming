#!/bin/bash
#displays HTTP methods allowed
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

#!/bin/bash

curl -s http://localhost:8000/partners/$1/engagements/ | python -m json.tool

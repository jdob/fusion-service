#!/bin/bash

curl -s http://localhost:8000/partners/ | python -m json.tool

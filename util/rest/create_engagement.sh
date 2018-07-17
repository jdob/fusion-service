#!/bin/bash

curl -s -H "Content-Type: application/json" -X POST -d "@create_engagement.json" http://localhost:8000/partners/$1/engagements/

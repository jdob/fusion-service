#!/bin/bash

curl -s -H "Content-Type: application/json" -X POST -d '{"username": "admin", "password": "admin"}' http://localhost:8000/api-token-auth/

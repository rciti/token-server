import os
from flask import Flask, json
from waitress import serve

# read first token and remove from the token file
token_filename = "tokens.txt"

def pop_token(filename):
  with open(filename, "r+") as f:
    token = f.readline().rstrip('\n')
    tokens = f.read()
    f.seek(0)
    f.write(tokens)
    f.truncate()
  return(token)

api = Flask(__name__)

@api.route('/token', methods=['GET'])
def get_token():
  return {"token": pop_token(token_filename)}

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=5000)
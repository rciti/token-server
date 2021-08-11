import os
from flask import Flask, json

# create a token index file if not exists
token_index_filename = ".next_token_index"
if not os.path.exists(token_index_filename):
  with open(token_index_filename, "w") as f:
    f.write('0')

# read tokens
with open("tokens.txt", "r") as f:
  tokens = f.read().split("\n")

def get_and_update_next_token_index(filename):
  
  # get the current value
  with open(filename, "r") as f:
    next_token_index = f.read()
    next_token_index = int(next_token_index)
  
  print(next_token_index)
  # overwrite with a new value
  with open(filename, 'w') as f:
    f.write(str(next_token_index + 1))

  return next_token_index

api = Flask(__name__)

@api.route('/token', methods=['GET'])
def get_companies():
  next_token_index = get_and_update_next_token_index(token_index_filename)
  return json.dumps(tokens[next_token_index])

if __name__ == '__main__':
    from waitress import serve
    serve(api, host='0.0.0.0', port=5000) 
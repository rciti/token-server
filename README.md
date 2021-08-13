# token-server

## How to use this service?

1) Generate tokens using `generate_tokens.py`. This script generates two files that are identical: `original-tokens.txt` and `tokens.txt`. 
2) Configure and run Dockerfile.

## How does it work?

Run `get_token.py` to spin up a REST API server. If you are running it on your local machine, going to `localhost:5000/token` on your browser should get you a token from the pre-generated list of tokens. The API server pops the first entry of `tokens.txt` and returns to the request, meaning that after each request the number of tokens in `tokens.txt` will be one token less than before. However, the `original-tokens.txt` won't change, and one can use it to validate if the tokens that were given out are valid.

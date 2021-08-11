docker build -t token-server .
docker stop token-server
docker rm token-server
docker run -d \
    -p 5000:5000 \
    --mount type=bind,source="$(pwd)"/tokens.txt,target=/usr/src/token-server/tokens.txt \
    --name=token-server token-server
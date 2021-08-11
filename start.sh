docker build -t token-server .
docker stop token-server
docker rm token-server
docker run -d -p 5000:5000 --name=token-server token-server
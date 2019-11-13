virtual-public-network local repro setup
========================================

1. Check out https://github.com/pclinger/docker-apache-perl/
2. `cd docker-apache-perl && docker build -t docker-apache-perl .`
6. `chmod +x src/diag.cgi` (make sure this is set)
7. `./server.sh`
8. `docker ps | grep docker-apache-perl` and cpy container name
9. `docker exec -it $CONTAINER_NAME /bin/bash` and then `apt install tcpdump`
10. open [`https://localhost:1337`](https://localhost:1337) to see the helpful web interface
11. `../exploit_local.py "ls -hla /"` to run the exploit


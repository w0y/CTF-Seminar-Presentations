#!/usr/bin/env bash
docker run -v $PWD/src:/var/www/html -p 1337:80 -d --rm docker-apache-perl /usr/sbin/apache2ctl -D FOREGROUND

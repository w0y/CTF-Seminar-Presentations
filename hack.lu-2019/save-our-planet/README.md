# Save our planet
## Bot
* `git clone https://github.com/pspaul/ctf-challenges.git`
* `cd save-our-planet/bot`
* `docker build -t save-our-planet .`
* `docker run save-our-planet-bot http://10.0.2.2:8080?flag-page=http://10.0.2.2:9000/ "[{\"url\":\"http://10.0.2.2:9000/setflag.html\",\"cookies\":[]}]"`

* `cd save-our-planet/flag-page`
* `http-server -p 9000`

## exploit
* go to exploit directory
* `http-server -p 8080 -d .`
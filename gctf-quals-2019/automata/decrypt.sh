#!/usr/bin/env bash
while read in;
do
        echo "$in" > /tmp/plain.key 
        xxd -r -p /tmp/plain.key > /tmp/enc.key
        echo "U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ=" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key
done < keys.txt

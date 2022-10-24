import json
import re
import requests
import os
import yara

# Preamble
input_directory = './inputs'
result_directory = "./results"
user_agent = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"} 
rule = yara.compile("./rules/RULES.yara")

# iterate over files in inputs folder
for file_name in os.listdir(input_directory):
    file_path = os.path.join(input_directory, file_name)

    # checking if it is a file
    if os.path.isfile(file_path):

        # read files
        file_handler = open(file_path, "r")
        file_content = file_handler.read()

        # REGEX to get URL
        url_list = re.findall("(?P<url>https?://[^\s]+)", file_content)
        
        # list for matches 
        match_list = []

        # result dictionary
        res_dict = {
            "file_name": file_name,
            "result": match_list
        }

        # iterate over URL
        for url in url_list:

            # file handler for results
            res_file_name = "./results/{}.json".format(file_name.split(".")[0])
            res_file_handler = open(res_file_name, "w", encoding="utf-8")
            res = requests.get(url, headers=user_agent).text

            matched = rule.match(data=res)
            # print("{}:{}".format(url, matched))

            # add dict to list
            match_list_dict = {
                "url" : url,
                "matches" : str(matched).strip("[]").split(",")
            }
            match_list.append(match_list_dict)

            # save json
            res_file_handler.write(json.dumps(res_dict))
            res_file_handler.close()
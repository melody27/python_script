import requests
import hashlib
import base64
# import mmh3
import pymmh3
import re
import time



class favicon(object):

    def __init__(self,url):
        self.url = url
        self.hash = None

    def chang_format(self,content):
        end_str_length = len(content) % 76
        raw_content_list = re.findall(r'.{76}',content)
        end_str = content[-end_str_length::]
        raw_content_list.append(end_str)

        return "{}\n".format("\n".join(raw_content_list))



    def get_hash(self):
        favicon_raw_data = self.get_favicon()
        favicon_data = self.chang_format(favicon_raw_data)

        result = pymmh3.hash(favicon_data)
        self.hash = result

    def get_favicon(self):
        favicon_raw_data = requests.get(self.url,verify=False)
        favicon_data = base64.b64encode(favicon_raw_data.content).decode('utf-8')
        # print(favicon_data)
        return favicon_data


if __name__ == "__main__":


    data = favicon('http://www.baidu.com/favicon.ico')
    data.get_hash()
    print(data.hash)

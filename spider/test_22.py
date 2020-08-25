import pymmh3
import requests
import base64
import re
import time


def change_format(content):
    end_str_length = len(content) % 76
    new_content_list = re.findall(r'.{76}',content)
    end_str = content[-end_str_length::]
    
    new_content_list.append(end_str)
    return "{}\n".format("\n".join(new_content_list))


if __name__ == "__main__":
    start_time = time.time()
    response = requests.get('https://www.baidu.com/favicon.ico')
    if response.headers['Content-Type'] == "image/x-icon":
        favicon = base64.b64encode(response.content).decode('utf-8')
        hash = pymmh3.hash(change_format(favicon))
        print(hash)
    end_time = time.time()

    print("总用时为：{}".format((end_time-start_time)))
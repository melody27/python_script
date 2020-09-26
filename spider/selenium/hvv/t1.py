import re


def exteact_message(data):
    result = {}
    message = data
    ip_list = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',message)
    honeypot_name = re.findall(r'ag_\w+',message)[0]
    attack_message = re.findall(r"(?<=上的).+",message)[0]
    attack_ip = ''
    honeypot_ip = ''
    for x in ip_list:
        if x.startswith("172.18") or x.startswith("10.79"):
            honeypot_ip = x
        else:
            attack_ip = x
    result['honeypot_name'] = honeypot_name
    result['attack_message'] = attack_message
    result['attack_ip'] = attack_ip
    result['honeypot_ip'] = honeypot_ip
    
    return result



data = "202.60.123.136 入侵了探针 ag_79f2a234(172.18.20.51) 上的 中国华电集团高级培训中心-trace(自定义 Web (PHP)) 蜜罐"
print(exteact_message(data))
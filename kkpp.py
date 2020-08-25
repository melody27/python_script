import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'adicwu.loidair.com'])
# print('Exit code:', r)

import subprocess

p = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'print(1)\n')
print("结果: " + output.decode('utf-8'))
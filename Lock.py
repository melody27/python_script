import time,threading
balance=0
def jack(n):
    global balance
    balance=balance+n
    balance=balance-n
def jisuan(n):
    for x in range(1000):
        jack(n)
af=threading.Thread(target=jisuan,args=(5,))
ae=threading.Thread(target=jisuan,args=(8,))
af.start()
ae.start()
af.join()
ae.join()
print(balance)
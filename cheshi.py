def gg(a):
    s=int(a)
    # if s==0:
    #     raise print('除数不能为0')
    assert s!=0,'s is zero'
    return 10/s
def main():
    try:
        return gg('0')
    except Exception as e:
        print('worry is',e)
main()
print('-------'*10)
import logging
logging.basicConfig(level=logging.INFO)
e='0'
z=int(e)
logging.info('n=%d'%z)
print(10/z)
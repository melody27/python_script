import socket
import argparse

# argparse使用测试
# 官方API文档



parse = argparse.ArgumentParser(description="redis利用脚本")
group = parse.add_mutually_exclusive_group()
            # 指定位置参数，

# group有冲突的选项
# group.add_argument('-q','--quiet',help="测试add_mutually_exclusive_group方法",required=True)    # required强行指定可选参数为必选
group.add_argument('-v','--verbios',help="查看详细使用，不需要参数的选项",action="store_true")    # 使用 action参数即可指定不需要参数的选项
parse.add_argument('-l','--let',help="测试action中的计数",action="count")
parse.add_argument('echo')
parse.add_argument('-i','--input',help="测试数字类型和可选值",choices=[1,2,3],type=int,default=1)
                # 短选项  长选项        help信息                可选值     指定输入值类型  默认值 
parse.add_argument('rport',help='目标端口。不填,默认为6379。示例：6379',nargs='?',default=6379,type=int)
                                                                   # nargs参数和default参数搭配，构建可选的位置参数。默认的位置参数必选

# 指定输入或输出文件
# parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),default=sys.stdin)
# parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),default=sys.stdout)


args = parse.parse_args()
test = args.read_buff
if args.verbios:
    print("使用-s 参数指定模式")
if args.input:
    print("输出-i的值：{}".format(args.input))
if args.echo:
    print("已经指定号echo ")
if args.let:
    print("输出一下args.let的获取数量",args.let)

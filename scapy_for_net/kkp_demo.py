from scapy.all import *
# from automaton import *


# 未完成的 python scapy automaton demo 

# 需要记住的是，实际上automaton类是scapy类的子类。scapy类的方法，实际上automaton类都可以使用。例如：send，srp等方法。



class Helper(Automaton):
    # def parse_args(self,filename, server, sport=None, port=80, **keys):
        
    #     Automaton.parse_args(self, **keys)
    #     self.filename = filename
    #     self.server = server
    #     self.port = port
    #     self.sport = sport

    def master_filter(self, pkt):
        return ( IP in pkt and pkt[IP].src == self.server and TCP in pkt)


    




    @ATMT.state(initial=1)
    def BEGIN(self):
        self.server = '192.168.3.70'
        self.send(IP(dst="192.168.3.30")/TCP(sport=80,flags="S"))

        print("here is a begin ")
        raise self.jisuan()


    @ATMT.state()
    def jisuan(self):
        print("here is a jisuan function")
        pass
    @ATMT.receive_condition(jisuan,prio=1)
    def start_condition(self,pkt):
        # print("this is a conditions for start")

        pkt.show()
        self.send(IP(dst="192.168.3.30")/TCP(dport=80,flags="S",options=[("Timestamp",(0,0))]))
        # self.show()
        raise self.END()



    @ATMT.state(error=1)
    def ERROR(self):
        return "here is a error on here"


    @ATMT.state(final=1)
    def END(self):
        return "this is a end"


melody = Helper()
melody.run()
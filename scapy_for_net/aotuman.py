from scapy.all import *
# from automaton import *


class HelloWorld(Automaton):
    
    @ATMT.state(initial=1)                  # 不能将start作为automaton的入口函数，否则无法进入。应该是其automaton类本身要使用start函数
    def into(self):                            # run 也不能占用
        print("i think this is start function")

    
    @ATMT.condition(into)
    def start_condition(self):
        print("this is a conditions for start")
        raise self.end()

    @ATMT.action(start_condition)
    def start_action(self):
        print("this should be an action for condition excuted over")



    @ATMT.state(final=1)
    def end(self):
        print(" this is a end ,should be state for final")

if __name__ == "__main__":
    print("进入状态机")
    melody = HelloWorld()
    melody.run()
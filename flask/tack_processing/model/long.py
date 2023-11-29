from model.thing import Thing

class Long_im_not(Thing):
    def __init__(sel,name=None,summary=None,desc=None,deadline=None,important=None,emergent=None,processing=None,status=None,priority=None):
        super().__init__(name,summary,desc,deadline,False,emergent,processing,status,priority)



class Long_im(Thing):
    def __init__(sel,name=None,summary=None,desc=None,deadline=None,important=None,emergent=None,processing=None,status=None,priority=None):
        super().__init__(name,summary,desc,deadline,True,emergent,processing,status,priority)


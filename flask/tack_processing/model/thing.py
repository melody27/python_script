

# 直接使用 list来代替chain
class Thing(object):
    def __init__(self,name=None,summary=None,desc=None,deadline=None,important=None,emergent=None,processing=None,status=None,priority=None):
        self.name=name
        self.summary=summary
        self.desc=desc
        self.deadline=deadline

        # for status
        self.important=important
        self.emergent=emergent
        self.processing=processing
        self.status=status
        self.priority=priority




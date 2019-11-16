from node import node
class BST(object):
    def __init__(self):
        self.rootnode=None
        
    def insert(self,data):
        if not self.rootnode:
            self.rootnode=node(data)
        else:
            self.rootnode.insert(data)
            
    def getmin(self):
        if self.rootnode:
            return self.rootnode.getmin()
        
    def getmax(self):
        if self.rootnode:
            return self.rootnode.getmax()
        
    def traverseinorder(self):
        if self.rootnode:
            return self.rootnode.traverseinorder()
        
    def remove(self, datatoremove):
        if self.rootnode:
            if self.rootnode==datatoremove:
                tempnode= node(None)
                tempnode.leftchild=self.rootnode
                self.rootnode.remove(datatoremove, tempnode)
            else:
                self.rootnode.remove(datatoremove, None)
class node(object):
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        
    def insert(self,data):
        if data<self.data:
            if not self.leftchild:
                self.leftchild=node(data)
            else:
                self.leftchild.insert(data)
        else:
            if not self.rightchild:
                self.rightchild=node(data)
            else:
                self.rightchild.insert(data)
                
    def getmin(self):
        if self.leftchild is None:
            print(self.data)
            return self.data
            print(self.data)
        else:
            return self.leftchild.getmin()
            print(self.data)
        
    def getmax(self):
        if self.rightchild is None:
            print(self.data)
            return self.data
            
        else:
            return self.rightchild.getmax()
            print(self.data)
        
    def traverseinorder(self):
        if self.leftchild is not None:
            self.leftchild.traverseinorder()
            
        print(self.data)
        
        if self.rightchild is not None:
            self.rightchild.traverseinorder()
            
    def remove(self,data,parentnode):
        if data<self.data:
            if self.leftchild is not None:
                self.leftchild.remove(data,self)
        elif data>self.data:
            if self.rightchild is not None:
                self.rightchild.remove(data,self)
                
        else:
            if self.leftchild is not None and self.rightchild is not None:
                self.data=self.rightchild.getmin()
                self.rightchild.remove(self.data, self)
                
            elif parentnode.leftchild==self:
                if self.leftchild is not None:
                    tempnode= self.leftchild
                else:
                    tempnode= self.rightchild
                    parentnode.leftchild=tempnode
                    
            elif parentnode.rightchild==self:
                if self.leftchild is not None:
                    tempnode= self.leftchild
                else:
                    tempnode= self.rightchild
                    parentnode.rightchild=tempnode
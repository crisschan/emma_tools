#encoding=utf8
#!/usr/bin/env python
# __author_='crisschan'
# __data__='20161130'
# __from__='EmmaTools'
#栈的操作
class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        '''
        返回是否为空
        Returns: true  为空
                 false  不为空
        '''
        return len(self.items)==0
    def push(self,item):
        '''
        入栈
        Args:
            item: 入栈的数据

        Returns:null

        '''
        self.items.append(item)
    def pop(self):
        '''
        出栈
        Returns:null

        '''
        return self.items.pop()
    def peek(self):
        '''
        查看栈顶对象而不移除它
        Returns: 栈顶元素

        '''
        if not self.isEmpty():
            return self.items[len(self.items)-1]
    def size(self):
        '''
        计算站大小
        Returns:长度

        '''
        return len(self.items)
'''
if __name__=="__main__":
    s=Stack()
    print s.isEmpty()
    s.push('1')
    print s.peek()
    s.push(444)
    print s.items
    print s.size()
    print s.pop()
    print s.size()
'''
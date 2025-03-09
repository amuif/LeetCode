class CacheNode:
    def __init__(self,key,val,prev=None,nextt=None):
        self.val = val
        self.key = key
        self.prev=prev
        self.next=nextt

class LRUCache:

    def __init__(self, capacity: int):
        self.my_dic={}
        self.capacity = capacity
        self.head = CacheNode(-1,-1)
        self.tail = CacheNode(-1,-1)
        self.head.prev = self.tail
        self.tail.next = self.head

    def remove(self,node):
        # previous = node.prev
        # next_one = node.next
        node.prev.next = node.next
        node.next.prev = node.prev

    def promote(self,node):
        node.prev = self.head.prev
        node.next = self.head

        self.head.prev.next = node
        self.head.prev = node



    def get(self, key: int) -> int:
        # print((self.my_dic.keys()))
        value = -1
        
        if key  in self.my_dic:
            node = self.my_dic[key]
            self.remove(node)
            self.promote(node)
            value = node.val
            # return node.val       
        return value
        

    def put(self, key: int, value: int) -> None:
        # print(len(self.my_dic))
        node = None
        
        if key in self.my_dic:
            node = self.my_dic[key]
            node.val = value
            self.remove(node)
            # self.promote(node)

        else:
            node =  CacheNode(value,key)
            self.my_dic[key] = node

        self.promote(node)

        if self.capacity  < len(self.my_dic):
            last_node = self.tail.next
            self.remove(last_node)
            del self.my_dic[last_node.key]

            

                   

             


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
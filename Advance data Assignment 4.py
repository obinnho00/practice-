class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_newaddress(self, current_adress, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_adress is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_addres = current_adress.next
            new_node.next = new_addres
            new_node.prev = current_adress
            current_adress.next = new_node
            new_addres.prev = new_node

    def remove(self, current_node):
        successor_node = current_node.next
        predecessor_node = current_node.prev

        if successor_node is not None:
            successor_node.prev = predecessor_node

        if predecessor_node is not None:
            predecessor_node.next = successor_node

        if current_node is self.head:
            self.head = successor_node

        if current_node is self.tail:
            self.tail = predecessor_node


    def print(self):
        if self.head is None:
            return
        val = self.head
        while val != None:
            num = val.data
            val = val.next

            print(num)




cal = LinkedList()
cal.append(Node("Head Northwest on S charles\nBlvd toward E 11th St"))
cal.append(Node("0.1 miles\nTurn left onto E 10th St"))
cal.append(Node("keep left\n in 1.1 mile\n Continue straight onto W 10th St/Farmville Blvd"))
cal.append(Node("-----> pass by walls fargo Bank(on the right in 0.3 mi\n in 2.2 miles|---->"))
cal.append(Node("Continue onto john P East Memorial HWY\n 37 miles\<---|----Keep left to stay on I-795 N"))
cal.append(Node("19 miles\n<----Take the US-64 W exit on the left toward Raleigh"))
cal.append(Node('17 miles\nUse the |---> right 2 lanes to take exist 3 for\n for I-440 W toward US-1/wake Forest'))
cal.append(Node("6.7 miles\nTake exist 7 B for US-70 W/NC-50 N/Glenwood Ave toward Crabtree Vly/Durham"))
cal.append(Node("0.1 miles\n<--- Use the left lane to merge onto NC-50 N/US-70 W/Glenwood Ave"))
cal.append(Node("0.2 miles\nUse the left 2 lanes to turn left onto Blue Ridge Rd"))
cal.append(Node("200 feet\n Arraved\n Crabtree Valley Mal\n4325 Glenwood Ave, Raleigh\nNC 27612"))

cal.print()
class MaxHeap:
    def __init__(self, list):
        self.heap = []
        for element in list:
            self.insert(element)

    def __len__(self):
        return len(self.heap)
    
    def insert(self, value):
        self.heap.append(value)
        self.pushUp(len(self)-1)
    
    def popMax(self):
        max = self.heap[0]
        last = self.heap.pop()
        if len(self)>0:
            self.heap[0] = last
            self.pushDown(0)
        return max

    def pushUp(self, pos):
        if pos != 0:
            parentPos = pos//2
            if self.heap[pos] > self.heap[parentPos]:
               self.swap(pos, parentPos)
               self.pushUp(parentPos)

    def pushDown(self, pos):
        if not self.isLeaf(pos):
            leftChildPos = 2 * pos
            rightChildPos = 2 * pos + 1
            if rightChildPos < len(self):
                if self.heap[rightChildPos] > self.heap[leftChildPos] and self.heap[pos]<self.heap[rightChildPos]:
                    self.swap(pos, rightChildPos)
                    self.pushDown(rightChildPos)
                    return
            if self.heap[pos]<self.heap[leftChildPos]:
                self.swap(pos, leftChildPos)
                self.pushDown(leftChildPos)
    
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def isLeaf(self, pos):
            return True if pos >= len(self)//2 and pos<= len(self) else 0


def productOfLargest(_list, k=3):
    '''Function that finds the highest product between k of those numbers

    params:
    _list(list): List of numbers
    k(int): Number of integers

    returns:
    int:The product
    '''
    heap = MaxHeap(_list) #Alternatives: sorted list, heapq with negative version of list
    product = 1
    for i in range(k):
        product *= heap.popMax()
    return product

if __name__=='__main__':
    testList = [1,10,2,6,5,3]
    testList2 = [4,5,6]
    testList3 = [1232,41234 ,51345, 41532346,674567, 1234, 1, 63456]
    testList4 = [1,2]
    tests = [testList, testList2, testList3, testList4]
    for _list in tests:
        print(productOfLargest(_list))

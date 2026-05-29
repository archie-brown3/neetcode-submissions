class DynamicArray:
    
    # [1, 0, 0, 0]
    # size = 1
    # capacity = 3

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.arr = [0] * self.capacity



    def get(self, i: int) -> int: 
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
         

    def pushback(self, n: int) -> None:
        # push self[n] to the end of the array
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n 
        self.size += 1 
        


    def popback(self) -> int:
        # get the value at the end of the array
        self.size -= 1 
        popped = self.arr[self.size]
    
        return popped

 

    def resize(self) -> None:
        self.capacity = self.capacity * 2 
        new_array = [0] * self.capacity # create a new array with * 2 capacity
        for i in range(self.size):
            new_array[i] = self.arr[i]
        self.arr = new_array
        



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity 

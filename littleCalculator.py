class Calculator:
    #Init is making a default to the methods, as also, assign value to object properties without being manually
    def __init__(self, *args):
        self.args = args

    def add(self): 
        #acessing the first number
        result = self.args[0] 
        for num in self.args[1:]: 
           result += num 
        return result
    
    def substract(self):
        #saving the first number put on args
        result = self.args[0]
        #while true, the loop will acess each number from args through the num
        for num in self.args[1:]:
            #updating the result, before it was a number, now its a new number 
            result -= num
        return result

    def multiply(self):
        result = args[0]
        for num in args[1:]:
            result *= num
        return result
    
    def divide(self):
        result = self.args[0]
        #it will take from the first one because result = args[0] is already taking the first one 
        for num in self.args[1:]:
            result /= num
        return result


#bringing the "character" to life(instancing)
cal1 = Calculator(1,2, 4)
cal1.add()


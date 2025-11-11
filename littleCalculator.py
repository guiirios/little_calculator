#MY Calculator
class Calculator:
    def add(self, *args): 
        #acessing the first number
        result = args[0] 
        for num in args[1:]: 
           result += num 
        return result
    
    def substract(self, *args):
        #saving the first number put on args
        result = args[0]
        #while true, the loop will acess each number from args through the num
        for num in args[1:]:
            #updating the result, before it was a number, now its a new number 
            result -= num
        return result

    def multiply(self, *args):
        result = args[0]
        for num in args[1:]:
            result *= num
        return result
    
    def divide(self, *args):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result


#bringing the "character" to life(instantiating)
cal1 = Calculator()
cal1.divide(3, 1)

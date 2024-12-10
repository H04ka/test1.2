class Calculation():

    def sum(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def find_playndrome(self, arg: input) -> str:
        arg= input() 
        return arg == arg[::-1]   

class Text_Greeting():

    def greeting(self, name):
        return f"My name {name}"
    
    def empty_string(self, arg):
        return len(arg) > 0
    
    def register_check(self, arg):
        return arg.lower
    
    def long_check(self, arg):
        return len(arg) < 10
    
    def string_type(self,arg):
        return str(arg)
            
    
        
        

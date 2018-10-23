class Operator:
    def __init__(self, function = 0):
        self.function = function
        
    def set_function(self, function):
        self.function = function
        
    def perform(self, *arguments):
        return self.function(*arguments)
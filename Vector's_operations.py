class Vector:
    def __init__(self, args=[]):
        self.args = args

    def add(self, others):
        if len(self.args) != len(others.args):
            raise Exception('You can only add vectors of same dimension.')
        result = []
        for i in range(len(self.args)):
            result.append(self.args[i] + others.args[i])
        return result

    def subtract(self, others):
        if len(self.args) != len(others.args):
            raise Exception('You can only subtract vectors of same dimension.')
        result = []
        for i in range(len(self.args)):
            result.append(self.args[i] - others.args[i])
        return result
    
    def dot(self, others):
        if len(self.args) != len(others.args):
            raise Exception('You can only dot vectors of same dimension.')
        result = []
        for i in range(len(self.args)):
            result.append(self.args[i] * others.args[i])
        return result
    
    def norm(self):
        return (sum(self.args[i]**2 for i in range(len(self.args))))**0.5
            
    def toString(self):
        return '{}'.format(self.args)


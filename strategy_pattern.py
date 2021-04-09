class Strategy:
    def do_operation(self, num1: 'int', num2: 'int'):
        pass

class OperationAdd(Strategy):
    def do_operation(self, num1: 'int', num2: 'int'):
        return num1 + num2

class OperationSub(Strategy):
    def do_operation(self, num1: 'int', num2: 'int'):
        return num1 - num2

class OperationMul(Strategy):
    def do_operation(self, num1: 'int', num2: 'int'):
        return num1 * num2

class OperationDiv(Strategy):
    def do_operation(self, num1: 'int', num2: 'int'):
        return num1 / num2

class Context:
    def __init__(self, strategy: 'Strategy'):
        self.strategy = strategy

    def execute_strategy(self, num1: 'int', num2: 'int'):
        return self.strategy.do_operation(num1, num2)

context = Context(OperationAdd())
print('10 + 5 = '+str(context.execute_strategy(10, 5)))
context = Context(OperationSub())
print('10 - 5 = '+str(context.execute_strategy(10, 5)))


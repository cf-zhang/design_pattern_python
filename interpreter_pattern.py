class Expression:
    def interpret(self, context: 'str'):
        pass

class TerminalExpression(Expression):
    def __init__(self, data: 'str'):
        self.data = data

    def interpret(self, context: 'str'):
        return context.__contains__(self.data)

class OrExpression(Expression):
    def __init__(self, expr1: 'Expression', expr2: 'Expression'):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: 'str'):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

class AndExpression(Expression):
    def __init__(self, expr1: 'Expression', expr2: 'Expression'):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: 'str'):
        return self.expr1.interpret(context) and self.expr2.interpret(context)


robert = TerminalExpression('Robert')
john = TerminalExpression('John')
isMale = OrExpression(robert, john)

julie = TerminalExpression('Julie')
married = TerminalExpression('Married')
isMarriedWoman = AndExpression(julie, married)

print('John is male? '+str(isMale.interpret('John')))
print('Julie is a married women? '+str(isMarriedWoman.interpret('Married Julie')))




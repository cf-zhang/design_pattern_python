from abc import abstractmethod, ABCMeta
class ComputerPartVisitor(metaclass=ABCMeta):
    def visit(self, computer: 'Computer'):
        pass

    def visit(self, mouse: 'Mouse'):
        pass

    def visit(self, keyboart: 'KeyBoard'):
        pass

    def visit(self, monitor: 'Monitor'):
        pass


class ComputerPart(metaclass=ABCMeta):
    def accept(self, computer_part_visitor: ComputerPartVisitor):
        pass


class KeyBoard(ComputerPart):
    def accept(self, computer_part_visitor: ComputerPartVisitor):
        computer_part_visitor.visit4(self)


class Monitor(ComputerPart):
    def accept(self, computer_part_visitor: ComputerPartVisitor):
        computer_part_visitor.visit5(self)


class Mouse(ComputerPart):
    def accept(self, computer_part_visitor: ComputerPartVisitor):
        computer_part_visitor.visit2(self)


class Computer(ComputerPart):
    def __init__(self):
        self.parts = [Mouse(), KeyBoard(), Monitor()]

    def accept(self, computer_part_visitor: ComputerPartVisitor):
        for part in self.parts:
            part.accept(computer_part_visitor)
        computer_part_visitor.visit1(self)


class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit1(self, computer: 'Computer'):
        print('displaying computer')

    def visit2(self, mouse: 'Mouse'):
        print('dispalying mouse')

    def visit4(self, keyboart: 'KeyBoard'):
        print('displaying keyboard')

    def visit5(self, monitor: 'Monitor'):
        print('displaying monitor')


computer = Computer()
computer.accept(ComputerPartDisplayVisitor())

class Employee:
    def __init__(self, name: 'str', dept: 'str', sal: 'int'):
        self._name = name
        self._dept = dept
        self._sal = sal
        self.sub_ordinates = list()

    def add(self, employee: 'Employee'):
        self.sub_ordinates.append(employee)

    def remove(self, employee: 'Employee'):
        self.sub_ordinates.remove(employee)

    def get_sub_ordinates(self):
        return self.sub_ordinates

    def __str__(self):
        return "Employee: [" + self._name + ', ' + self._dept + ', ' + str(self._sal) + ']'


CEO = Employee("John", "CEO", 30000)
head1 = Employee("head1", "head1", 20000)
head2 = Employee("head2", "head2", 20000)
mao1 = Employee("mao1", "mao2", 10000)
mao2 = Employee("mao2", "mao2", 10000)
dao1 = Employee("dao1", "dao1", 10000)
dao2 = Employee("dao2", "dao2", 10000)

CEO.add(head2)
CEO.add(head1)
head2.add(dao2)
head2.add(dao1)
head1.add(mao2)
head1.add(mao1)

print(CEO)
for x in CEO.get_sub_ordinates():
    print(x)
    for y in x.get_sub_ordinates():
        print(y)



class Person:
    def __init__(self, name: 'str', gender: 'str', marital_status: 'str'):
        self._name = name
        self._gender = gender
        self._marital_status = marital_status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: 'str'):
        self._name = name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender: 'str'):
        self._gender = gender

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status: 'str'):
        self._marital_status = marital_status


class Criteria:
    def meet_criteria(self, persons: 'list'):
        pass


class CriteriaMale(Criteria):
    def meet_criteria(self, persons: 'list'):
        male_persons = list()
        for person in persons:
            if person.gender == "MALE":
                male_persons.append(person)
        return male_persons


class CriteriaFemale(Criteria):
    def meet_criteria(self, persons: 'list'):
        female_persons = list()
        for person in persons:
            if person.gender == "FEMALE":
                female_persons.append(person)
        return female_persons


class CriteriaSingle(Criteria):
    def meet_criteria(self, persons: 'list'):
        single_persons = list()
        for person in persons:
            if person.marital_status == "SINGLE":
                single_persons.append(person)
        return single_persons


class AndCriteria(Criteria):
    def __init__(self, criteria: 'Criteria', other_criteria: 'Criteria'):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet_criteria(self, persons: 'list'):
        first_criteria_persons = self.criteria.meet_criteria(persons)
        return self.other_criteria.meet_criteria(first_criteria_persons)


class OrCriteria(Criteria):
    def __init__(self, criteria: 'Criteria', other_criteria: 'Criteria'):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet_criteria(self, persons: 'list'):
        first_criteria_persons = self.criteria.meet_criteria(persons)
        second_criteria_person = self.other_criteria.meet_criteria(persons)
        for person in second_criteria_person:
            if person not in first_criteria_persons:
                first_criteria_persons.append(person)
        return first_criteria_persons


persons = list()
persons.append(Person("Robert", "MALE", "SINGLE"))
persons.append(Person("John", "MALE", "MARRIED"))
persons.append(Person("Laura", "FEMALE", "MARRIED"))
persons.append(Person("Diana", "FEMALE", "SINGLE"))
persons.append(Person("Mike", "MALE", "SINGLE"))
persons.append(Person("Bobby", "MALE", "SINGLE"))

critia_male = CriteriaMale()
critia_femal = CriteriaFemale()
critia_single = CriteriaSingle()
critia_single_male = AndCriteria(CriteriaMale(), CriteriaSingle())
critia_single_or_female = OrCriteria(CriteriaSingle(), CriteriaFemale())

for x in critia_single.meet_criteria(persons):
    print(x.name)
print()
for x in critia_femal.meet_criteria(persons):
    print(x.name)
print()
for x in critia_single_male.meet_criteria(persons):
    print(x.name)




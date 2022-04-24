class Employee:
    #name slaray bday id
    """
    this is a block comment
    represents an employee with a name, id, salary, birthday
    this is a docstring for a class and go under the definition
    """
    def __init__(self,id,name):
        """
        constructs an employee with name and id
        """
        self.id = int(id)
        self.name = name
        self.salary = 0
        self.birthday = ''

    def get_id(self):
        """gets employee id"""
        return self.id
    def set_id(self,id):
        self.id = id
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_salary(self):
        return self.salary
    def set_salary(self,salary):
        self.salary = salary
    def get_birthday(self):
        return self.birthday
    def set_birthday(self,birthday):
        self.__parse_birthday(birthday)

    def __parse_birthday(self,birthday):
        #1/1/2001
        #Jan 1, 2001
        if birthday.find('/') < 0:
            self.birthday = birthday
        else:
            month, day, year = birthday.split('/')


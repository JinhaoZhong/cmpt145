#Jinhao Zhong, 11204178, CMPT145, lab05

class Case(object):
    def __init__(self, name, crime, defence, prosecutor, judge, description):
        self.__name = name
        self.__crime = crime
        self.__defence = defence
        self.__prosecutor = prosecutor
        self.__judge = judge
        self.description = description


class Person(object):
    def __init__(self, name, role, address, clearance):
        self.name = name
        self.role = role
        self.__address = address
        self.__clearance = clearance


    def getClearance(self):
        return self.__clearance


class Evidence(object):
    def __init__(self, name, presenter, description):
        self.__name = name
        self.__presenter = presenter
        self.__description = description


    def Evidence_Info(self, viewer):
        if self.__presenter.getClearance() <= viewer.getClearance():
            return {self.__name},"presented by" ,{self.__presenter} ,{self.__description}


        elif viewer is not 'Judge':
            return "coffee_cup MUST BE admitted filed by judge"
        else:
            return ""

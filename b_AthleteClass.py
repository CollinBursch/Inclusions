class Athlete:
    def __init__(self, ht, wt, bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf


class Football_Player(Athlete):
    def __init__(self, ht, wt, bodyfat, position, team):

        Athlete.__init__(self, ht, wt, bodyfat)  # this creates the other

        self.__position = (
            position  # other attributes recorded to the football plater superclass
        )
        self.__team = team

    def get_position(self):  # don't need to define things lready defined in superclass
        return self.__position

    def get_team(self):
        return self.__team

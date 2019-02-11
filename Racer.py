class Racer:
    def __init__(self, full_name, year_of_birth, gender, category, country, code, start_number, position, times,
                 points):
        self.surname, self.name = full_name.split(" ", 1)

        self.year_of_birth = year_of_birth
        self.code = code
        self.gender = gender
        self.category = category
        self.country = country
        self.start_number = start_number
        self.position = position
        self.times = times
        self.points_earned = points

        self._DNF = False
        self._DNS = False
        self._DSQ = False

        # self.total_number_of_points += points

    @property
    def full_name(self):
        return self.name + " " + self.surname

    @property
    def DNF(self):
        return self._DNF

    @DNF.setter
    def DNF(self, value):
        self._DNF = value

    @property
    def DNS(self):
        return self._DNS

    @DNS.setter
    def DNS(self, value):
        self._DNS = value

    @property
    def DSQ(self):
        return self._DSQ

    @DSQ.setter
    def DSQ(self, value):
        self._DSQ = value

# test = Racer("Domminik", "Bullo", "09.12.1996", "m", "kategória", "SVK")

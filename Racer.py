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

        self._without_time = False
        self._additional_info = ""
        # self.total_number_of_points += points

    @property
    def full_name(self):
        return self.name + " " + self.surname

    @property
    def without_time(self):
        return self._without_time

    @without_time.setter
    def without_time(self, value):
        self._without_time = value

    @property
    def additional_info(self):
        return self._additional_info

    @additional_info.setter
    def additional_info(self, value):
        self._additional_info = value

# test = Racer("Domminik", "Bullo", "09.12.1996", "m", "kategória", "SVK")

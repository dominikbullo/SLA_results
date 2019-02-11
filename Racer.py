class Racer:
    def __init__(self, full_name, year_of_birth, gender, category, country):
        self.surname, self.name = full_name.split(" ", 1)

        self.year_of_birth = year_of_birth
        self.gender = gender
        self.category = category
        self.country = country

        self.start_number = None
        self.code = None
        self.position = None
        self.times = None
        self.points_earned = 0

        self.my_racer = False

        self._without_time = False
        self._additional_info = ""
        # self.total_number_of_points += points

    def __str__(self):
        if self._without_time:
            return self.full_name + " -> " + str(self._additional_info)
        else:
            return self.full_name + " -> " + str(self.position)

    @property
    def full_name(self):
        return self.surname.capitalize() + " " + self.name.capitalize()

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

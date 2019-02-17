class Racer:
    def __init__(self, full_name, year_of_birth, gender, category, country):
        self.surname, self.name = full_name.split(" ", 1)

        self.year_of_birth = year_of_birth
        self.gender = gender
        self.category = category
        self.country = country
        self.sci_club = None

        self.start_number = None
        self.code = None
        self.position = None
        self.position_in_year = None
        self.times = None
        self.points_earned = 0

        self.my_racer = False
        self.link_to_summary_page = None

        self.without_time = False
        self.additional_info = None
        # self.total_number_of_points += points

    def __str__(self):
        if self.without_time:
            return self.full_name + " -> " + str(self.additional_info)
        else:
            return self.full_name + " -> " + str(self.position)

    @property
    def full_name(self):
        return self.surname.capitalize() + " " + self.name.capitalize()

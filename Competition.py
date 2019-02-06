class Competition:
    def __init__(self, link, place):
        self.competition_link = link
        self.place = place
        self.results_list = []
        self.date = None

    def set_date(self, date):
        self.date = date

    class Result:
        def __init__(self, link, date, category, gender, discipline):
            # TODO: if date is None -> check if every date is equal
            Competition.set_date(Competition, date)

            self.date = date
            self.result_link = link
            self.category = category
            self.gender = gender
            self.discipline = discipline

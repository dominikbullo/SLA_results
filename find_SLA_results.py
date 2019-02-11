#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from Competition import Competition
from Racer import Racer


class ResultsFinder:
    def __init__(self, competitions_links_list, racer_list):
        self.competitions_links_list = competitions_links_list
        self.racer_list = racer_list
        self.competition_list = []

        # for item in racers_list:
        #     item[0] = item[0].lower()

        # add_dates_to_categories()

    def create_competitions_list_with_results(self):
        for competition_link in self.competitions_links_list:
            # for every competition create class Competition
            soup = BeautifulSoup(requests.get(competition_link).content, "lxml")
            competition_class = Competition(link=competition_link)

            for link in soup.findAll('a', href=True, title='Výsledky'):
                # for every class Competition add class Result
                # autofill every detail about competition and result

                # competition.results_list.append(competition.Result(
                #     link='http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/' + link['href']))

                ###########
                # TESTING #
                ###########
                print(f'Printing result for race with {link["href"]}')
                # TODO: this overwriting every place and date
                result = competition_class.Result(
                    link='http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/' + link['href'])

                # TODO: fill results for my child immediately when searching for every result
                competition_class.results_list.append(result)
                competition_class.date = result.date
                competition_class.place = result.place
                result.create_racer_list_with_results(self.racer_list)

            self.competition_list.append(competition_class)

    def print_results_list(self):
        print("Results list:")
        for competition in self.competition_list:
            print([(competition.place, competition.date, x.category, x.discipline) for x in competition.results_list])


def create_racers_list():
    racer_list_temp = [Racer("Dominik Bullo", '2010', "muži", "Mladšie predžiactvo", "SVK"),
                       Racer("Dominik Bullo1", '2010', "muži", "Mladšie predžiactvo", "SVK"),
                       Racer("Dominik Bullo2", '2010', "muži", "Mladšie predžiactvo", "SVK"),
                       Racer("Dominik Bullo3", '2010', "muži", "Mladšie predžiactvo", "SVK"),
                       Racer("Dominik Bullo4", '2010', "muži", "Mladšie predžiactvo", "SVK")]
    return racer_list_temp


def find_competitions_links(start_number, number_of_rounds):
    competitions_links_list = []
    link = "http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$"
    for x in range(start_number, start_number + number_of_rounds):
        competitions_links_list.append(link + str(x) + ".html")
    return competitions_links_list


if __name__ == "__main__":
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$651.html
    # to
    # 650+8
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$658.html

    # competitions "žiaci" starts from
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$645.html
    # to
    # 644 + 6
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$650.html
    categories = {
        "Predžiaci": find_competitions_links(651, 8),
        # "Žiaci": find_competitions_links(645, 6)
    }

    my_racers_to_find_list = create_racers_list()

    for competition_links in categories.values():
        print('Zoznam podujatí:', *competition_links, sep='\n- ')
        finder = ResultsFinder(competition_links, my_racers_to_find_list)
        finder.create_competitions_list_with_results()
        finder.print_results_list()

        # finder.write_results_into_excel()

        # TODO: find racers by ski club

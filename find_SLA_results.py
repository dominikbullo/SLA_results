#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from Competition import Competition
from Racer import Racer

from local_settings import *


class ResultsFinder:
    def __init__(self, competitions_links_list, racer_list):
        self.competitions_links_list = competitions_links_list
        self.racer_list = racer_list
        self.competition_list = []

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
                # print(f'Printing result for race with {link["href"]}')

                result = competition_class.Result(
                    link='http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/' + link['href'])

                # TODO: fill results for my child immediately when searching for every result
                competition_class.results_list.append(result)
                competition_class.date = result.date
                competition_class.place = result.place
                # print(f'Printing result for race on {result.date} in {result.place} for category {result.category}')
                result.create_racer_list_with_results(self.racer_list)

            self.competition_list.append(competition_class)

    def print_results_list(self):
        # print("Results list:")
        # for competition in self.competition_list:
        #     print(competition)
        # print([(competition.place, competition.date, x.category, x.discipline) for x in competition.results_list])
        pass


def create_racers_list():
    def create_and_add_categories():
        global MP, SP, MZ, SZ, racer
        # TODO: ask for correction date
        MP = datetime.now().year - 8
        SP = MP - 3
        MZ = SP - 2
        SZ = MZ - 2
        for i, racer in enumerate(racers):
            if datetime.strptime(racers[i][1], '%Y').year <= datetime(SZ, 1, 1).year:
                racer.append("Staršie žiactvo")
                # print("SZ")
            elif datetime.strptime(racers[i][1], '%Y').year <= datetime(MZ, 1, 1).year:
                racer.append("Mladšie žiactvo")
                # print("MZ")
            elif datetime.strptime(racers[i][1], '%Y').year <= datetime(SP, 1, 1).year:
                racer.append("Staršie predžiactvo")
                # print("SP")
            elif datetime.strptime(racers[i][1], '%Y').year <= datetime(MP, 1, 1).year:
                racer.append("Mladšie predžiactvo")
                # print("MP")
            elif datetime.strptime(racers[i][1], '%Y').year >= datetime(MP, 1, 1).year:
                racer.append("Superbejby")
                # print("SB")
            else:
                print("Neviem rozpoznať dátum")

    create_and_add_categories()
    my_racers_list = []
    for racer in racers:
        my_racers_list.append(Racer(full_name=racer[0],
                                    year_of_birth=racer[1],
                                    country="SVK",
                                    category=racer[3],
                                    gender=racer[2]))

    print('Zoznam pretekárov:', *[[x.full_name, x.category] for x in my_racers_list], sep='\n- ')

    return my_racers_list


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

# SLA_results
Simple program that search for result of my racers on page http://slovak-ski.sk.
This repo is for my personal and school project, it is not coded for someone else...yet.

Project is under developments...currently stopped, 
because i have a lot of programming into school but I will look at this program as soon as i can.
I think it will be after winter season about 04/2019

## Requirements
* Python v3.7 or greater
* pip v18 or greater
* pipenv tool
  
## Getting started

Use the new tool [pipenv](https://pipenv.readthedocs.io/en/latest/) to virtual environment and also packages.
If you don't have pipenv just type
```bash
pip install -U pipenv
 ```
### Copy project from my repo
```bash
git clone https://github.com/dominikbullo/SLA_results.git && cd SLA_results
```

### Parameters
You could run thi program with multiple parameters, which you can see down bellow or in help.

Short        | Long             | Description
------------ | ---------------- | -------------
-sc          | --ski_club_name  | Argument for full ski club name, for searching result for racers from this club. Only searching for racers who has at least 1 point because cannot access to all racers data by club
-cb          | --combine_search | If you want to find racers by club, and add some racers from file at the same time. It removes duplicates automatically
-rl          | --by_racers_list | If you want to specify list of racers, e.g. from multiple clubs_list, or compare specific people on one place


## Examples:
* **Club names are from this sites**: 
[Predžiaci](http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$17.html)
[Žiaci](http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$18.html)

* Find results for club AC UNIZA Žilina
    * `pipenv run python ResultFinder.py -sc "AC UNIZA Žilina"`
    * long:  `pipenv run python ResultFinder.py --ski_club_name "AC UNIZA Žilina"`
   
* Find results for club AC UNIZA Žilina combined with custom racers list txt file
    * `pipenv run python ResultFinder.py -sc "AC UNIZA Žilina" -cb`
    * long: `pipenv run python ResultFinder.py --ski_club_name "AC UNIZA Žilina" -combine_search`
    
* You could also find results for multiple clubs in the same time
    * `pipenv run python ResultFinder.py -sc "AC UNIZA Žilina","LK Valčianska Dolina"

* Find results for specific people just from txt file
    * `pipenv run python ResultFinder.py -rl`
    * long: `pipenv run python ResultFinder.py --by_racers_list`

### Start the script
Finally start the script with command:
```bash
pipenv run python ResultFinder.py
```

## Crete list of racers (optional)
In file **racers_to_find_list.txt** of racer which you want to find.

##### ONE RACER PER ONE LINE!
Fill information about racers in this order:
> SURNAME NAME, YEAR OF BIRTH, GENDER

* SURNAME NAME
  * Fill surname first then first name
* YEAR OF BIRTH
  * Year of birth of racer
* SURNAME NAME
  * M for Man, L for Ladies

Example of **racers_to_find_list.txt**:
```bash
Bullo Dominik, 1996, M
Bullo Dominik, 2001, L
```

## TODO
- [x] find results from page and store then into Objects
- [x] print the results to the console
- [ ] calculate statistics in round/year and so on...
- [ ] write results into Excel
- [ ] speed up → better finding system 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/#)

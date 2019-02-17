# SLA_results
Simple program that search for result of my racers on page http://slovak-ski.sk.
This repo is for my personal and school project, it is not coded for someone else...yet.

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



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/#)
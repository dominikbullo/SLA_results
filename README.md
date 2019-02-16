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
pip install pipenv
 ```
Then copy project from my repo
```bash
git clone https://github.com/dominikbullo/SLA_results.git && cd SLA_results

pipenv run python find_SLA_results.py
```
Crete list of racer which you want to find.
Example:
```bash
racers = (["Bullo Dominik", '1996', 'muži'],
          ["Bullo Dominik", '2006', 'muži'])
```

* racers[0][0] = surname and name of racer
* racers[0][1] = year of birth
* racers[0][2] = gender (man=muži/woman=ženy)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/#)
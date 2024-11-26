'''4. Create an array with 5 dictionaries, each containing a country and its population. Then, print the array contents. Sample result:

   ```
   COUNTRY  POPULATION
   Poland   38000000
   …        …
   …        …
   …        …
   …        …'''

countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Canada", "population":3809897987000},
    {"name":"Chile", "population":382342400},
    {"name":"Argentina", "population":234243200000},
    {"name":"Brazil", "population":234243000000},
   ]

for i in countries:
    for key, values in i.items():
        print(values)
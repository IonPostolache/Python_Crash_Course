cities={
    'shanghai':{
        'country':'china',
        'population':26317104,
        'fact':'one of the fastest developing for 20 years'
        },
    'delhi':{
        'country':'india',
        'population':29399141,
        'fact':'first in air pollution'
        },
    'tokyo':{
        'country':'japan',
        'population':37435191,
        'fact':'population drop of 0.09 percent in 2019'
        },
    }

for a, b in cities.items():
    print(f"{a.title()}:")
    for c,d in b.items():
        print(f"\t{c.title()}: {d}.")

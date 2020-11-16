#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys


path = 'titanic.csv'

titanic = pd.read_csv(path)

males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()

proportions = [males, females]

a = titanic.Fare<=200
b = titanic.Fare>20

Passeger_200 = titanic[titanic.Fare>200] 
Passeger_200_num = Passeger_200.sum()
Passeger_200_passenger = (Passeger_200['Sex'] == 'male').sum() + (Passeger_200['Sex'] == 'female').sum()

Passeger_20 = titanic[titanic.Fare<=20] 
Passeger_20_num = Passeger_20.sum()
Passeger_20_passenger = (Passeger_20['Sex'] == 'male').sum() + (Passeger_20['Sex'] == 'female').sum()

Passeger_other = titanic[a & b] 
Passeger_other_num = Passeger_other.sum()
Passeger_other_passenger = (Passeger_other['Sex'] == 'male').sum() + (Passeger_other['Sex'] == 'female').sum()

x =[{'Fare<20':Passeger_20_passenger,'20>=Fare<200':Passeger_other_passenger,'Fare>=200':Passeger_20_passenger},{'Fare<20':Passeger_20_num.loc['Survived'], '20>=Fare<200':Passeger_other_num.loc['Survived'],'Fare>=200':Passeger_200_num.loc['Survived']}]



plt.pie(
    proportions,
    labels = ['Males', 'Females'],
    shadow = False,
    colors = ['blue','red'],
    explode = (0.15 , 0),
    startangle = 90,
    autopct = '%1.1f%%'
    )

plt.axis('equal')
plt.title("Sex Proportion")
plt.tight_layout()



arg_no = str(sys.argv[1])

if arg_no == '-1':
    print(pd.DataFrame(x, index = ['登船人數', '生還人數']))
            
elif arg_no == '-2':
    plt.show()
                


# In[ ]:





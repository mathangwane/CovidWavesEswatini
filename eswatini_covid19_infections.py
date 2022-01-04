import pandas as pd 
from matplotlib import pyplot as plt

plt.xkcd()
plt.style.use('seaborn')

data = pd.read_csv('data/wave1.csv')
data2 = pd.read_csv('data/wave2.csv')
data3 = pd.read_csv('data/wave3.csv')
data4 = pd.read_csv('data/wave4.csv')

Infection_Day = data['Day']
Infection_Number = data['Infections']

Infection_Day2 = data2['Day']
Infection_Number2 = data2['Infections']

Infection_Day3 = data3['Day']
Infection_Number3 = data3['Infections']

Infection_Day4 = data4['Day']
Infection_Number4 = data4['Infections']

plt.plot(Infection_Day, Infection_Number, marker=None, linestyle='solid')
plt.plot(Infection_Day2, Infection_Number2, marker=None, linestyle='solid')
plt.plot(Infection_Day3, Infection_Number3, marker=None, linestyle='solid')
plt.plot(Infection_Day4, Infection_Number4, marker=None, linestyle='solid')

plt.title('Covid Waves in Eswatini \n (Data Source: Government of Eswatini)')
plt.xlabel('Number of Days Since Start of Wave \n Graphic by Mathangwane (github.com/mathangwane/eswatinicovidstats)')
plt.ylabel('Confirmed Infections (7-Day Moving Average)')

plt.tight_layout()

plt.legend(["First Wave", "Second Wave", "Third Wave", "Fourth Wave"])

plt.show()
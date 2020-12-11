import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
import seaborn as sb

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countriesaggregated.csv'
df = pd.read_csv("covid_dataset.csv")
#print(df.head(3))  # get first 3 entries in df
#print(df.tail(3))   # get last 3 entries in df


# india

df_india = df[df['Country'] == 'India']
#print(df_india.head(5))
plt.bar(x='Date', height = 'Confirmed', color ='red', data=df_india ) #bar graph
#plt.plot('Date','Confirmed', color ='red', data=df_india )#linegraph
plt.xlabel("DATE")
plt.ylabel("Total No. Confirmed Of Cases")
plt.title("INDIA")
plt.show()



# itlay
df_italy = df[df['Country'] == 'Italy']
#print(df_italy.head(10))
#plt.plot('Date','Confirmed', color ='blue', data=df_italy)
plt.bar('Date','Confirmed', color ='blue', data=df_italy)
plt.xlabel("DATE")
plt.ylabel("Total No. Confirmed Of Cases")
plt.title("ITALY")
plt.show()


#china

df_china = df[df['Country'] == 'China']
#print(df_china.head(10))
#plt.plot('Date','Confirmed', color ='orange', data=df_china)
plt.bar('Date','Confirmed', color ='orange', data=df_china)
plt.xlabel("DATE")
plt.ylabel("Total No. Confirmed Of Cases")
plt.title("CHINA")
plt.show()


#more than on country

df5 = df.query('Country in ["India", "China", "US"]')
#print(df5)
#sb.stripplot(x='Date', y='Deaths', hue='Country',data=df5)
#plt.show()



#ANIMATION for 5 country

list_dates = df['Date'].unique()
fig, ax = plt.subplots(figsize=(15, 8))
# We will animate for these 5 countries only
list_countries = ['India', 'China', 'US', 'Italy', 'Spain']
# colors for the 5 horizontal bars
list_colors = ['black', 'red', 'green', 'blue', 'yellow']

def plot_bar(some_date):
        df2 = df[df['Date'].eq(some_date)]
        ax.clear()
        #death column only
        df3 = df2.sort_values(by = 'Deaths', ascending = False)
        df4 = df3[df3['Country'].isin(list_countries)]
        sleep(0.2) # To slow down the animation
        # makes a horizontal bar plot.
        return ax.barh(df4['Country'], df4['Deaths'],color= list_colors)


my_anim = animation.FuncAnimation(fig = fig,func = plot_bar,
                                  frames= list_dates, blit=True,interval=20)

plt.xlabel("RATE OF DEATHS")
plt.title("COVID WITH DATA VISUALIZATION")
plt.show()


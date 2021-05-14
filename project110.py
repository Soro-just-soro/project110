import random
import scipy
import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics as S
import plotly.graph_objects as go
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
dataSet=[]
def RS(counter):
    for i in range(100):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=S.mean(dataSet)
    return mean
def Showfig(meanlist):
    df=meanlist
    mean=S.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def main():
    meanlist=[]
    for e in range(1000):
        setOfMeans=RS(100)
        meanlist.append(setOfMeans)
    Showfig(meanlist)
    mean=S.mean(meanlist)
main()
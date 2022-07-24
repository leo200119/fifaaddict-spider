import pandas as pd
import csv

def onename():
    l = list()
    with open('a.csv','r',encoding='utf-8') as read:
        reader = csv.reader(read)
        for i in reader:
            l.append(i)
    df = pd.DataFrame(l)
    # df1 = df['name']
    # df1.drop_duplicates(subset=3,inplace=True)
    df.drop_duplicates(subset=0,keep='first',inplace=True)
    df.to_csv('b.csv',header=False,encoding ='utf-8',index=False)
    return
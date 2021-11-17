import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{
        'x': coffee,
        'y': sleep,
    }

def find_correlation(data):
    c = np.corrcoef(data['x'], data['y'])
    print(c[0,1])

def plotFigure(data):
    fig = px.scatter(x=data['x'], y=data['y'])
    fig.show()

def main():
    data_path = 'data.csv'
    data = getDataSource(data_path)
    find_correlation(data)
    plotFigure(data)

if __name__ == '__main__':
    main()

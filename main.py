import numpy as np
import math as m
from openpyxl import load_workbook
import matplotlib.pyplot as plt


def Y(x):
    y=np.zeros(len(x))
    for i in range(len(x)):
        h = np.random.normal(1, 0.05, 1)[0]
        y[i]=(m.sin(x[i]) + x[i]/10 + 50/(m.log(x[i]+10))) * h
    return y


def K(z):
    if abs(z)<=1:
        k = 0.75*(1-z**2)
    else:
        k=0
    return k


def Ksum(z0, z, n):
    sum=0
    hn = H(n)
    for i in range (len(z)):
        sum+=K((z0-z[i])/hn)
    return sum


def H(n):
    c=52
    h=c*n**(-1/5)
    return h


def M(x0, x, y, n):
    sum = 0
    ksum = Ksum(x0, x, n)
    hn = H(n)
    for i in range(len(x)):
        sum += (K((x0-x[i])/hn))/ksum*y[i]
    return sum


def delete(j, x, n):
    xwithoutj = np.zeros(n-1)
    for i in range (j):
       xwithoutj[i] = x[i]
    for i in range (j, len(x)-1):
        xwithoutj[i] = x[i+1]
    return xwithoutj


if __name__ == '__main__':
    n=1000
    x = np.zeros(n)
    for i in range(1,n+1):
        x[i-1]=i*0.1
    y=Y(x)
    #print("y = ", y)
    plt.plot(x,y)
    #plt.show()
    ypredict = np.zeros(n)
    E = np.zeros(n)
    """for j in range(n):
        x0=x[j]
        xwithoutj = delete(j, x, n)
        y0=y[j]
        ywithoutj = delete(j, y, n)
        ypredict[j] = M(x0, xwithoutj, ywithoutj, n)
        E[j] = (ypredict[j]-y0)**2
    plt.plot(x,ypredict)
    plt.show()
    print(sum(E))"""

    n2=200
    square=np.zeros(n2)
    price = np.zeros(n2)
    i=0
    wb = load_workbook('./selection.xlsx')
    sheet = wb['cian_parsing_result_sale_1_10_k']
    for cellObj in sheet['I2':'I201']:
        for cell in cellObj:
            square[i] = cell.value
            i+=1
    print(square)
    i=0
    for cellObj in sheet['J2':'J201']:
        for cell in cellObj:
            price[i] = cell.value
            i+=1
    print(price)

    plt.plot(square, price)
    #plt.show()
    ypredict2 = np.zeros(n2)
    E2 = np.zeros(n2)
    for j in range(n2):
        x0=square[j]
        squarewithoutj = delete(j, square, n2)
        y0=price[j]
        pricewithoutj = delete(j, price, n2)
        ypredict2[j] = M(x0, squarewithoutj, pricewithoutj, n2)
        E2[j] = (ypredict2[j]-y0)**2
    plt.plot(square,ypredict2)
    plt.show()
    print(sum(E2))

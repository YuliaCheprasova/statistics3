import numpy as np
import math as m


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
    for i in range (len(z)):
        sum+=K((z0-z[i])/H(n))
    return sum


def H(n):
    c=1
    h=c*n**(-1/5)
    return h


def M(x0, x, y, n):
    sum = 0
    for i in range(len(x)):
        sum += K((x0-x[i])/H(n))/Ksum(x0, x, n)*y[i]
    return sum


def delete(j, x):
    xwithoutj = np.zeros(99)
    for i in range (j):
       xwithoutj[i] = x[i]
    for i in range (j+1, len(x)-1):
        xwithoutj[i] = x[i-1]
    return xwithoutj


if __name__ == '__main__':
    n=100
    x = np.zeros(100)
    for i in range(1,101):
        x[i-1]=i
    y=Y(x)
    print("y = ", y)
    j=55
    x0=x[j]
    xwithoutj = delete(j, x)
    y0=y[j]
    ywithoutj = delete(j, y)
    R = M(x0, xwithoutj, ywithoutj, n)
    print(R)

# правильно ли я понимаю что нужно исключить каждую из точек
# и посчитать среднеквадратическую ошибку, а потом сложить эти ошибки?
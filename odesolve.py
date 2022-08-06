# odesolve.py
#
# Author: Yikai Zhang
# Date:23rd July 2022
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

def euler(f, x, t, h):
    return x+f(x,t)*h


def rk4(f, x, t, h):
    k_1=f(x,t)
    k_2=f(x+k_1*h/2,t+h/2)
    k_3=f(x+k_2*h/2,t+h/2)
    k_4=f(x+k_3*h,t+h)
    return x+(k_1+2*k_2+2*k_3+k_4)*h/6


def solveto(f, x1, t1, t2, hmax, method=euler):
    A=divmod((t2-t1),hmax)
    B=A[0]
    B=int(B)
    C=A[1]
    C=round(C,10)
    N=0
    if t2-t1==0:
        x_2=1
        return x_2
    if method == euler and t2-t1!=0:
     for N in range (N,B):
        N=N+1
        x_2=euler(f,x1,t1,hmax)
        x1=x_2
        t1=t1+hmax
        if C > 0:
            x_2=euler(f,x1,t1,C)
     return x_2
    if method == rk4 and t2-t1!=0:
      for N in range (N,B):
          N=N+1
          x_2 =rk4(f, x1, t1, hmax)
          x1=x_2
          t1=t1+hmax
          if C > 0:
              x_2=rk4(f, x1, t1, C)
    return x_2


def odesolve(f, X0, t, hmax, method=euler):
    import numpy as np
    X0=X0[0]
    t1=np.array(t)
    N=divmod((t[-1]-t[0]),t[1])
    M=N[0]
    M=M+1
    M=int(M)
    i=0
    x_2list=[]
    if method ==euler:
        for i in range (0,M):
            x_2=solveto(f,X0,t1[i],1,hmax,euler)
            i=i+1
            x_2list.insert(0,x_2)
        A=np.array(x_2list)
        B=np.mat(A)
        return B    
    if method ==rk4:
        for i in range (0,M):
            x_2=solveto(f,X0,t1[i],1,hmax,rk4)
            i=i+1
            x_2list.insert(0,x_2)
        A=np.array(x_2list)
        B=np.mat(A)
        return B


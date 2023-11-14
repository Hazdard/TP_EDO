# from package import * EST INTERDIT
# Sauf mention du contraire, il est inutile de rajouter d'autres packages
import pylab as plt
import numpy as np
import numpy.random as rd
from scipy.integrate import odeint
from scipy.linalg import eig
from numpy import sin, cos
# taper ds le shell "cd le nom du répertoire" où se trouve le fichier edoenv
# OU
# ouvrir File Browse ds Tools
# selectionner le répertoire où se trouve edoenv.py
# et ds l'étoile cliquer "Go to the directory in the current shell"
# OU
# ouvrir explorateur de fichiers ds Outils
# selectionner le répertoire où se trouve edoenv.py
# et ds l'étoile cliquer "Aller ds ce dossier (shell courant)"
from edoenv import envpp

plt.ion()  # interactive on
plt.show() # affiche les figures

eps=0.5
a1=lambda t : 2+eps*sin(t)
b1=lambda t : 2-eps*sin(t)+eps**2*sin(t)**2
a2=lambda t : 1+(1+eps*sin(t))*(1+eps*sin(t)+eps*cos(t))
b2=lambda t : 1+(1-eps*sin(t))*(1-eps*sin(t)-eps*cos(t))

CI=np.array([[0.01,0.1],[0.2,0.002],[1.0,1.0],[0.01,0.01]])
#Question 1

f=lambda y,t: np.array([a1(t)*y[0]*(1-y[0])-b1(t)*y[0]*y[1],a2(t)*y[1]*(1-y[1])-b2(t)*y[0]*y[1]])

xmin=0
xmax=1
ymin=0
ymax=1

ti=0
tf=40
h=0.1
T=np.arange(ti,tf+h,h)

for y0 in CI :
        Sode=odeint(f,y0,T)
        plt.plot(Sode[:,0],Sode[:,1])

plt.axis([xmin,xmax,ymin,ymax])
plt.title("Comportement chaotique des solutions du système étudié")
plt.figure()

#Question 2
y0 = CI[3]
for i in range(len(T)):
    plt.clf()
    Sode=odeint(f,y0,np.arange(ti,T[i]+h,h))
    plt.plot(Sode[:,0],Sode[:,1])
    plt.scatter(Sode[i][0],Sode[i][1],s=100,color="purple",marker="x")
    envpp(lambda y,u:f(y,T[i]),xmin,xmax,ymin,ymax)
    plt.title("Temps t=%f"%T[i])
    plt.pause(0.001)
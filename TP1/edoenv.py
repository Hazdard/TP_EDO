# taper ds le shell cd le nom du répertoire où se trouve le fichier edoenv
# OU
# ouvrir File Browse ds Tools
# selectionner le répertoire où se trouve edoenv.py
# et ds l'étoile cliquer "Go to the directory in the current shell"
# OU
# ouvrir explorateur de fichiers ds Outils
# selectionner le répertoire où se trouve edoenv.py
# et ds l'étoile cliquer "Alller ds ce dossier (shell courant)"

# PUIS from edoenv import envpp

# Trace l'environnement du portrait de phase ; champs de vecteur et isoclines

def envpp(F,xmin,xmax,ymin,ymax,autonome=True) :

    from numpy import asarray,linspace,meshgrid,hypot,array
    from pylab import quiver,contour,text
    from warnings import filterwarnings


    # F(y,t) : fonction de R x R ds R
    # ou
    # F(y,t) : fonction de R  ds R

    if autonome :

        # CHAMPS DE VECTEUR

        x = linspace(xmin,xmax,21)
        y = linspace(ymin,ymax,21)
        [X,Y] = meshgrid(x,y)
        [DX,DY]=F([X,Y],1.234) # autonome le temps est sans importance

        # Adimensionnement
        N=hypot(DX,DY)

        # Quiver
        # On adimensionne (et on ignore l'éventuel message d'erreur)

        filterwarnings('ignore')

        # On rajoute l'argument N pour des flèches colorées
        # Enfin angles='xy' : obligatoirement pour ne pas avoir de pb d'échelle

        quiver(X,Y,DX/N,DY/N,N,scale=20,angles='xy')#,color='r')

        #  ISOCLINES

        x = linspace(xmin-0.01,xmax+0.01,1201)
        y = linspace(ymin-0.01,ymax+0.01,1201)
        [X,Y] = meshgrid(x,y)
        # On raffine le maillage pour éviter les parasites et les coins anguleux
        # On etend un peu le domaine pour voir les axes (cf erreur arrondi)
        [DX,DY] = F([X,Y],0)

        # contour
        contour(X,Y,DX,[0.0],linewidths=2,colors='r')
        contour(X,Y,DY,[0.0],linewidths=2,colors='g')

        #text(xmax,ymax,"23/24")

    else :
        # fonction scalaire
        G = lambda y,t : array([1.0+0*y[0]+0*y[1],F(y[1],y[0])])

        # CHAMPS DE VECTEUR

        x = linspace(xmin,xmax,21)
        y = linspace(ymin,ymax,21)
        [X,Y] = meshgrid(x,y)
        [DX,DY]=G([X,Y],1.234) # autonome le temps est sans importance

        # Adimensionnement
        N=hypot(DX,DY)

        # Quiver
        # On adimensionne (et on ignore l'éventuel message d'erreur)

        filterwarnings('ignore')

        # On rajoute l'argument N pour des flèches colorées
        # Enfin angles='xy' : obligatoirement pour ne pas avoir de pb d'échelle

        quiver(X,Y,DX/N,DY/N,N,scale=20,angles='xy')#,color='r')

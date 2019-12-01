import nltk
import nltk.data
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt
import seaborn as sns
import cv2
x = cv2.__version__
from matplotlib import pyplot as plt


#para medir la similitud de algo 
#original van los autores
#predicho parrafo
#inf[tamaño,cantcomas,cantMexico]

#pendiente hacer mi vector 
def vectorize(texto):
    vector = []
    vector.append(len(texto)) #aqui es el vector con mis caracteristicas
    vector.append(texto.count(","))
    vector.append(texto.count("."))
    vector.append(texto.count(" "))
    vector.append(texto.count(" o "))
    return vector



def score(predicho,original):
    contador=0
    longitud=len(original)
    for i in range(longitud):
        if(original[i]==predicho[i]):
            contador=contador+1
            #print(longitud)
    resultado=contador/(len(original))
    return resultado

def clasificacion():
    df = pd.read_csv('author_corpus.txt',sep='\t',index_col=False,names=["autor","texto"])
    # Remueve autor 5, que es igual al 4
    df = df[:][df['autor']!=5]
    X_raw = df['texto']
    X_vectors = np.array([])
    for i in range(len(X_raw)):
        if len(X_vectors) == 0:
            X_vectors = vectorize(X_raw[:].iloc[i])
        else:
            X_vectors = np.vstack([X_vectors,vectorize(X_raw[:].iloc[i])])
    y = df['autor'].to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(X_vectors,y,test_size=0.3,random_state=101)
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    print('\nPrecision: {0}'.format(score(y_pred, y_test)))
    return X_vectors
    
    

original=[1,1,0,1]
predicho=[0,1,0,0]

puntuacionscore=score(original,predicho)
print(puntuacionscore)
vectorx=clasificacion()
print(vectorx)

datos = pd.DataFrame(vectorx)
ax = sns.scatterplot(x=0, y=1, hue=2,data =datos)
plt.show()

#datos = pd.DataFrame(vectorx)#fmri es un datase
a = sns.lineplot(x=0,y =1,data=datos)
#print(datos)

plt.show()


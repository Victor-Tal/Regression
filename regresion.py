#---------------------------------------
# Cordero Correa Victor Hugo
#----------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
frn  om sklearn.metrics import mean_squared_error, r2_score

#----------------------------------------
#Carga datos de prueba (diabetes)
#---------------------------------------
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

#-------------------------------------------
#Utilizar solo una parte de los datos 
#---------------------------------------------
diabetes_X = diabetes_X[:, np.newaxis, 2]

#------------------------------------------------
#Separar datos en conjunto de entrenamiento/prueba
#-----------------------------------------------------
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[:-20]

#-------------------------------------------------------
#Separar resultados en conjunto de entrenamiento/prueba
#--------------------------------------------------------
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[:-20]

#-------------------------------
#Crear objeto regresion lineal
#-------------------------------
regr_lin = linear_model.LinearRegression()

#-------------------------------
#Entrenar un modelo
#--------------------------------
regr_lin.fit(diabetes_X_train, diabetes_y_train)

#--------------
#Predicción
#---------------
diabetes_y_pred = regr_lin.predict(diabetes_X_test)

#------------------------
#Los coeficientes
#-------------------------
print("Coeficientes: \n", regr_lin.coef_)

#------------------------------
#Error medio al cuadrado
#------------------------------
print("Error medio al cuadrado :%.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

#------------------------------------------------------------
#Coeficiente de determinación : 1 es predicción perfecta
#------------------------------------------------------------
print("Coeficiente de determinación: %.2f" % r2_score(diabetes_y_test,diabetes_y_pred))

#----------
#Graficas
#------------
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
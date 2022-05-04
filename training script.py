import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv('CarPrice_Assignment.csv')
df = df.drop(['car_ID','symboling','carheight', 'CarName','compressionratio','peakrpm','stroke','fuelsystem','boreratio','citympg','highwaympg','carlength', 'carwidth', 'curbweight', 'enginesize',], axis=1)

df = pd.get_dummies(df, columns=['fueltype','aspiration', 'doornumber','drivewheel','enginelocation','carbody','enginetype','cylindernumber'], drop_first=True)

var_pred = df[[
        'horsepower','wheelbase',
        'fueltype_gas', 'aspiration_turbo', 'doornumber_two', 'drivewheel_fwd',
        'drivewheel_rwd', 'enginelocation_rear', 'carbody_hardtop',
        'carbody_hatchback', 'carbody_sedan', 'carbody_wagon',
        'enginetype_dohcv', 'enginetype_l', 'enginetype_ohc',
        'enginetype_ohcf', 'enginetype_ohcv', 'enginetype_rotor',
        'cylindernumber_five', 'cylindernumber_four', 'cylindernumber_six',
        'cylindernumber_three', 'cylindernumber_twelve', 'cylindernumber_two']]

var_res = df['price']
modelregrsilinier = LinearRegression()
modelregrsilinier.fit(var_pred,var_res)

pickle.dump(modelregrsilinier,open('saved model','wb'))
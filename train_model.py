import pandas as pd
from xgboost import XGBRegressor
import pickle

df=pd.read_csv("cars24-car-price-cleaned-new.csv")
X=df[['km_driven','mileage','age','Petrol','Diesel','Electric']]
y = df[['selling_price']]


xgbmodel=XGBRegressor(n_estimators=200
                    ,learning_rate=0.2,
                    max_depth=6)

xgbmodel.fit(X,y)

with open("xgb_car_price_model.pkl","wb") as f:
    pickle.dump(xgbmodel,f)
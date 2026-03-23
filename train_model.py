import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data={
    "experience" : [1,2,3,4,5],
    "salary": [2000,3000,4000,5000,6000]
}
df=pd.DataFrame(data)
x=df[["experience"]]
y=df[["salary"]]

model=LinearRegression()
model.fit(x,y)
pickle.dump(model,open('model.pkl','wb'))
print("model trained and saved")
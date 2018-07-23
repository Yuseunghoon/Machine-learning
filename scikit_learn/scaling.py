from sklearn.preprocessing import scale, minmax_scale, StandardScaler, MinMaxScaler
import pandas as pd
import numpy as np

stdscaler = StandardScaler()
minmax_scaler = MinMaxScaler()

input_data = (np.arange(5, dtype = np.float) -2).reshape(-1,1)
print(np.arange(5, dtype = np.float))
print(input_data)

# 평균 표준편차 스케일링
minmax_scale_data = minmax_scaler.fit_transform(input_data)
print('평균 :', minmax_scale_data.mean(axis=0))
print("표준편차 :", minmax_scale_data.std(axis=0))

df1 = pd.DataFrame(np.hstack([input_data, minmax_scale(input_data)]), columns =["input data", "minmax_scale"])
print(df1)


# 타켓(목표) -> 실측
t = [0,0,0,0,0,0,0,1,0,0]

# 예측 y -> 모델에서 출력된 데이터
y1=[0.1,0,0.1,0.05,0,0.05,0,0.7,0,0] # 7일 확률이 70%
y2=[0,0.1,0.7,0.05,0.05,0.1,0,0,0,0] # 2일 확률이 70%

import numpy as np

def mean_seq_err(t,y):
    return 0.5 * np.sum((t-y)**2)


print(mean_seq_err(np.array(t), np.array(y1)))

print(mean_seq_err(np.array(t), np.array(y2)))


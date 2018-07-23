import tensorflow as tf

x = [1,2,3]
y = [1,2,3]
#가중치
#균등분포로 랜덤하게 숫자를 만들기 위함
w = tf.Variable(tf.random_uniform([1], -1, 1)) #[] 자리수 맞게 -1 과 1 사이를 랜덤하게 추출
b = tf.Variable(tf.random_uniform([1], -1, 1))
x_test = [5, 7]
# hypothesis 설정
# hypothesis = tf.add(tf.multiply(x,w),b) 같은 의미
hypothesis = w * x +b
# 평균 제곱 오차를 구한다
cost = tf.reduce_mean((hypothesis - y) ** 2)
# 옵티마이저를 지정한다(학습방법을 지정한다)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
# 학습을 시킨다, cost의 오류률이 최소화되게
train = optimizer.minimize(loss = cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# epoch를 10번 수행
for i in range(100):
    sess.run(train)

print("w :", sess.run(w), "b :", sess.run(b), "cost :", sess.run(cost))

for i in range(len(x_test)):
    print("x = ",x_test[i], "predict :", sess.run(w * x_test[i]+b))

sess.close()



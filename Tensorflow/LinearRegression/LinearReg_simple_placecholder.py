import tensorflow as tf

xx= [1,2,3]
y = [1,2,3]

w = tf.Variable(tf.random_uniform([1],-1,1))
b = tf.Variable(tf.random_uniform([1],-1,1))

x= tf.placeholder(tf.float32)
x_test = [5,7]

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

for i in range(10):
    sess.run(train, feed_dict={x:xx})
    print(i, sess.run(cost, feed_dict={x:xx}))

for i in len(x_test):
    print("predict : ", w*x_test[i] + b)

sess.close()
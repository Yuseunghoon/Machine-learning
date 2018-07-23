import tensorflow as tf

x = [[1.,0.,3.,0.,5.], [0.,2.,0.,4.,0.]] # 공부 시간, 출석한 일수
y = [1.,2.,3.,4.,5.] # 시험점수

w = tf.Variable(tf.random_uniform([1, 2],-1,1)) # 가중치
b = tf.Variable(tf.random_uniform([1],-1,1)) # bias

# w (1 X 2)  x(2 X 5) -> 1 X 5
hypothesis = tf.matmul(w, x) + b

cost = tf.reduce_mean((hypothesis-y) ** 2)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)

train = optimizer.minimize(loss=cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    sess.run(train)
    print(i,sess.run(cost))

ww, bb = sess.run(w), sess.run(b)

print('ww :', ww, 'bb :',bb)
x_test = [0,4]
print("predict :", ww[0][0] * x_test[0] + ww[0][1] * x_test[1] + bb[0])

sess.close()

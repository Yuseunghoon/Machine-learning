import tensorflow as tf

x = [[1.,0.,3.,0.,5.], [0.,2.,0.,4.,0.]] # 공부 시간, 출석한 일수
y = [1.,2.,3.,4.,5.] # 시험점수

x.insert(0,[1.,1.,1.,1.,1.]) # 0번째에 리스트 삽입

w = tf.Variable(tf.random_uniform([1, 3],-1,1)) # 가중치


# w (1 X 3)  x(3 X 5) -> 1 X 5
hypothesis = tf.matmul(w, x)

cost = tf.reduce_mean((hypothesis-y) ** 2)

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)

train = optimizer.minimize(loss=cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    sess.run(train)
    print(i,sess.run(cost))

ww = sess.run(w)

print('ww :', ww)
x_test = [0,4]
print("predict :", ww[0][1] * x_test[0] + ww[0][2] * x_test[1] + ww[0][0])

sess.close()

import tensorflow as tf
import numpy as np

# 6 X 3
x = [[1.,1.,2.],
     [1.,2.,3.],
     [1.,2.,4.],
     [1.,5.,3.],
     [1.,7.,5.,],
     [1.,8.,4.,]]
# 6 X 1
y = [[0],[0],[0],[1],[1],[1]]

w = tf.Variable(tf.random_uniform([3, 1],-1,1))
# 브로드 케스팅 기능을 사용하기 위해 numpy 배열로 변경함
yy = np.array(y)
# z : 6 X 3. w : 3 X 1 -> 6 x 1
z = tf.matmul(x, w)
# 시그모이드 구하기
hypothesis = 1/ (1 +tf.exp(-z))

cost = tf.reduce_mean(yy * -tf.log(hypothesis) + (1-yy) * -tf.log(1-hypothesis))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train = optimizer.minimize(loss=cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(10):
    sess.run(train)
    print(i, sess.run(cost))

sess.close()

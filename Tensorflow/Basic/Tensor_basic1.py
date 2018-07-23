import tensorflow as tf

a = tf.constant(3)
b = tf.Variable(5)

add = tf.add(a,b)

print('a:', a, 'b:', b)

sess = tf.Session()

# 초기화 (전체 변수 초기화)
sess.run(tf.global_variables_initializer())

print('a :', sess.run(a))
print('b :', sess.run(b))
print('add :', sess.run(add))


sess.close()
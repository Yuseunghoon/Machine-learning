import tensorflow as tf

# 원하는 구구단을 입력 받아 구구단을 완성

def nine_1(dan):
    left = tf.placeholder(tf.float32)
    right = tf.placeholder(tf.float32)
    multiply = tf.multiply(left, right)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(1,10):
        result = sess.run(multiply, feed_dict={left:dan, right:i})
        print('{} X {} = {:2}' .format(dan, i, result))

    sess.close()

#nine_1(9)

# left를 인자로 받아 계산

def nine_2(dan):
    right = tf.placeholder(tf.int32)
    multply = tf.multiply(dan, right)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    for i in range(1, 10):
        result = sess.run(multply, feed_dict={right:i})
        print('{} X {} = {}' .format(dan, i, result))
    sess.close()

nine_2(9)
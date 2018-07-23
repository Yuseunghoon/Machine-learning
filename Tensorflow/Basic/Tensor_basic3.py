import tensorflow as tf

# 세션을 실행할때 순서에 따라 변수가 어떻게 변하는지 확인
value = tf.Variable(0)
one = tf.constant(1)

state = tf.add(value, one)
update = tf.assign(value, state)  # state 값을 value에 할당하고 할당된 값을 리턴하기 위한 함수


sess = tf.Session()
sess.run(tf.global_variables_initializer())

for _ in range(3):
    print("update :", sess.run(update),
          "state :", sess.run(state))

    #print("state :", sess.run(state),
    #      "update", sess.run(update))

sess.close()

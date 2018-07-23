import tensorflow as tf

# 그래프 작성
aa = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32) # 값이 없는 변수 b 생성
add = tf.add(aa, b)

# 실행부
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 변수 초기화
# 세션 실행 시 feed를 통해 add 함수 수행
print(sess.run(add, feed_dict={aa:4, b:5})) # add 함수 실행, feed_dict는 변수 값 넣기
sess.close()
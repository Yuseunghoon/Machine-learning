from sklearn.neural_network import MLPClassifier
X_train = [[0., 0.], [1., 1.]]
y_train = [[0, 1], [1, 1]]

'''
MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
       beta_1=0.9, beta_2=0.999, early_stopping=False,
       epsilon=1e-08, hidden_layer_sizes=(15,), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)
'''
mlp = MLPClassifier(solver='lbfgs', alpha= 1e-5, hidden_layer_sizes= (5, 3), random_state = 1)
mlp.fit(X_train, y_train)

print(mlp.predict([[1., 2.]]))

print(mlp.predict([[0., 0.]]))


print("mlp.coefs_ :", mlp.coefs_)
print("coef.shape :", [coef.shape for coef in mlp.coefs_])
print("mlp.n_outputs_ : ", mlp.n_outputs_)
print("mlp.classes_:", mlp.classes_)
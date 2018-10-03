from sklearn import svm
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)

lin_clf = svm.LinearSVC()
lin_clf.fit(X, Y)




dec = lin_clf.decision_function([[1]])
dec.shape[1]
print dec
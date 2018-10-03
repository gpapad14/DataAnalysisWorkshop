from sklearn import datasets, tree
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydot
import sys

from time import time
sys.path.append("../Assignment4/")


X = [[0, 0], [0, 2], [2,0], [2,1], [1,2], [2,3], [5,1], [3,2], [3,3], [4,2], [4,3], [4,4], [5,2], [1, 1]]
Y = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)
print clf.predict([[1.1, 1.1]])
print clf.predict_proba([[1.1, 1.1]])


dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names='X',
                         class_names='sdf',
                         filled=True, rounded=True,
                         special_characters=True)



# one way is:
#dot_data =tree.export_graphviz(clf, out_file='tree.dot')
# After that command, you can run in terminal:...$ dot -Tpng tree.dot -o tree.png
#                                         or :...$ dot -Tpdf tree.dot -o tree.pdf

# other way without terminal:
# #dotfile = StringIO()
# #tree.export_graphviz(clf, out_file=dotfile)
#graph = pydot.graph_from_dot_data(dotfile.getvalue())
#graph.create_png('dfj.png')
#graph.write_pdf("flfn.pdf")

#-----------------------------------

# 2nd way
#dotfile = StringIO()
#tree.export_graphviz(clf, out_file=dotfile)
#pydot.graph_from_dot_data(dotfile.getvalue()).write_png("dtree2.png")

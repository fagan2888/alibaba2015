# coding:utf-8
'''
利用特征 最后一天对物品点击数，最后一天对品牌点击数， 用户转化率
'''
import sklearn,pandas, pickle
import numpy as np

from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.metrics import f1_score
from sklearn.grid_search import GridSearchCV

def GetData():
	
	data = pandas.read_csv('data.csv.subset.csv')
	
	
	X=GetFeature(data)
	
	
	Y=data['buy'].as_matrix()
	
	#rand = np.random.rand(len(Y))<0.0001
	#idx = (Y==1) | ((Y==0) & rand)
	
	#X = X[idx]
	#Y = Y[idx]

	
	return X, Y
	
def GetFeature(data):
	data['user_cat_lastday_count'] = np.log(0.3+data['user_cat_lastday_count'])
	data['user_item_lastday_count'] = np.log(0.3+data['user_item_lastday_count'])
	data['user_convert_rate'] = data['user_buy_count'] / (1+data['user_action_count'])
	data['user_action_count'] = np.log(0.3 + data['user_action_count'])
	
	X=data[['user_item_lastday_count','user_cat_lastday_count','user_convert_rate', 'user_action_count']].as_matrix()
	
	return X

		
def GetModel():
	f = open('model5.model','rb')
	clf = pickle.load(f)
	f.close()
	return clf

if __name__ == '__main__':
	
	X, Y = GetData()

	parms = {
	'C':np.logspace(-6,0,10),
	#'class_weight':[{0:1,1:50},{0:1,1:70},{0:1,1:85},{0:1,1:100},{0:1,1:120},{0:1,1:150}]
	'class_weight':[{0:1,1:200}] #[{0:1,1:r} for r in np.logspace(2,4,10)]
	}
	lr = LogisticRegression(penalty='l2')
	clf = GridSearchCV(lr, parms, scoring='f1', n_jobs=10)

	clf.fit(X,Y)
	
	import pickle
	f = open('model5.model','wb')
	pickle.dump(clf, f)
	f.close()
	
	
	
	pred = clf.predict(X)
	from summary import summary,clf_summary
	clf_summary(clf)
	summary(Y, pred)
	
	



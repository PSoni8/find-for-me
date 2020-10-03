import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
data = fetch_movielens(min_rating = 4.0)
print(repr(data['train']))
print(repr(data['test']))
data
model = LightFM(loss='warp')
model.fit(data['train'], epochs = 30, num_threads=2)
def sample_recommendation(model, data, user_ids):
#number of users and movies in training data
n_users, n_items = data['train'].shape

    #generate recommendations for each user input
    for user_id in user_ids: 

        #movies they always like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies the model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print results
        print("User %s" % user_id)
        print("         Known positives:")

        for x in known_positives[:3]:
            print("          %s" % x)
        
        print("         Recommend:")

        for x in top_items[:3]:
            print("         %s" % x)
            sample_recommendation(model, data, [0, 3, 25, 34, 450])

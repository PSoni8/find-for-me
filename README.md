# find-for-me
Built a Primary Movie Recommendation Engine using lightfm Library.Data is collected from 'fetch\_movielens'method from lightfm.A function is build to recommend movies for any number of users.Also Studied and implemented popular collaborative filtering.</br>
1.The code uses the lightfm recommender system library to train a hybrid content-based + collaborative algorithm that uses the WARP loss function on the movielens dataset.</br>
2. The movielens dataset contains movies and ratings from over 1700 users. Once trained, our script prints out recommended movies for whatever users from the dataset that we choose to terminal.</br>
RECOMMENDATION SYSTEM:A recommendation system is any system that automatically suggests content, products or serivces which should interest customers based on their preferences.</br>
PURPOSE:
The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.</br>
TYPES OF RECOMMENDATION SYSTEM:</br>
1.Content-based recommendation engine</br>
2.Collobrative-filtering (CF) based recommendation engine </br>
3.Popularity based recommendation systems</br>
4.Classification model based</br>
5.Hybrid Approaches</br>
6.Association rule mining</br>
7.Deep Learning based recommendation systems</br>
DESCRIPTION:</br>
1.Content-based recommendation engine:</br>
i.Content based system suggests you what you like based on what you liked in past.</br>
ii.Recommendation of items are based on : user's previous purcheses, reviews and likes</br>
iii.Combine: Item description and User profile description</br>
iv.Generate similarity score</br>
v.Recommend the items based on similarity score</br>
Tasks:</br>
i.Requirements:some information about the available items such as genre,some sort of user profile describing what the user likes</br>
ii.similarit by actors,directors,genre</br>
iii.learn user preferences about suggest same.</br>
2.Collobrative-filtering (CF) based recommendation engine </br>
Types of CF</br>
i.User-Item Collaborative Filtering: “Users who are similar to you also liked …”</br>
ii.Item-Item Collaborative Filtering: “Users who liked this item also liked …”</br>
Kaggle Notebook here:https://www.kaggle.com/psoni1507/notebooks</br>
Data sets:</br>
i.kaggle:https://www.kaggle.com/rounakbanik/the-movies-dataset/data</br>
ii.Movielens:https://grouplens.org/datasets/movielens/latest/</br>
Types of dataset:</br>
1.The full dataset: This dataset consists of 26,000,000 ratings and 750,000 tag applications applied to 45,000 movies by 270,000 users. Includes tag genome data with 12 million relevance scores across 1,100 tags.</br>
2.2.The small dataset: This dataset comprises of 100,000 ratings and 1,300 tag applications applied to 9,000 movies by 700 users.</br>
We will build a simple Recommendation for movies using The full dataset.</br>
Data description:</br>
It contains 100004 ratings and 1296 tag applications across 9125 movies. These data were created by 671 users between January 09, 1995 and October 16, 2016. This dataset was generated on October 17, 2016.Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.</br>
The data are contained in the following files:</br>
credits.csv</br>
keywords.csv</br>
links.csv</br>
links_small.csv</br>
movies_metadata.csv</br>
ratings.csv</br>
ratings_small.csv</br>


from django.shortcuts import render
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np


# Create your views here.
def item_based(request):
    rating_data = pd.read_csv('ratings.csv')
    movie_data = pd.read_csv('movies.csv')

    if request.method == 'POST':
        movie_input = request.POST.get('movie_name')
        rating_data.drop('timestamp', axis=1, inplace=True)
        user_movie_rating = pd.merge(rating_data, movie_data, on='movieId')

        movie_user_rating = user_movie_rating.pivot_table('rating', index='title', columns='userId')
        # user_movie_rating = user_movie_rating.pivot_table('rating', index='userid', columns='title')

        movie_user_rating.fillna(0, inplace=True)

        item_based_collaborator = cosine_similarity(movie_user_rating)
        item_based_collaborator_df = pd.DataFrame(data=item_based_collaborator, index=movie_user_rating.index,
                                                  columns=movie_user_rating.index)

        result = get_item_based_collaborator(movie_input, item_based_collaborator_df)
        result = result.index.to_list()

        return render(request, 'item_based_result.html', {'result': result})

    # msg = 'failed'
    return render(request, 'item_based.html', {'message': movie_data})


def get_item_based_collaborator(title, item_based_collaborator):
    return item_based_collaborator[title].sort_values(ascending=False)[1:6]


def matrix_factorization(request):
    rating_data = pd.read_csv('ratings.csv')
    movie_data = pd.read_csv('movies.csv')

    if request.method == 'POST':
        movie_input = request.POST.get('movie_name')
        rating_data.drop('timestamp', axis=1, inplace=True)
        movie_data.drop('genres', axis=1, inplace=True)

        user_movie_data = pd.merge(rating_data, movie_data, on='movieId')
        user_movie_rating = user_movie_data.pivot_table('rating', index='userId', columns='title').fillna(0)

        movie_user_rating = user_movie_rating.values.T
        svd_ = TruncatedSVD(n_components=12)
        matrix = svd_.fit_transform(movie_user_rating)

        corr = np.corrcoef(matrix)
        movie_title = user_movie_rating.columns
        movie_title_list = list(movie_title)
        coffey_hands = movie_title_list.index(movie_input)

        corr_coffey_hands = corr[coffey_hands]
        result = list(movie_title[(corr_coffey_hands >= 0.9)])[:5]

        return render(request, 'matrix_factorization_result.html', {'result': result})

    return render(request, 'matrix_factorization.html', {'message': movie_data})


def index(request):
    return render(request, 'index.html')

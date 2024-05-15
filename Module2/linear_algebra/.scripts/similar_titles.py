import numpy as np

def cosine_similarity(titles_matrix, query_vector):
    """
        Description:
            Compute the cosine similarity between the query vector and the titles vector.
        Args:
            query_vector (numpy.ndarray): The query vector.
            titles_vector (numpy.ndarray): The titles vector.
        Returns:
            numpy.ndarray: The cosine similarity between the query and the titles.
        Expected Output:
            array([0.        , 0.        , 0.        , ..., 0.        , 0.        , 0.23570226])
    """
    # Option 1 - using sklearn cosine_similarity
    # cosine_similarities = cosine_similarity(
    #     query_vector, titles_vector)

    # Option 2 - using numpy dot product
    dot_product = np.dot(titles_matrix, query_vector) # Dot product between the query and the titles
    norm_titles = np.linalg.norm(titles_matrix, ord=2, axis=1) # Euclidean norm by row
    norm_query = np.linalg.norm(query_vector, ord=2)
    cosine_similarities = dot_product / (norm_titles * norm_query) # Cosine similarity

    cosine_similarities_flatten = cosine_similarities.flatten()

    return cosine_similarities_flatten
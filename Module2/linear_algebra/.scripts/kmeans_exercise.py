import numpy as np

random_state = 42

def initialize_centroids(points, k):
    """
        Description:
            Randomly initialize the centroids from the data points.
        Args:
            points (np.ndarray): Data points.
            k (int): Number of clusters.
        Returns:
            np.ndarray: Initial k centroids.
    """
    np.random.seed(random_state)
    _centroids = points.copy()
    np.random.shuffle(_centroids)

    return _centroids[:k]

def calculate_distance(points, centroids):
    """
        Description:
            Compute the euclidean distance between data points and centroids.
        Args:
            points (np.ndarray): Data points.
            centroids (np.ndarray): Centroids.
        Returns:
            np.ndarray: Distances between data points and centroids.
    """

    # # Option 1 - using for loop:
    # distances = []

    # for _centroid in centroids:
    #     _dist = np.sqrt( ( (points - _centroid) ** 2 ).sum(axis=1) )
    #     distances.append(_dist)

    # distances = np.array(distances)

    # # Option 2 - using numpy broadcasting:
    # distances = np.sqrt(
    #     ((points[np.newaxis, :, :] - centroids[:, np.newaxis, :])**2).sum(axis=2)
    # )

    # Option 3 - using numpy broadcasting and linalg.norm:
    distances = np.linalg.norm(
        points[np.newaxis, :, :] - centroids[:, np.newaxis, :], axis=2)

    # Other options - try with other distance metrics:
    # ...

    return distances

def closest_centroid(distances):
    """
        Description:
            Obtain the index of the closest centroid, minimum distance, for each data point.
        Args:
            distances (np.ndarray): Distances between data points and centroids.
        Returns:
            np.ndarray: Index of the closest centroid for each data point.
    """
    return np.argmin(distances, axis=0) # Column-wise axis=0

def update_centroids(points, closest, centroids):
    """
        Description:
            Update centroid positions as the mean of all assigned points.
        Args:
            points (np.ndarray): Data points.
            closest (np.ndarray): Index of the closest centroid for each data point.
            centroids (np.ndarray): Centroids.
        Returns:
            np.ndarray: Updated centroids.
    """
    for i in range(centroids.shape[0]):
        centroids[i] = points[closest == i].mean(axis=0) # Mean along the rows
    return centroids

def naive_kmeans(points, k, max_iters):
    """
        Description:
            Repeat the process for a maximum number of iterations
        Args:
            points (np.ndarray): Data points.
            k (int): Number of clusters.
            max_iters (int): Maximum number of iterations.
        Returns:
            np.ndarray: Final centroids.
    """

    centroids = initialize_centroids(points, k)

    for _ in range(max_iters):
        distances = calculate_distance(points, centroids)
        closest = closest_centroid(distances)
        centroids = update_centroids(points, closest, centroids)

    return centroids, closest

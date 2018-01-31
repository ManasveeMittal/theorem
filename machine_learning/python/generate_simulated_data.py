

def generate_simulated_data(type, display=True, visualize=False):
    """ generated simulated_data"""
    from sklearn.datasets import make_classification
    from sklearn.datasets import make_regression
    from sklearn.datasets import make_blobs
    import matplotlib.pyplot as plt
    # Create a simulated feature matrix and output vector with 100 samples,
    if type == 'classification':
        features, output = make_classification(n_samples=100,
                                               # ten features
                                               n_features=10,
                                               # five features that actually predict the output's classes
                                               n_informative=5,
                                               # five features that are random and unrelated to the output's classes
                                               n_redundant=5,
                                               # three output classes
                                               n_classes=3,
                                               # with 20% of observations in the first class, 30% in the second class,
                                               # and 50% in the third class. ('None' makes balanced classes)
                                               weights=[.2, .3, .8])
        return features, output
    elif type == 'clustering':
        # Make the features (X) and output (y) with 200 samples,
        features, output = make_blobs(n_samples=200,
                                      # two feature variables,
                                      n_features=2,
                                      # three clusters,
                                      centers=3,
                                      # with .5 cluster standard deviation,
                                      cluster_std=0.5,
                                      # shuffled,
                                      shuffle=True)
        # Create a scatterplot of the first and second features
        if visualize == True:
            plt.scatter(features[:, 0],
                        features[:, 1])

            # Show the scatterplot
            plt.show()
        return features, output

    elif type == 'regression':
        # Generate fetures, outputs, and true coefficient of 100 samples,
        features, output, coef = make_regression(n_samples=100,
                                                 # three features
                                                 n_features=3,
                                                 # where only two features are useful,
                                                 n_informative=2,
                                                 # a single target value per observation
                                                 n_targets=1,
                                                 # 0.0 standard deviation of the guassian noise
                                                 noise=0.0,
                                                 # show the true coefficient used to generated the data
                                                 coef=True)
        print(coef)
        return features, output  # , coef
    else:
        print(__doc__)
        print("recheck parameter values")


X, y = generate_simulated_data("clustering", display=True, visualize=True)
print(X)

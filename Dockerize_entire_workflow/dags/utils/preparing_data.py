import numpy as np

def preparing_data(scaled_features, scaled_target=None):
    """
    function take scaled data as input
    and return X and y target
    """
    n_steps = 1
    X = np.array([scaled_features[i-n_steps:i, :] for i in range(n_steps, len(scaled_features))])
    if scaled_target is not None:
        y = np.array(scaled_target[n_steps:])
    else:
        y = None
        
    return X, y
        
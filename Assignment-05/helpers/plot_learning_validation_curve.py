def plot_learning_curve(train_sizes, train_scores, test_scores):
    
    """Plot the learning curve."""
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Create means and standard deviations of training set scores:
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)

    # Create means and standard deviations of test set scores:
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # Draw lines:
    plt.plot(train_sizes, train_mean, '--', color="#111111", label="Training score")
    plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

    # Draw bands:
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

    # Create the plot:
    plt.xlim(left=np.min(train_sizes), right=np.max(train_sizes))
    plt.ylim(bottom=0, top=1.0)
    plt.title("Learning Curve")
    plt.xlabel("Training Set Size"), plt.ylabel("Score"),
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()
    
    
def plot_validation_curve(param_range, train_scores, test_scores):
    
    """Plot the validation curve."""
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Calculate mean and standard deviation for training set scores:
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    
    # Calculate mean and standard deviation for test set scores:
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    
    # Plot mean accuracy scores for training and test sets:
    plt.plot(param_range, train_mean, label="Training score", color="black")
    plt.plot(param_range, test_mean, label="Cross-validation score", color="dimgrey")
    
    # Plot accurancy bands for training and test sets:
    plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, color="gray")
    plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, color="gainsboro")
    
    # Create plot:
    plt.xlim(left=np.min(param_range), right=np.max(param_range))
    plt.ylim(bottom=0, top=1.0)
    plt.title("Validation Curve")
    plt.xlabel("Parameter range")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.legend(loc="best")
    plt.show()
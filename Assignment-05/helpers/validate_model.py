def compare_models(X, y, scoring, estimators={}, **kwargs):
    "Compare different estimators."
    import matplotlib.pyplot as plt
    from sklearn.model_selection import cross_val_score, KFold
    estimators.update(kwargs)
    results = []
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    for name, estimator in estimators.items():
        cv_results = cross_val_score(estimator, X, y, cv=kf, scoring=scoring)
        print(f"For {name}, results are:")
        print(f"  min = {cv_results.min():.2%}")
        print(f"  mean = {cv_results.mean():.2%}")
        print(f"  max = {cv_results.max():.2%}\n")
        results.append(cv_results)
    plt.boxplot(results, labels=estimators.keys())
    return results
        
        
    
from infomeasure import mutual_information as im_mi

MI_APPROACHES = {
    "discrete",
    "metric",   # kNN-based MI
}


def compute_mutual_information(x, y, approach: str, **kwargs):
    """
    Compute mutual information I(X;Y).

    Parameters
    ----------
    x, y : array-like
        Samples of two random variables.
    approach : str
        Mutual information estimator.
    kwargs : dict
        Estimator-specific parameters.

    Returns
    -------
    dict
        Mutual information value with metadata.
    """

    if approach not in MI_APPROACHES:
        raise ValueError(
            f"Approach '{approach}' not supported for mutual information."
        )

    value = im_mi(x, y, approach=approach, **kwargs)

    return {
        "mutual_information": float(value),
        "approach": approach,
        "params": kwargs,
    }

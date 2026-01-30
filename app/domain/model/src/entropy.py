from infomeasure import entropy as im_entropy

# ---- estimator types ----
DISCRETE_APPROACHES = {
    "discrete",
    "miller_madow",
    "grassberger",
    "chao_shen",
    "chao_wang_jost",
    "bonachela",
    "shrink",
    "nsb",
    "ansb",
}

CONTINUOUS_APPROACHES = {
    "metric",   # Kozachenko–Leonenko
    "kernel",
}



def compute_entropy(data, approach: str, **kwargs):
    """
    Compute entropy using infomeasure with explicit estimator semantics.

    Parameters
    ----------
    data : array-like
        Samples of a random variable.
    approach : str
        Entropy estimator name (infomeasure).
    kwargs : dict
        Estimator-specific parameters.

    Returns
    -------
    dict
        Entropy value with metadata.
    """

    if approach in DISCRETE_APPROACHES:
        value = im_entropy(data, approach=approach, **kwargs)
        entropy_type = "shannon"

    elif approach in CONTINUOUS_APPROACHES:
        value = im_entropy(data, approach=approach, **kwargs)
        entropy_type = "differential"

    else:
        raise ValueError(f"Unsupported entropy approach: {approach}")

    return {
        "entropy": float(value),
        "approach": approach,
        "entropy_type": entropy_type,
        "params": kwargs,
    }

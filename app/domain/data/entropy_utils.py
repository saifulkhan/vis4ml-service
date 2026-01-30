import numpy as np
import infomeasure as im

def entropy_from_samples(
    samples,
    estimator: str = "discrete",
    base=2
):
    """
    Sample-based entropy estimation using infomeasure.
    """
    return im.entropy(samples, approach=estimator, base=base)



def shannon_entropy_from_probs(probs, base=2):
    """
    Exact Shannon entropy from a discrete probability distribution.
    """
    probs = np.asarray(probs, dtype=float)
    probs = probs[probs > 0]  # avoid log(0)

    if base == 2:
        log_fn = np.log2
    else:
        log_fn = np.log

    return -np.sum(probs * log_fn(probs))
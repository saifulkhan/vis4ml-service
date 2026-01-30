import numpy as np

def generate_normal_integer_samples(
    n_samples: int = 320,
    mean: float = 50,
    std: float = 20,
    low: int = 0,
    high: int = 100,
    seed: int | None = None,
):
    """
    Generate integer samples from clipped normal distribution.
    This will later be replaced by real model/data outputs.
    """
    rng = np.random.default_rng(seed)

    samples = rng.normal(loc=mean, scale=std, size=n_samples)
    samples = np.round(samples).astype(int)
    samples = np.clip(samples, low, high)

    return samples.tolist()

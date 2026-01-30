from fastapi import APIRouter
from app.domain.data.sample_generator import generate_normal_integer_samples
from app.domain.data.alphabet_utils import samples_to_alphabet_distribution
from app.domain.data.entropy_utils import ( entropy_from_samples, shannon_entropy_from_probs )

router = APIRouter(prefix="/data/alphabet", tags=["Alphabet"])

@router.post("/raw")
async def get_raw_alphabet(
    n_samples: int = 320,
    mean: float = 50,
    std: float = 20,
    seed: int = 42,
):
    # generate samples
    samples = generate_normal_integer_samples(
        n_samples=n_samples,
        mean=mean,
        std=std,
        seed=seed,
    )

    # alphabet distribution
    data = samples_to_alphabet_distribution(samples)
    probs = [d["prob"] for d in data]

    # entropy (sample-based)
    H = entropy_from_samples(samples, estimator="discrete")

    return {
        "alphabet_type": "raw",
        "total_count": len(samples),
        "data": data,
        "probs": probs,
        "entropy": H,
        "entropy_type": "samples",
        "approach": "discrete"
    }

@router.post("/entropy")
async def compute_entropy(
    mode: str,  # "samples" | "probs"
    samples: list[int] | None = None,
    probs: list[float] | None = None,
    estimator: str = "discrete",
):
    """
    Compute entropy for alphabet-related data.

    Modes:
    - samples: entropy computed from discrete samples (infomeasure-based)
    - probs: entropy computed directly from probability distribution (Shannon)

    Parameters
    ----------
    mode : str
        "samples" or "probs"
    samples : list[int], optional
        Discrete alphabet samples
    probs : list[float], optional
        Probability distribution over alphabet
    estimator : str
        Estimator name for sample-based entropy

    Returns
    -------
    dict
        Entropy value and metadata
    """

    # Case 1: sample-based entropy (raw / binned)
    if mode == "samples":
        if samples is None or len(samples) == 0:
            return {
                "status": "error",
                "message": "samples must be provided for mode='samples'"
            }

        H = entropy_from_samples(samples, estimator=estimator)

        return {
            "entropy": H,
            "entropy_type": "sample",
            "estimator": estimator,
            "sample_size": len(samples),
        }

    # Case 2: probability-based entropy (synthetic)
    elif mode == "probs":
        if probs is None or len(probs) == 0:
            return {
                "status": "error",
                "message": "probs must be provided for mode='probs'"
            }

        H = shannon_entropy_from_probs(probs)

        return {
            "entropy": H,
            "entropy_type": "probability",
            "definition": "Shannon",
            "alphabet_size": len(probs),
        }

    # Invalid mode
    else:
        return {
            "status": "error",
            "message": f"unknown mode '{mode}', expected 'samples' or 'probs'"
        }



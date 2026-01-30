from collections import Counter
from typing import List, Dict

def samples_to_alphabet_distribution(
    samples: List[int],
    alphabet_size: int = 101
) -> List[Dict]:
    """
    Convert integer samples to alphabet distribution.
    """
    total = len(samples)
    counter = Counter(samples)

    data = []
    for i in range(alphabet_size):
        count = counter.get(i, 0)
        prob = count / total if total > 0 else 0.0
        data.append({
            "letter": i,
            "count": count,
            "prob": prob
        })

    return data

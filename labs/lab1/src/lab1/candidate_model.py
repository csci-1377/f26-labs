"""A pointing-time model with diminishing increases in movement time."""

import numpy as np


class SquareRootModel:
    """Predict time in seconds with T = a * sqrt(distance / width) + b.

    With a > 0, farther targets take longer and wider targets take less time.
    Increasing distance has a progressively smaller effect on predicted time.
    The parameters a and b control the scale and baseline time, respectively.
    """

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        if not np.isfinite(self.a) or self.a <= 0:
            raise ValueError("a must be finite and positive")
        if not np.isfinite(self.b):
            raise ValueError("b must be finite")

    def pointing_time(self, distance, width):
        """Accept scalars or broadcastable arrays; D >= 0 and W > 0."""
        distance = np.asarray(distance, dtype=float)
        width = np.asarray(width, dtype=float)
        if np.any(~np.isfinite(distance)) or np.any(distance < 0):
            raise ValueError("distance must be finite and non-negative")
        if np.any(~np.isfinite(width)) or np.any(width <= 0):
            raise ValueError("width must be finite and positive")
        return self.a * np.sqrt(distance / width) + self.b


def hyperopt_space(label_prefix=""):
    """Return a fresh search space for this model.

    Suggested ranges: 0 < a < 0.3 and 0 <= b < 0.5 (seconds).
    Default labels match constructor arguments, as in the lab's fit_model.
    When combining models in one search, use distinct prefixes and decode
    fmin's result with hyperopt.space_eval before constructing the model.
    """
    from hyperopt import hp

    return {
        "a": hp.uniform(f"{label_prefix}a", 1e-8, 0.3),
        "b": hp.uniform(f"{label_prefix}b", 0.0, 0.5),
    }

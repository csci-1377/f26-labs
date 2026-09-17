"""Run pointing-time experiments and collect raw attempt data."""

from numbers import Integral

import numpy as np
import pandas as pd

from .mystery.mystery import PointingParticipant, _validate_condition


def _positive_integer(name, value):
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be a positive integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _validated_conditions(conditions):
    conditions = list(conditions)
    if not conditions:
        raise ValueError("conditions must contain at least one (distance, width) pair")
    for distance, width in conditions:
        _validate_condition(distance, width)
    return conditions


def simulate_participant(participant, conditions, *, repeats):
    """Run repeated attempts for one participant under each condition.

    Inputs:
        participant: An existing PointingParticipant; its attempt sequence continues.
        conditions: (distance, width) pairs in pixels.
        repeats: Positive number of attempts per condition, supplied explicitly.

    Output:
        DataFrame with one row per attempt: participant_id, distance, width,
        attempt (zero-based within each condition), pointing_time (seconds).
    """
    _positive_integer("repeats", repeats)
    conditions = _validated_conditions(conditions)
    rows = []
    for distance, width in conditions:
        for attempt in range(repeats):
            rows.append({
                "participant_id": participant.participant_id,
                "distance": distance,
                "width": width,
                "attempt": attempt,
                "pointing_time": participant.pointing_time(distance, width),
            })
    return pd.DataFrame(rows)


def simulate_group(conditions, *, n_participants, repeats):
    """Run repeated attempts for a randomly sampled group of participants.

    Inputs:
        conditions: (distance, width) pairs in pixels.
        n_participants: Positive number of distinct participants to create.
        repeats: Positive number of attempts per participant per condition.
        Both counts must be supplied explicitly as integers.

    Output:
        DataFrame combining all participants' raw attempts: participant_id,
        distance, width, attempt (zero-based), pointing_time (seconds).
    """
    _positive_integer("n_participants", n_participants)
    _positive_integer("repeats", repeats)
    conditions = _validated_conditions(conditions)
    rng = np.random.default_rng()
    participant_ids = rng.choice(2**63 - 1, size=n_participants, replace=False)
    results = [
        simulate_participant(
            PointingParticipant(participant_id=participant_id),
            conditions,
            repeats=repeats,
        )
        for participant_id in participant_ids
    ]
    return pd.concat(results, ignore_index=True)

"""Helpers the demo tests share, copied from indrajala-ml's tests/helpers.py."""

import pytest
from indrajala_ml.model.networks.python.linear_classifier_network import LinearClassifierNetwork


def approx(expected: object, rel: float | None = None, abs: float | None = None) -> object:
    """pytest.approx, typed: pytest 8.1 leaves its parameters unannotated, which strict mode reports at every call."""
    return pytest.approx(expected, rel=rel, abs=abs)  # pyright: ignore[reportUnknownMemberType]


def classifier_with_bounded_square_region(bounds: list[tuple[float, float]]) -> LinearClassifierNetwork:

    # positive region is exactly the square [-1, 1] x [-1, 1]: x > -1, x < 1, y > -1, y < 1
    classifier = LinearClassifierNetwork(4, 2, bounds)
    for node, (weights, threshold) in zip(
        classifier.hidden_layer.nodes,
        [([1.0, 0.0], 1.0), ([-1.0, 0.0], 1.0), ([0.0, 1.0], 1.0), ([0.0, -1.0], 1.0)],
    ):
        node.update_input_weights(weights)
        node.threshold = threshold
    return classifier

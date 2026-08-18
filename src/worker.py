"""Minimal resilient queue worker example."""


def retry_delay(attempt: int) -> int:
    """Return a bounded exponential retry delay in seconds."""
    return min(2 ** max(attempt, 0), 60)

"""Retry utilities with exponential backoff for SIPAP.

Provides decorators for automatically retrying functions on transient failures.
"""

import functools
import random
import time
from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry_with_backoff(
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    max_delay: float = 60.0,
    retry_exceptions: tuple[type[Exception], ...] = (Exception,),
    no_retry_exceptions: tuple[type[Exception], ...] = (),
    jitter: bool = False,
) -> Callable[[F], F]:
    """Decorator to retry function with exponential backoff.

    Args:
        max_attempts: Maximum number of attempts (default 3)
        initial_delay: Initial delay in seconds before first retry (default 1.0)
        backoff_factor: Multiplier for delay between retries (default 2.0)
        max_delay: Maximum delay between retries in seconds (default 60.0)
        retry_exceptions: Tuple of exceptions to retry on (default all exceptions)
        no_retry_exceptions: Tuple of exceptions to never retry (overrides retry_exceptions)
        jitter: Add random jitter to delays to avoid thundering herd (default False)

    Returns:
        Decorated function with retry logic

    Examples:
        >>> @retry_with_backoff(max_attempts=3, initial_delay=1.0)
        ... def fetch_data(url: str) -> dict:
        ...     response = requests.get(url)
        ...     response.raise_for_status()
        ...     return response.json()

        >>> # Retry only on specific exceptions
        >>> @retry_with_backoff(
        ...     max_attempts=5,
        ...     retry_exceptions=(ConnectionError, TimeoutError)
        ... )
        ... def api_call() -> dict:
        ...     return external_api.fetch()

        >>> # Never retry on certain errors
        >>> @retry_with_backoff(
        ...     max_attempts=3,
        ...     no_retry_exceptions=(ValueError, KeyError)
        ... )
        ... def process_data(data: dict) -> dict:
        ...     return transform(data)
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            delay = initial_delay

            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except no_retry_exceptions:
                    # Never retry these exceptions
                    raise
                except retry_exceptions:
                    attempt += 1

                    # If this was the last attempt, re-raise
                    if attempt >= max_attempts:
                        raise

                    # Calculate delay with exponential backoff
                    if attempt > 1:
                        delay = min(delay * backoff_factor, max_delay)

                    # Add jitter if enabled (random 0-100% of delay)
                    actual_delay = delay
                    if jitter:
                        actual_delay = delay * random.uniform(0, 1)

                    # Sleep before retry
                    if actual_delay > 0:
                        time.sleep(actual_delay)

            # This should never be reached, but satisfies type checker
            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator

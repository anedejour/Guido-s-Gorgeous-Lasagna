"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """

    """

    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time

    return time_remaining


def preparation_time_in_minutes(layers):
    """

    """
    TIME_TO_PREPARE_A_LAYER = 2

    time = TIME_TO_PREPARE_A_LAYER * layers

    return time


def elapsed_time_in_minutes(layers, elapsed):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """

    bake_time = preparation_time_in_minutes(layers) + elapsed

    return bake_time

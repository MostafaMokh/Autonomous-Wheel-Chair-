"""
Autonomous Wheelchair Decision Module

Determines wheelchair movement based on obstacle distance.
"""

# Distance thresholds in centimeters
STOP_THRESHOLD = 20
SLOW_THRESHOLD = 50


def decide_movement(distance):
    """
    Decide wheelchair movement based on distance input.

    Args:
        distance (float/int/str): Distance from obstacle in cm.

    Returns:
        str: Movement decision:
            - "STOP"
            - "SLOW"
            - "MOVE"
            - "INVALID INPUT"
    """

    if distance is None:
        return "INVALID INPUT"

    try:
        distance = float(distance)
    except (ValueError, TypeError):
        return "INVALID INPUT"

    if distance < 0:
        return "INVALID INPUT"

    if distance <= STOP_THRESHOLD:
        return "STOP"
    elif distance <= SLOW_THRESHOLD:
        return "SLOW"
    else:
        return "MOVE"


def run_tests():
    """Run sample test cases."""
    test_inputs = [15, 35, 80, -5, "invalid", None]

    print(f"{'Input (cm)':<15} | {'Decision':<15}")
    print("-" * 35)

    for value in test_inputs:
        print(f"{str(value):<15} | {decide_movement(value):<15}")


if __name__ == "__main__":
    run_tests()

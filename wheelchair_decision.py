"""
Decision system for wheelchair movement based on distance input.

This function takes a distance value (in cm) and returns one of three decisions:
- STOP: if the object is very close
- SLOW: if the object is at a moderate distance
- MOVE: if the path is clear

It also handles invalid inputs like non-numeric values, negative numbers, or None.
"""

def decide_movement(distance):
    # Handle None input
    if distance is None:
        return "INVALID INPUT"

    # Try to convert input to float to handle strings or other numeric types
    try:
        distance = float(distance)
    except (ValueError, TypeError):
        return "INVALID INPUT"

    # Handle negative distance
    if distance < 0:
        return "INVALID INPUT"

    # Thresholds logic (As required: Use thresholds not just one if)
    STOP_THRESHOLD = 20
    SLOW_THRESHOLD = 50

    if distance <= STOP_THRESHOLD:
        return "STOP"
    elif distance <= SLOW_THRESHOLD:
        return "SLOW"
    else:
        return "MOVE"

# --- Test Cases (Deliverable: Test cases input -> output) ---
if __name__ == "__main__":
    # Sample inputs to test all logic branches and error handling
    test_inputs = [15, 35, 80, -5, "invalid", None]

    print(f"{'Input (cm)':<15} | {'Decision':<15}")
    print("-" * 35)

    for val in test_inputs:
        result = decide_movement(val)
        print(f"{str(val):<15} | {result:<15}")

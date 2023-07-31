step_index = 1


def step(message: str):
    global step_index

    print()
    print(f"--- STEP {step_index}: {message}")
    print()

    step_index += 1

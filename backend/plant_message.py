def generate_plant_message(plant):
    issues = plant["issues"]

    if issues == ["healthy"]:
        return "I'm feeling great! My soil, light, and temperature all look good."

    messages = []

    if "needs water" in issues:
        messages.append("I'm feeling pretty thirsty because my soil is dry")

    if "too wet" in issues:
        messages.append("my soil is a little too wet right now")

    if "needs more light" in issues:
        messages.append("it's a little dark over here")

    if "too much light" in issues:
        messages.append("I'm getting a little too much light")

    if "too cold" in issues:
        messages.append("I'm feeling a little cold")

    if "too hot" in issues:
        messages.append("I'm getting too warm")

    if len(messages) == 1:
        problem_text = messages[0]
    else:
        problem_text = ", ".join(messages[:-1]) + ", and " + messages[-1]

    return "Hey! " + problem_text + ". Could you check on me?"


if __name__ == "__main__":
    # Temporary test data
    test_plant = {
        "issues": ["needs water", "needs more light", "too cold"]
    }

    message = generate_plant_message(test_plant)
    print(message)
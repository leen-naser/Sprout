def generate_plant_message(plant):
    status = plant["overall_status"]

    if status == "needs water":
        return "Hey! I'm feeling pretty thirsty. My soil is dry, but otherwise I'm doing okay. Could you give me some water?"

    elif status == "too wet":
        return "My soil is a little too wet right now. Please give me some time to dry out."

    elif status == "needs more light":
        return "It's a little dark over here. Could you move me somewhere with more light?"

    elif status == "too much light":
        return "I'm getting a little too much light. Could you move me somewhere less bright?"

    elif status == "too cold":
        return "I'm feeling a little cold. Could you move me somewhere warmer?"

    elif status == "too hot":
        return "I'm getting too warm. Could you move me somewhere cooler?"

    else:
        return "I'm feeling great! My soil, light, and temperature all look good."


if __name__ == "__main__":
    # Temporary test data
    test_plant = {
        "overall_status": "needs water"
    }

    message = generate_plant_message(test_plant)
    print(message)
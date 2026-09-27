def get_light_status(light):
    if light < 30:
        return "too dark"
    elif light > 80:
        return "too bright"
    else:
        return "healthy"


def read_light():
    # Temporary test value until Raspberry Pi sensor is connected
    light = 20

    return {
        "light": light,
        "status": get_light_status(light)
    }


if __name__ == "__main__":
    result = read_light()

    print("Light Level:", result["light"])
    print("Status:", result["status"])
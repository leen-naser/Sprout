def get_temperature_status(temperature):
    if temperature < 18:
        return "too cold"
    elif temperature > 27:
        return "too hot"
    else:
        return "healthy"


def read_temperature():
    # Temporary test value until Raspberry Pi sensor is connected
    temperature = 22.5

    return {
        "temperature": temperature,
        "status": get_temperature_status(temperature)
    }


if __name__ == "__main__":
    result = read_temperature()

    print("Temperature:", result["temperature"], "°C")
    print("Status:", result["status"])
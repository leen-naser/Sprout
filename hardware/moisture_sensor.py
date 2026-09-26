def get_moisture_status(moisture):
    if moisture < 30:
        return "dry"
    elif moisture > 75:
        return "too wet"
    else:
        return "healthy"


def read_moisture():
    # Temporary test value until Raspberry Pi sensor is connected
    moisture = 25

    return {
        "moisture": moisture,
        "status": get_moisture_status(moisture)
    }


if __name__ == "__main__":
    result = read_moisture()

    print("Soil Moisture:", result["moisture"])
    print("Status:", result["status"])
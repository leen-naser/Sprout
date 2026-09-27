from hardware.moisture_sensor import read_moisture
from hardware.light_sensor import read_light
from hardware.temperature_sensor import read_temperature


def get_plant_reading():
    moisture = read_moisture()
    light = read_light()
    temperature = read_temperature()

    issues = []

    if moisture["status"] == "dry":
        issues.append("needs water")

    if moisture["status"] == "too wet":
        issues.append("too wet")

    if light["status"] == "too dark":
        issues.append("needs more light")

    if light["status"] == "too bright":
        issues.append("too much light")

    if temperature["status"] == "too cold":
        issues.append("too cold")

    if temperature["status"] == "too hot":
        issues.append("too hot")

    if not issues:
        issues.append("healthy")

    return {
        "moisture": moisture,
        "light": light,
        "temperature": temperature,
        "issues": issues
    }


if __name__ == "__main__":
    plant = get_plant_reading()

    print("Moisture:", plant["moisture"])
    print("Light:", plant["light"])
    print("Temperature:", plant["temperature"])
    print("Plant Issues:", plant["issues"])
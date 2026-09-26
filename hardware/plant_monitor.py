from moisture_sensor import read_moisture
from light_sensor import read_light
from temperature_sensor import read_temperature


def get_plant_reading():
    moisture = read_moisture()
    light = read_light()
    temperature = read_temperature()

    if moisture["status"] == "dry":
        overall_status = "needs water"
    elif moisture["status"] == "too wet":
        overall_status = "too wet"
    elif light["status"] == "too dark":
        overall_status = "needs more light"
    elif light["status"] == "too bright":
        overall_status = "too much light"
    elif temperature["status"] == "too cold":
        overall_status = "too cold"
    elif temperature["status"] == "too hot":
        overall_status = "too hot"
    else:
        overall_status = "healthy"

    return {
        "moisture": moisture,
        "light": light,
        "temperature": temperature,
        "overall_status": overall_status
    }


if __name__ == "__main__":
    plant = get_plant_reading()

    print("Moisture:", plant["moisture"])
    print("Light:", plant["light"])
    print("Temperature:", plant["temperature"])
    print("Overall Plant Status:", plant["overall_status"])
from hardware.plant_monitor import get_plant_reading
from backend.plant_message import generate_plant_message
from backend.voice import speak


def check_plant():
    plant = get_plant_reading()
    message = generate_plant_message(plant)

    plant_data = {
        "moisture": plant["moisture"]["moisture"],
        "moisture_status": plant["moisture"]["status"],

        "light": plant["light"]["light"],
        "light_status": plant["light"]["status"],

        "temperature": plant["temperature"]["temperature"],
        "temperature_status": plant["temperature"]["status"],

        "issues": plant["issues"],
        "message": message
    }

    return plant_data


if __name__ == "__main__":
    plant_data = check_plant()

    print(plant_data)

    speak(plant_data["message"])
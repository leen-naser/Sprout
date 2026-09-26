from hardware.plant_monitor import get_plant_reading
from backend.plant_message import generate_plant_message
from backend.voice import speak


plant = get_plant_reading()

message = generate_plant_message(plant)

print(message)

speak(message)
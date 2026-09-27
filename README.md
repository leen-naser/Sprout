# 🌱 Sprout

**A plant that can tell you what it needs.**

Sprout is a smart plant monitoring system built for Hack the Hill 3. It combines physical sensors, computer vision, and voice AI to make plant care more intuitive.

Instead of making users interpret raw sensor readings, Sprout translates information about the plant and its environment into simple messages such as:

> "Hey! I'm feeling pretty thirsty. My soil is dry, but otherwise I'm doing okay. Could you give me some water?"

## 🌿 What Sprout Monitors

Sprout uses physical sensors connected to a Raspberry Pi to monitor:

- 💧 **Soil moisture**
- ☀️ **Light level**
- 🌡️ **Temperature**

The sensor readings are processed by our Python backend to determine the plant's current environmental conditions.

Sprout also uses a **Logitech webcam and Gemini Vision** to visually inspect the plant for:

- 🍃 Leaf condition
- 🎨 Discoloration
- 🔍 Other visible issues

The sensor readings and visual analysis are displayed separately so users can see both the plant's environment and its visible condition.

## 🔊 Giving the Plant a Voice

After analyzing the sensor data, Sprout generates a human-friendly message describing what the plant needs.

Using **ElevenLabs text-to-speech**, Sprout can then speak that message aloud, making the plant itself feel like the interface.

## 🛠️ Tech Stack

### Hardware
- Raspberry Pi 4
- Grove Base HAT
- Grove Soil Moisture Sensor
- Grove Light Sensor
- Grove Temperature & Barometer Sensor (SPA06-003)
- Logitech Webcam

### Software
- Python
- Flask
- React
- Vite
- Gemini Vision
- ElevenLabs
- Grove.py

## ⚙️ How It Works

```text
                 ┌── Soil Moisture Sensor
                 ├── Light Sensor
Plant ───────────┼── Temperature Sensor
                 │
                 └── Webcam
                       │
                       ▼
                 Raspberry Pi
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
      Sensor Analysis       Gemini Vision
            │                     │
            └──────────┬──────────┘
                       ▼
                React Dashboard
                       │
                       ▼
               ElevenLabs Voice
```

The Raspberry Pi collects live environmental readings from the sensors.

The webcam captures an image of the plant, which is analyzed separately using Gemini Vision.

The React interface displays the sensor readings and visual analysis, while ElevenLabs allows Sprout to speak its sensor-based status message aloud.

## 🚀 Running Sprout

### Backend

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing the required API keys.

Start the Raspberry Pi plant-data server:

```bash
python -m backend.server
```

Start the voice and vision server on the laptop:

```bash
python -m backend.voice_server
```

### Frontend

From the `frontend` directory:

```bash
npm install
npm run dev
```

Then open the local Vite address shown in the terminal.

## 👩‍💻 Team

Built at **Hack the Hill 3** by:

- Leen Naser
- Olivia Fullerton
- Annmaria

## 💡 Why Sprout?

Plant monitoring systems often provide numbers, graphs, and alerts that still require the user to understand what those measurements mean.

Sprout takes a different approach:

**Instead of asking you to understand your plant's data, Sprout lets your plant tell you what it needs.** 🌱

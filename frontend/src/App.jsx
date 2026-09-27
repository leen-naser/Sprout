import { useState } from 'react'
import './App.css'

function getStatusText(issues) {
  if (!issues || issues.length === 0) {
    return 'Please check on me!'
  }

  if (issues.includes('healthy')) {
    return "I'm feeling great!"
  }

  if (issues.length > 1) {
    return 'Please check on me!'
  }

  const issue = issues[0]

  if (issue === 'needs water') return "I'm thirsty!"
  if (issue === 'too wet') return "I'm too wet!"
  if (issue === 'needs more light') return 'I need more light!'
  if (issue === 'too much light') return "I'm getting too much light!"
  if (issue === 'too cold') return "I'm too cold!"
  if (issue === 'too hot') return "I'm too hot!"

  return 'Please check on me!'
}

function App() {
  const [plantData, setPlantData] = useState({
    moisture: 24,
    light: 'Good',
    temperature: 22.8,
    status: "I'm thirsty!",
    message: 'My soil is getting dry.'
  })

  const [visionData, setVisionData] = useState(null)
  const [isChecking, setIsChecking] = useState(false)

  const checkPlant = async () => {
    setIsChecking(true)

    try {
      // Get real sensor data from Raspberry Pi
      const sensorResponse = await fetch(
        'http://192.168.137.19:5000/api/plant'
      )

      const data = await sensorResponse.json()

      setPlantData({
        moisture: data.moisture,
        light: data.light_status,
        temperature: data.temperature,
        status: getStatusText(data.issues),
        message: data.message
      })

      // Capture webcam photo and analyze it
      try {
        const visionResponse = await fetch(
          'http://127.0.0.1:5001/api/vision'
        )

        if (visionResponse.ok) {
          const vision = await visionResponse.json()
          setVisionData(vision)
        }
      } catch (visionError) {
        console.error('Visual check failed:', visionError)
      }

      // Generate Sprout's voice
      const voiceResponse = await fetch(
        'http://127.0.0.1:5001/api/voice',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            message: data.message
          })
        }
      )

      if (!voiceResponse.ok) {
        throw new Error('Could not generate Sprout voice')
      }

      // Play ElevenLabs audio through laptop
      const audioBlob = await voiceResponse.blob()
      const audioUrl = URL.createObjectURL(audioBlob)
      const audio = new Audio(audioUrl)

      audio.onended = () => {
        URL.revokeObjectURL(audioUrl)
      }

      await audio.play()
    } catch (error) {
      console.error('Could not connect to Sprout:', error)
    }

    setIsChecking(false)
  }

  return (
    <div className="app">
      <header>
        <div className="plant-icon">🌱</div>
        <h1>SPROUT</h1>
        <p>Your plant has something to tell you.</p>
      </header>

      <main>
        <section className="plant-message">
          <div className="message-icon">💧</div>

          <div>
            <p className="message-label">SPROUT SAYS...</p>
            <h2>{plantData.status}</h2>
            <p>{plantData.message}</p>
          </div>
        </section>

        <section className="readings">
          <div className="reading">
            <span>💧</span>
            <h3>Moisture</h3>
            <p>{plantData.moisture}%</p>
          </div>

          <div className="reading">
            <span>☀️</span>
            <h3>Light</h3>
            <p>{plantData.light}</p>
          </div>

          <div className="reading">
            <span>🌡️</span>
            <h3>Temperature</h3>
            <p>{plantData.temperature}°C</p>
          </div>
        </section>

        {visionData && (
          <section className="readings">
            <div className="reading">
              <span>🍃</span>
              <h3>Leaves</h3>
              <p>{visionData.leaf_condition}</p>
            </div>

            <div className="reading">
              <span>🎨</span>
              <h3>Discoloration</h3>
              <p>{visionData.discoloration}</p>
            </div>

            <div className="reading">
              <span>🔍</span>
              <h3>Visible Issue</h3>
              <p>{visionData.visible_issue}</p>
            </div>
          </section>
        )}

        <button
          className="check-button"
          onClick={checkPlant}
          disabled={isChecking}
        >
          {isChecking ? 'CHECKING... 🌱' : 'CHECK ON MY PLANT'}
        </button>
      </main>
    </div>
  )
}

export default App
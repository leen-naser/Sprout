import { useState } from 'react'
import './App.css'

function App() {
  const [plantData, setPlantData] = useState({
    moisture: 24,
    light: 'Good',
    temperature: 22.8,
    status: 'thirsty',
    message: 'My soil is getting dry.'
  })

  const [isChecking, setIsChecking] = useState(false)

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
            <h2>I'm {plantData.status}!</h2>
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

        <button
          className="check-button"
          onClick={async () => {
            setIsChecking(true)

            try {
              const response = await fetch(
                'http://192.168.137.19:5000/api/plant'
              )

              const data = await response.json()

              setPlantData({
                moisture: data.moisture,
                light: data.light_status,
                temperature: data.temperature,
                status: data.overall_status,
                message: data.message
              })

              const speech = new SpeechSynthesisUtterance(data.message)
              window.speechSynthesis.speak(speech)

            } catch (error) {
              console.error('Could not connect to Sprout:', error)
            }

            setIsChecking(false)
          }}
        >
          {isChecking ? 'CHECKING... 🌱' : 'CHECK ON MY PLANT'}
        </button>
      </main>
    </div>
  )
}

export default App
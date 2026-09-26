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
          onClick={() => {
            setIsChecking(true)

            setTimeout(() => {
              setPlantData({
                moisture: 18,
                light: 'Good',
                temperature: 23.1,
                status: 'thirsty',
                message: 'Please give me some water!'
              })

              setIsChecking(false)
            }, 1000)
          }}
        >
          {isChecking ? 'CHECKING... 🌱' : 'CHECK ON MY PLANT'}
        </button>
      </main>
    </div>
  )
}

export default App
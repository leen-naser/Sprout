import './App.css'

function App() {
  return (
  <div className="app">
      <header>
        <div className="plant-icon">🌱</div>
        <h1>SPROUT</h1>
        <p>Your plant has something to tell you.</p>
      </header>

      <main>
        <section className="plant-message">
          <h2>I'm thirsty 💧</h2>
          <p>My soil is getting dry.</p>
        </section>

        <section className="readings">
          <div className="reading">
            <span>💧</span>
            <h3>Moisture</h3>
            <p>24%</p>
          </div>

          <div className="reading">
            <span>☀️</span>
            <h3>Light</h3>
            <p>Good</p>
          </div>

          <div className="reading">
            <span>🌡️</span>
            <h3>Temperature</h3>
            <p>22.8°C</p>
          </div>
        </section>

        <button className="check-button">
          CHECK ON MY PLANT
        </button>
      </main>
    </div>
  )

}

export default App
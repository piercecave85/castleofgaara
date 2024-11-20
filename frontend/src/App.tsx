import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.scss'

function App() {
  const [count, setCount] = useState(0)
  const [status, setStatus] = useState("Lights are off?")

  const requestOptions = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
  };

  const requestOptionsGet = {
        method: 'GET',
  };
  const getBulbStatus = async () => {
        try {
          const data = await (await fetch('https://api.castleofgaara.com/status/', requestOptionsGet)).json()
          console.log(data)
          setStatus(data.message ? "Lights are on" : "Lights are off")
        } catch (err) {
          console.log(err)
        }
  }
  const handleOnClick = async () => {
        try {
            const data = await (await fetch('https://api.castleofgaara.com/on/', requestOptions)).json()
            console.log(data)
            getBulbStatus()
        } catch (err) {
            console.log(err)
        }
    }
  const handleOffClick = async () => {
        try {
            const data = await (await fetch('https://api.castleofgaara.com/off/', requestOptions)).json()
            console.log(data)
            getBulbStatus()
        } catch (err) {
            console.log(err)
        }
    }

  useEffect(() => {
    getBulbStatus();
  }, []);

  return (
    <>
      <div className="container">
      <div className="row">
      <h2>
        Hi Sara &lt;3
      </h2>
      </div>
      <div className="row top-buffer">
      <div className="col">
      <button onClick={handleOnClick} className="btn btn-primary mx-1">
        On
      </button>
      <button onClick={handleOffClick} className="btn btn-dark mx-1">
        Off
      </button>
      </div>
      </div>
      <div className="row top-buffer">
      <img src="/cat3.png" />
      </div>
      <p>{status}</p>
      </div>
    </>
  )
}

export default App

import { useState } from 'react'
import './App.css'

function App() {
  const [value, setValue] = useState('')

  const append = (v) => setValue(value + v)
  const clear = () => setValue('')
  const backspace = () => setValue(value.slice(0, -1))

  const calculate = () => {
    try {
      setValue(eval(value).toString())
    } catch {
      setValue('Error')
    }
  }

  return (
    <div className="container">
      <div className="calculator">
        <h1>CALCULATOR</h1>
        <h2>BT23F05F014 <br></br>Arjun R Dasalkar<br></br>Batch A </h2>

        <input className="display" value={value} readOnly />

        <div className="buttons">
          <button onClick={clear}>C</button>
          <button onClick={backspace}>⌫</button>
          <button onClick={() => append('/')}>÷</button>
          <button onClick={() => append('*')}>×</button>

          <button onClick={() => append('7')}>7</button>
          <button onClick={() => append('8')}>8</button>
          <button onClick={() => append('9')}>9</button>
          <button onClick={() => append('-')}>−</button>

          <button onClick={() => append('4')}>4</button>
          <button onClick={() => append('5')}>5</button>
          <button onClick={() => append('6')}>6</button>
          <button onClick={() => append('+')}>+</button>

          <button onClick={() => append('1')}>1</button>
          <button onClick={() => append('2')}>2</button>
          <button onClick={() => append('3')}>3</button>
          <button onClick={() => append('0')}>0</button>

          <button onClick={() => append('.')}>.</button>
          <button className="equals" onClick={calculate}>=</button>
        </div>
      </div>
    </div>
  )
}

export default App

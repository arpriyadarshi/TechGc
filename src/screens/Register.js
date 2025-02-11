import React, { useState } from 'react';
import './Register.css';  // Create a new CSS file for Register component-specific styles.

function Register() {
  const [x, setX] = useState(0);
  const [y, setY] = useState(0);
  const [z, setZ] = useState(0);
  const [error, setError] = useState('');

  function validate(value) {
    if (isNaN(value)) {
      setError('Coordinates must be a number!');
      return false;
    }
    setError('');
    return true;
  }

  function handleInputChange(setter, value) {
    if (validate(value)) {
      setter(Number(value));
    }
  }

  function inc(setter, value) {
    setter(value + 0.05);
  }

  function dec(setter, value) {
    setter(value - 0.05);
  }

  function resetCoordinates() {
    setX(0);
    setY(0);
    setZ(0);
  }

  return (
    <div className="control-panel">
      <h1>Robotic Arm Interface</h1>
      <p>x:</p>
      <input 
        type="text" 
        placeholder="Enter x coordinate" 
        value={x} 
        onChange={(e) => handleInputChange(setX, e.target.value)} 
      />
      <p>y:</p>
      <input 
        type="text" 
        placeholder="Enter y coordinate" 
        value={y} 
        onChange={(e) => handleInputChange(setY, e.target.value)} 
      />
      <p>z:</p>
      <input 
        type="text" 
        placeholder="Enter z coordinate" 
        value={z} 
        onChange={(e) => handleInputChange(setZ, e.target.value)} 
      />
      <p>           </p>
      
      {error && <div className="error-message">{error}</div>}

      <div className="control-buttons">
        <button className="btn" onClick={() => inc(setX, x)}>x+</button>
        <button className="btn" onClick={() => inc(setY, y)}>y+</button>
        <button className="btn" onClick={() => inc(setZ, z)}>z+</button>
        <button className="btn" onClick={() => dec(setX, x)}>x-</button>
        <button className="btn" onClick={() => dec(setY, y)}>y-</button>
        <button className="btn" onClick={() => dec(setZ, z)}>z-</button>
      </div>

      <div className="status-display">
        <p>x: {x}</p>
        <p>y: {y}</p>
        <p>z: {z}</p>
      </div>
      
      <button className="reset-btn" onClick={resetCoordinates}>Reset</button>
    </div>
  );
}

export default Register;

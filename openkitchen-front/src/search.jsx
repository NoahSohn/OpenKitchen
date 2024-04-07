import { useState } from 'react'
import './Search.css'
// import searchmag from './assets/mag.svg'

function SearchBox() {
const [inputText, setInputText] = useState(''); // Initialize input text state

  const handleChange = (event) => {
    setInputText(event.target.value);
  };

  return (
    <div className="bubble-container">
      <input
        type="text"
        className="bubble-input"
        placeholder="Search"
        value={inputText}
        onChange={handleChange}
      />
    </div>
  );
}

export default SearchBox;

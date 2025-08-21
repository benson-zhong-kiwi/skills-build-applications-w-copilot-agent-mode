
import ReactDOM from 'react-dom/client';
import React from 'react';
import App from './App';
import reportWebVitals from './reportWebVitals';

console.log('REACT_APP_CODESPACE_NAME:', process.env.REACT_APP_CODESPACE_NAME);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();

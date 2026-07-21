import React from 'react'
import Inicio from './Inicio'
import RegistrarCampo from './RegistrarCampo.jsx'
import '../styles/App.css'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'

function App() {
  return (
    <div className="app-shell">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Inicio />} />
          <Route path='*' element={<Navigate to='/' replace />} />
          <Route path='/RegistrarCampo' element={<RegistrarCampo />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App

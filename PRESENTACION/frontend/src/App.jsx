import { Inicio } from './components/Inicio'
import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import './App.css'
import Reloj from './components/Reloj'

function App() {

  return (
    <>
      <Reloj />
      <BrowserRouter>
        <Routes>
          <Route path='/inicio' element={<Inicio />} />
          <Route path='*' element={<Navigate to='/inicio' replace />} />
        </Routes>
      </BrowserRouter>
      
    </>
  )
}

export default App

import { Inicio } from './components/Inicio'
import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import './App.css'

function App() {

  return (
    <>
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

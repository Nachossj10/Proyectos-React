import React from 'react'
import '../styles/RegistrarCampo.css'

function RegistrarCampo() {
  return (
    <div className="registro-container">
      <h1>Vamos a Registrar Un Nuevo Campo</h1>
      <div className="registro-form">
        <form>
          <div className="form-group">
            <label htmlFor="nombre" className='form-label'>Nombre del Campo:</label>
            <input type="text" id="nombre" name="nombre" className='form-control'/>
          </div>
          <div className="form-group">
            <label htmlFor="descripcion" className='form-label'>Descripción:</label>
            <textarea id="descripcion" name="descripcion" className='form-control'></textarea>
          </div>
          <button type="submit" className="btn btn-primary">Registrar Campo</button>
        </form>
      </div>
    </div>

  )
}

export default RegistrarCampo
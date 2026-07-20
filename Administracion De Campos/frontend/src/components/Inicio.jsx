import React from 'react';
import '../styles/Inicio.css';

function Inicio() {
  return (
    // 2. Agregamos el contenedor principal
    <div className="inicio-container">
      <div className="inicio-content">
        <h1>Bienvenido a la Administración de Campos</h1>
        <p>Esta es la página de inicio de la aplicación.</p>
        <button className="btn btn-primary">Registrar Nuevo Campo</button>
      </div>
    </div>
  );
}

export default Inicio;
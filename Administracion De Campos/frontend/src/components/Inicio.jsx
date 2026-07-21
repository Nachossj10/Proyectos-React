import React from 'react';
import '../styles/Inicio.css';
import {useNavigate} from 'react-router-dom';

function Inicio() {
  const navigate = useNavigate();

  const handleRegistrarCampo = () => {
    navigate('/RegistrarCampo');
  };

  return (
    // 2. Agregamos el contenedor principal
    <div className="inicio-container">
      <div className="inicio-content">
        <h1>Bienvenido a la Administración de Campos</h1>
        <p>Esta es la página de inicio de la aplicación.</p>
        <button className="btn btn-primary" onClick={handleRegistrarCampo}>Registrar Nuevo Campo</button>
      </div>
    </div>
  );
}

export default Inicio;
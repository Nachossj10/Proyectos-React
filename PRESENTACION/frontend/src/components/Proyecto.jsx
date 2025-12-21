import React from 'react';
import gstEnv from '../assets/gstEnv.png';
import redSSl from '../assets/redSSL.png';
import '../styles/Proyecto.css';

function Proyectos() {
  return (
    <div className='card'>
      <h2>Mis Proyectos</h2>
      <div className="card-group">
        <div className='card rounded-lg mini-card m-3 p-3'>
          <img src={gstEnv} alt="Gestion de Envios" />
          <div className="card-body">
            <h5 className="card-title">Gestor de Envios</h5>
            <p className="card-text">Aplicación web full-stack desarrollada con React.js, Node.js, Express, MySQL y JavaScript. Permite a los usuarios gestionar envíos, crear órdenes y crear nuevos usuarios.
              También cuenta con seguridad mediante autenticación JWT y manejo de sesiones.</p>
            <a href="https://github.com/Nachossj10/Proyectos-React/tree/main" target='_blank' className='btn custom-btn'>¡Vamos a verlo!</a>
          </div>
        </div>
        <div className="card rounded-lg mini-card m-3 p-3 rounded-sm">
          <img src={redSSl} alt="Red Social" />
          <div className="card-body">
            <h5 className="card-title">Mini-Red Social</h5>
            <p className="card-text">Desarrollo de una mini-red social utilizando React.js para el frontend y JavaScript, express y Sqlite para el backend. La aplicación permite a los usuarios registrarse, visualizar la informacion de otros usuarios, comentar en las publicaciones de otros usuarios, como a la vez borrar comentarios y publicaciones.</p>
            <a href="https://github.com/Nachossj10/Proyectos-React/tree/main" target='_blank' className='btn custom-btn'>¡Vamos a verlo!</a>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Proyectos;
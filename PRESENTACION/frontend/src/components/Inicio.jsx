import React from 'react';
import '../styles/Inicio.css';
import perfilImage from '../assets/perfil.jpg';
import { Tecnologia } from './Tecnologia';

function AcercaDeMi() {
  return (
    <div className='card my-4'>
      <h1>Acerca De Mi</h1>
      <div className="card-body">
        <p>Mi nombre es Juan Ignacio Vaca, tengo 22 años, actualmente soy estudiante de tercer año de ingeniería en sistemas de información. Tengo conocimientos básicos sobre programación full-stack de desarrollo web y administración de bases de datos, con buena predisposición para el aprendizaje

Aunque aún no cuento con experiencia laboral formal, me motiva seguir desarrollando mis habilidades técnicas y aprovechar cada oportunidad que me permita crecer profesionalmente.

Soy una persona curiosa, responsable y orientada al detalle, lo que me impulsa a resolver problemas de manera lógica y eficiente. 
Mi objetivo es incorporarme a un entorno donde pueda aportar compromiso y dedicación, al mismo tiempo que adquiero experiencia práctica en el área de tecnología y desarrollo de software.
Estoy abierto a oportunidades que me permitan continuar formándome, especialmente en roles relacionados con programación, análisis de datos y administración de bases de datos
</p>
      </div>
    </div>
  )
}


function Inicio() {
  return (
    <div className="inicio-container">
      <h1 className='pb-4' style={{color: 'white'}}>Bienvenidos a mi Perfil Profesional</h1>
      <div className='card'>
        <img src={perfilImage} alt="foto de perfil" className='perfil-foto card-img-top' />
        <div className='card-body'>
          <h5 className='card-title'>Juan Ignacio Vaca</h5>
          <p className='card-text'>Estudiante avanzado en la carrera de Ingenieria en Sistemas de Información</p>
        </div>
      </div>
      <AcercaDeMi />
      <Tecnologia />
    </div>
    
  )
}



export { Inicio }
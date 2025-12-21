import React from 'react';
import '../styles/Tecnologia.css';
import bootstrapLogo from '../assets/bootstrap.png'
import expressLogo from '../assets/expressjs.svg'
import javascriptLogo from '../assets/js.png'
import reactLogo from '../assets/react.svg'
import gitLogo from '../assets/Git_icon.png'
import oracleLogo from '../assets/oracle.png'
import pythonLogo from '../assets/python.png'
import sqlLogo from '../assets/Sql.png'

function Tecnologia() {
  return (
    <div className="tecnologia-card py-4" style={{color: 'white'}}>
      <h2>Tecnologías y Herramientas</h2>
      <p>Cuento con sólidos conocimientos en las siguientes tecnologías y herramientas</p>
      <div className="tech-row" role="list">
        <img className="tech-img" src={bootstrapLogo} alt="Bootstrap" role="listitem" />
        <img className="tech-img" src={expressLogo} alt="Express.js" role="listitem" />
        <img className="tech-img" src={javascriptLogo} alt="JavaScript" role="listitem" />
        <img className="tech-img" src={reactLogo} alt="React" role="listitem" />
        <img className="tech-img" src={gitLogo} alt="Git" role="listitem" />
        <img className="tech-img" src={oracleLogo} alt="Oracle" role="listitem" />
        <img className="tech-img" src={pythonLogo} alt="Python" role="listitem" />
        <img className="tech-img" src={sqlLogo} alt="SQL" role="listitem" />
      </div>
    </div>
  )
}

export { Tecnologia }
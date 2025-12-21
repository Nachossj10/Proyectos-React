import { useEffect, useState } from "react";
import '../styles/Reloj.css';

function Reloj() {
  const [fechaHora, setFechaHora] = useState(new Date());

  useEffect(() => {
    const intervalo = setInterval(() => {
      setFechaHora(new Date());
    }, 1000);

    return () => clearInterval(intervalo);
  }, []);

  return (
    <div className="reloj">
      <h2>{fechaHora.toLocaleDateString("es-AR")}</h2>
      <h2>{fechaHora.toLocaleTimeString("es-AR", { hour12: false })}</h2>
    </div>
  );
}

export default Reloj;
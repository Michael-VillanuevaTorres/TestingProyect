import React from "react";
import ReportesDev from "../components/ReportesDev";
import ListaRPDev from "./ListaRPDev";
import SearchBar from "../components/SearchBar";
import HeaderDev from '../components/HeaderDev';

type Props = {};




const Dev = (props: Props) => {
    return (
      <div>
        <HeaderDev></HeaderDev>
        <br />
        <ReportesDev></ReportesDev>
        
      </div>
    );
  };
  
  export default Dev;
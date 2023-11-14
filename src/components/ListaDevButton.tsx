import * as React from 'react';
import { useState, useEffect} from 'react';
import  { Button,Modal,Form } from 'react-bootstrap';
import { useForm, SubmitHandler } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { MDBTable, MDBTableBody, MDBTableHead } from 'mdbreact';
import AsignacionButton from './AsignacionButton';
import './ListaDevButton.css'
import CambiarPrioridadButton from './CambiarPrioridadButton';


interface IListaDevButtonProps {
  id_dev: number;
  id_producto: number;
};

type FormValues = {
  motivo: string;
};

type reporte = {
  id: number;
  title:string;
  description:string;
  likes:number;
  date:string;
  id_state: number;
  id_priority: number;
  id_product: number;
};

type producto = {
  name: string;
  id: number;
  id_developer: number;
};
type prioridad = {
  id: number;
  name: string;
};

const getData = (id_dev: number, id_product: number) => {
  const [datos, setUsers] = useState([]);
  const [devInfo, setDevInfo] = useState([]);
  const [productInfo, setProductInfo] = useState([]);

  const fetchUserData = () => {
    fetch("http://127.0.0.1:5000/developer/reports?id_dev=" + id_dev)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setUsers(data);
      });
  };

  const fetchDevInfo = () => {
    fetch("http://127.0.0.1:5000/developer/get?id_dev=" + id_dev)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setDevInfo(data);
      });
  };

  const fetchProductData = () => {
    fetch("http://127.0.0.1:5000/product/get?id_product=" + id_product)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setProductInfo(data);
      });
  };

  useEffect(() => {
  
    return () => {
      fetchUserData();
      fetchDevInfo();
      fetchProductData();
    };
  }, []);
  console.log(datos,devInfo,productInfo);
  return [datos, devInfo, productInfo];
};


const getPrioridades = (): prioridad[] => {
  const [prioridades, setPrioridades] = useState<prioridad[]>([]);

  useEffect(() => {
    const fetchPrioridades = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/report/priority/all');
        if (response.ok) {
          const data = await response.json();
          console.log(data)
          setPrioridades(data);
        } else {
          console.error('Failed to fetch prioridades');
        }
      } catch (error) {
        console.error('An error occurred while fetching prioridades:', error);
      }
    };
    
    fetchPrioridades();
  }, []); // Empty dependency array to run the effect only once

  return prioridades;
};
const ListaDevButton: React.FunctionComponent<IListaDevButtonProps> = ({ id_dev, id_producto }) => {
  const [show, setShow] = useState(false);
  const [products, setProducts] = useState([]);
  const prioridades = getPrioridades();



  const getPrioridadNombre =(id:number) =>{
    const  prio = prioridades.find((item: prioridad) => item.id === id);
    if (!prio) {
      return <h5 className="prioridadCero">NO ASIGNADO</h5>;
    } else if (prio.id === 0) {
      return <h5 className="prioridadCero">{prio.name.toUpperCase()}</h5>;
    } else if (prio.id === 1) {
      return <h5 className="prioridadUno">{prio.name.toUpperCase()}</h5>;
    } else if (prio.id === 2) {
      return <h5 className="prioridadDos">{prio.name.toUpperCase()}</h5>;
    } else if (prio.id === 3) {
      return <h5 className="prioridadTres">{prio.name.toUpperCase()}</h5>;
    } else {
      return <h5 className="prioridadCero">NO ASIGNADO</h5>;
    }
  };


  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  useEffect(() => {

  
    fetch("http://127.0.0.1:5000/product/get/all")
      .then((response) => response.json())
      .then((data) => setProducts(data));
  }, []);

  const getProductIds = () => {
    return products
      .filter((producto: producto) => producto.id_developer === 1)
      .map((item: producto) => item.id);
  };
  

  const productIds = getProductIds();
  const [datos,devInfo,productInfo] = getData(id_dev, id_producto);

  const reports = datos
    .filter((report :reporte) => report.id_product == (id_producto))
    .map((report: reporte) => {
      return {
        titulo: <Button href={"/VerReporteEnv/" + report.id} variant="link">{report.title}</Button>,
        prioridad: getPrioridadNombre(report.id_priority),
        likes: report.likes,
        fecha: report.date,
        producto: report.id_product,
        reasignacion: <AsignacionButton id_report={report.id}></AsignacionButton>,
        cambiarprioridad: <CambiarPrioridadButton id={report.id}></CambiarPrioridadButton>
      };
    });

  const data = {
    columns: [
      {
        label: 'Titulo',
        field: 'titulo',
        sort: 'asc'
      },
      {
        label: 'Prioridad',
        field: 'prioridad',
        sort: 'asc'

      },
      {
        label: 'Likes',
        field: 'likes',
        sort: 'asc'
      },
      {
        label: 'Fecha',
        field: 'fecha',
        sort: 'asc'
      },
      {
        label: 'Producto',
        field: 'producto',
        sort: 'asc'
      },
      {
        label: 'Reasignar',
        field: 'reasignacion',
        sort: 'asc'
      }
    ],
    rows: reports
  };


  return (
    <>
      <Button variant="success" onClick={handleShow}>
      Asignados
      </Button>

      <Modal show={show} onHide={handleClose} dialogClassName="modal-dialog modal-xl">
        <Modal.Header closeButton>
          <Modal.Title className="text-black">Reportes asignados al desarrollador {devInfo['name']} en el proyecto {productInfo['name']}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
        <MDBTable scrollY maxHeight='70vh'>
                <MDBTableHead columns={data.columns} />
                <MDBTableBody rows={data.rows} />
        </MDBTable>
        </Modal.Body>
      </Modal>
    </>
  );
}

export default ListaDevButton;
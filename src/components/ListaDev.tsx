import * as React from 'react';
import {Stack, Card, Container } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import { MDBTable, MDBTableBody, MDBTableHead } from 'mdbreact';
import ListaDevButtonEncargado from './ListaDevButtonEncargado';
import "./ReportTable.css";
import "./PrioridadesModal.css";
import Product from './Product';
import ListaDevButton from './ListaDevButton';
type Modal = React.ReactNode; 

interface IListaDevProps { }

type Dev = {
  id: number;
  name: string;
  email: string;
  num_reportes: string;
  modal: Modal;
}
type prioridad = {
  id: number;
  name: string;
};

type producto = {
  name: string;
  id: number;
  id_developer: number;
}


const useDevData = (url: string, id_product: number) => {
  const [datos, setUsers] = useState<Dev[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${url}?id_product=${id_product}`);
        const data = await response.json();
        setUsers(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();


    return () => {
      fetchData();
    };
  }, [url, id_product]);

  return datos;
};

const ListaDev: React.FunctionComponent<IListaDevProps> = (props) => {
  const [id_product, setId_product] = useState<number>(1);
  const [devs, setDevs] = useState<Dev[]>([]);

  const selectChange = async (event: React.ChangeEvent<HTMLSelectElement>) => {
    setId_product(parseInt(event.target.value, 10));
  };

  const datos = useDevData('http://127.0.0.1:5000/product/get/developers/all', id_product);

  const fetchNumReports = async (devId: number) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/developer/number/product/reports/all?id_dev=${devId}&id_product=${id_product}`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching num_reports data:', error);
    }
  };


  const fetchDevData = async () => {
    const devs = datos.map(async (dev: Dev) => {
      const num_rep = await fetchNumReports(dev.id);

      return {
        id:dev.id,
        nombre: dev.name,
        email: dev.email,
        num_reportes: num_rep.total_reports + ' (' + num_rep.product_reports + ')',
        modal: <ListaDevButton id_dev={dev.id} id_producto={id_product}></ListaDevButton>,
      };
    });

    const updatedDevs = await Promise.all(devs);
    return updatedDevs;
  };

  

  useEffect(() => {
    const fetchData = async () => {
      const updatedDevs = await fetchDevData();
      setDevs(updatedDevs);
    };
    fetchData();
    console.log("se realiza la actualizacion")
  }, [datos, id_product]);

  const getProducts = () => {
    const [products, setProducts] = useState([]);
  
    useEffect(() => {
      fetch("http://127.0.0.1:5000/product/get/all")
        .then((response) => response.json())
        .then((data) => setProducts(data));
    }, []);
    
    const productos = products.filter((producto:producto) => producto.id_developer === 1).map((item: producto) =>{
      return {
        nombre:item.name, id:item.id
        }
      });
      console.log(productos)
    return productos;
  };

  useEffect(() => {
    
  }, []);


  const data = {
    columns: [
      {
        label: 'Nombre',
        field: 'nombre',
        sort: 'asc',
      },
      {
        label: 'Email',
        field: 'email',
        sort: 'asc',
      },
      {
        label: 'Reportes(Producto)',
        field: 'num_reportes',
        sort: 'asc',
      },
      {
        label: 'Reportes',
        field: 'modal',
        sort: 'asc',
      },
    ],
    rows: devs,
  };

  const products=getProducts();
  return (
    <Container>
      <Card style={{ width: '43rem', height: '20rem'}}>
        <Card.Body>
          <Stack direction="horizontal" gap={3}>
            <div >
              <Card.Title className="text-black">Desarrolladores de :</Card.Title>
            </div>
            <div>
              <select id='producto_desarolladores' name="Producto" onChange={selectChange}>
                {products.map((product) => (
                  <option key={product.id} value={product.id}>
                    {product.nombre}
                  </option>
                ))}
              </select>
            </div>
          </Stack>

          <div style={{ width: '41rem', height: '15rem', overflowY: 'scroll' }}>
                <MDBTable >
                  <MDBTableHead  columns={data.columns} />
                  <MDBTableBody>
                    {data.rows.filter((row) => row).map((row, index) => (
                      <tr className={"row-developer"+row.id} key={index} data-custom="hidden data">
                        <td className={"nombre"+row.id} >{row.nombre}</td>
                        <td className={"email"+row.id}>{row.email}</td>
                        <td className={"num_reportes"+row.id}>{row.num_reportes}</td>
                        <td className={"modal"+row.id}>{row.modal}</td>
                      </tr>
                    ))}
                  </MDBTableBody>
                </MDBTable>
          </div>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default ListaDev;
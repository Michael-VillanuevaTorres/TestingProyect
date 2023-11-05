class Product {
  name: string;
  id: number;
  id_developer: number;
  constructor(
    nombre = "vacio",
    id = -1,
    id_developer = -1,
  ) {
    this.name = nombre;
    this.id = id;
    this.id_developer = id_developer;
  }
}

export default Product;

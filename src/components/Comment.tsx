class Comment {
    content: string;
    date: string;
    id: string;
    constructor(
      contenido = "vacio",
      date = "vacio",
      id = "vacio"
    ) {
      this.content = contenido;
      this.date = date;
      this.id = id;
    }
  }
  
  export default Comment;
  
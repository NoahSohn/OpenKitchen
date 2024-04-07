import "./navbar.css"
import React,{useEffect} from 'react';
import {Navbar, Container, Nav} from 'react-bootstrap';

const MyNavbar = () => {
  return (<Navbar bg="dark" data-bs-theme="dark" sticky="top">
        <Container>
          <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
            <Nav.Link href="#pricing">Pricing</Nav.Link>
          </Nav>
        </Container>
      </Navbar>)
}
        // <div className="logo">
        //   <img src={Logo} alt="Logo" title="Logo" />
        // </div>

export default MyNavbar 

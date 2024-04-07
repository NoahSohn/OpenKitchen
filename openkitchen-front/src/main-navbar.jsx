import "./navbar.css"
import React,{useEffect} from 'react';
import {Navbar, Container, Nav} from 'react-bootstrap';
import "./image-resize.css"
import Button from "./Button";

const MyNavbar = (AccountName, AccountIcon) => {
    return (
    <nav className="navbar navbar-dark navbar-expand-lg" style={{backgroundColor: "#333333"}}> 
        <a className="navbar-brand" href="/home"><img src="logo.png" alt="Logo" width="30" height="24"/></a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-center" id="navbarSupportedContent">
          <ul className="navbar-nav mb-2 mb-lg-0">
            <li className="nav-item">
              <a className="nav-link" href="/create">
                <Button isPressed={false} onClick={()=>{}} text="New recipe" defaultStyle="default-button" pressedStyle="pressedButton" defaultImg="new_recipe_unpressed.png" pressedImage="search_pressed.png"/> 
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/search">
                <Button isPressed={false} onClick={()=>{}} text="Search" defaultStyle="default-button" pressedStyle="pressedButton" defaultImg="search_unpressed.png" pressedImage="search_pressed.png"/> 
              </a>
            </li>
          </ul>
        </div>
    </nav>)
    }

export default MyNavbar 

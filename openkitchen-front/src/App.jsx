import { useState } from 'react'
import SearchBar from './search.jsx'
import Button from "./Button.jsx"
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter, RouterProvider,
} from "react-router-dom";
import MyNavbar from './main-navbar.jsx'
import './App.css'
import './Button.css'
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (
    <>
      <MyNavbar/>
    </>
  );
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>
  },
 {
    recipe: "/recipe",
    element: 
 },
]);

export default router 

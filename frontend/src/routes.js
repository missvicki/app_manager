import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Login from "./pages/Login.js";
import Home from "./pages/Home.js";
import Info from "./pages/Info.js";
import Settings from "./pages/Settings.js";
import Navbar from "./components/Navbar";
import './style_sheets/App.css';

function PathRoutes() {
  return (
      <div className="App">
        <BrowserRouter>
          <Navbar />
          <Routes>
          <Route path="/login" element={<Login/>} />
          <Route path="/" element={<Home/>} />
          <Route path="/info" element={<Info/>} />
          <Route path="/settings" element={<Settings/>} />
          </Routes>
        </BrowserRouter>
      </div>
  );
}

export default PathRoutes;



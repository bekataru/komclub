import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import '../Style/Layout.css';
import Logo from '../assets/images/logo.png';
const Layout = () => {
  return (
    <div className="layout">
      <header>
        <nav className="navigation">
          <ul className="navigation-bar">
            <img className="komclub-logo" src={Logo} alt="KomClub"></img>
            <li className="navigation-bar-item"><Link to="/">Home</Link></li>
            <li className="navigation-bar-item"><Link to="/about">About</Link></li>
          </ul>
        </nav>
      </header>
      
      <main>
        <Outlet />
      </main>
      
      <footer>
        <p>© {new Date().getFullYear()} My React App</p>
      </footer>
    </div>
  );
};

export default Layout;
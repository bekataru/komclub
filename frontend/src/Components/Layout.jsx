import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const Layout = () => {
  return (
    <div className="layout">
      <header>
        <nav>
          <ul style={{ display: 'flex', listStyle: 'none', gap: '1rem' }}>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/about">About</Link></li>
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
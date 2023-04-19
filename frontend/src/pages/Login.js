import React from 'react';
import '../style_sheets/login.css';

function Login() {
  return (
    <div className="Login">
      <header className="Login-header">
        <h1>
          Duke Development Tracker
        </h1>
        <button class = "signin-btn">Sign in</button>
      </header>
    </div>
  );
}

export default Login;

import React from "react";
import { Link } from "react-router-dom";

export default function NavBar(){
  return (
    <nav style={{display:"flex", gap:20, padding:10, background:"#0b4f6c", color:"white"}}>
      <Link to="/" style={{color:"white", textDecoration:"none", fontWeight:700}}>FinSight</Link>
      <Link to="/dashboard" style={{color:"white", textDecoration:"none"}}>Dashboard</Link>
    </nav>
  );
}

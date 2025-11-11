import React from "react";

export default function Home(){
  return (
    <div style={{textAlign:"center", marginTop:60}}>
      <h1 style={{fontSize:64, margin:0}}>FinSight</h1>
      <p style={{fontSize:18, color:"#333"}}>Financial Fraud & Risk Analytics System</p>

      <div style={{maxWidth:900, margin:"40px auto", textAlign:"left"}}>
        <h3>Overview</h3>
        <p>Welcome to FinSight — a demo analytics system for detecting and visualizing financial fraud. Use the Dashboard to view real-time analytics and reports.</p>
      </div>
    </div>
  );
}

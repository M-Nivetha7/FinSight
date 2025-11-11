import React from "react";

export default function Dashboard(){
  // POWER_BI_EMBED_URL will be provided after you publish the report or use a placeholder
  const embedUrl = import.meta.env.VITE_POWER_BI_EMBED_URL || "about:blank";

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Power BI report embed (placeholder). Replace the src with your Power BI embed URL or use Power BI Embedded SDK for secure embed.</p>

      <div style={{height:600, border:"1px solid #ddd"}}>
        {/* Simple iframe embed — replace with secure embed in production */}
        <iframe
          title="PowerBI"
          src={embedUrl}
          style={{width:"100%", height:"100%", border:0}}
        />
      </div>
    </div>
  );
}

"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState<string>("checking...");

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/health`)
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("backend unreachable"));
  }, []);

  return (
    <main style={{ fontFamily: "system-ui", padding: "4rem", maxWidth: 640 }}>
      <h1>IDAP</h1>
      <p>Intelligent Data Analytics Platform — Take 1 skeleton.</p>
      <p>
        Backend status: <strong>{status}</strong>
      </p>
    </main>
  );
}

import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "IDAP — Intelligent Data Analytics Platform",
  description: "Enterprise SaaS Data Analytics Platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

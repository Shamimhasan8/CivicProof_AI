import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata={title:'CivicProof AI — Evidence before action',description:'Independent citizen service evidence and accountability platform. A synthetic demonstration for Bangladesh e-Passport re-issue.',icons:{icon:'/favicon.svg'}};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="bn"><body>{children}</body></html>}

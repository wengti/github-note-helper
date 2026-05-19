import type { Metadata } from "next";
import { Outfit, Roboto } from "next/font/google";
import "./globals.css";
import React from "react";
import ThemeContextProvider from "@/context/ThemeContextProvider";
import Body from "@/components/body/Body";

const outfit = Outfit({
    subsets: ['latin'],
})

export const metadata: Metadata = {
    title: "GitHub Note Helper",
    description: "A RAG-based Chat Bot that generates grounded answer based on the GitHub notes",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en" className={`${outfit.className} h-full`}>
            <ThemeContextProvider>
                <Body>
                    {children}
                </Body>
            </ThemeContextProvider>
        </html>
    );
}

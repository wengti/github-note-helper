'use client'

import { ThemeContext } from "@/context/ThemeContextProvider"
import React, { useContext } from "react"

export default function Body({children}: {children: React.ReactNode}){
    const [isDark, setIsDark] = useContext(ThemeContext)

    const isDarkClsName = isDark ? 'dark' : ''

    return (
        <body className={`h-full ${isDarkClsName}`}>
            {children}
        </body>
    )

}
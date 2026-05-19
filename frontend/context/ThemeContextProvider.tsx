'use client'

import React, { createContext, useEffect, useRef, useState } from "react";



export const ThemeContext = createContext<[boolean, React.Dispatch<React.SetStateAction<boolean>>]>([true, null!])

export default function ThemeContextProvider({children}: {children: React.ReactNode}){

    function getThemeFromLS() {
        const storedTheme = localStorage.getItem("gnh-theme")
        return storedTheme
    }

    const [isDark, setIsDark] = useState<boolean>(true)
    const [isMounted, setIsMounted] = useState<boolean>(false)

    useEffect( () => {
        const storedThemeVal = getThemeFromLS()
        if(storedThemeVal){
            setIsDark(JSON.parse(storedThemeVal))
        }
        setIsMounted(true)
    })

    return (
        isMounted ?
            <ThemeContext value={[isDark, setIsDark]}>
                {children}
            </ThemeContext> :
            <body className='bg-(--background-black)'>
            </body>
    )
}
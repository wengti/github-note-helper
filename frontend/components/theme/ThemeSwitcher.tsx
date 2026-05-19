'use client'

import { ThemeContext } from "@/context/ThemeContextProvider"
import { useContext } from "react"
import { MdSunny } from "react-icons/md";
import { IoMdMoon } from "react-icons/io";

export default function ThemeSwitcher() {

    const [isDark, setIsDark] = useContext(ThemeContext)

    function handleThemeSwitch() {

        setIsDark( (curVal) => {
            localStorage.setItem("gnh-theme", JSON.stringify(!curVal))
            return !curVal
        })
    }

    return (
        <div
            className='w-fit text-2xl text-(--letter-black) dark:text-(--letter-white)'
            onClick={() => { handleThemeSwitch() }}
        >
            {
                isDark ?
                    <MdSunny /> :
                    <IoMdMoon />
            }
        </div>
    )
}
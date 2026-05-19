'use client'
import { FaArrowDown } from "react-icons/fa6";

export default function ScrollDownToggle() {

    function scrollDown() {
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    }

    return (
        <div
            className='cursor-pointer'
            onClick={() => scrollDown()}
        >
            <FaArrowDown className='font-bold text-2xl'/>
        </div>
    )
}
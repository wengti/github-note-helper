'use client'
import { FaArrowUp } from "react-icons/fa6";

export default function ScrollUpToggle() {

    function scrollUp() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    return (
        <div
            className='cursor-pointer'
            onClick={() => scrollUp()}
        >
            <FaArrowUp className='font-bold text-2xl'/>
        </div>
    )
}
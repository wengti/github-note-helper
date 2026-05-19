'use client'

export default function FooterComponent(){

    const now = new Date()
    const year = now.getFullYear()

    return (
        <footer className='flex items-center justify-center bg-(--banner-blue) dark:bg-(--banner-black) h-(--footer-height)'>
            <p>Wong Weng Ti @ {year}</p>
        </footer>
    )
}
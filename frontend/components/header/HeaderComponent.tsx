import Image from "next/image";
import ThemeSwitcher from "../theme/ThemeSwitcher";

export default function HeaderComponent(){

    return (
        <header className='p-4 bg-(--banner-blue) dark:bg-(--banner-black) h-(--header-height)'>
            <div className='flex justify-between'>
                <div className='flex gap-4 items-end'>
                    <Image 
                        src='/gnh-dark-icon.png'
                        width={240}
                        height={240}
                        alt="The icon of the website"
                        className='w-20 hidden dark:block'
                    />
                    <Image 
                        src='/gnh-light-icon.png'
                        width={240}
                        height={240}
                        alt="The icon of the website"
                        className='w-20 block dark:hidden'
                    />
                    <h1 className='text-3xl font-extrabold text-(--letter-blue) dark:text-(--letter-white)'>
                        GitHub <br/> Note Helper
                    </h1>
                </div>
                <ThemeSwitcher />
            </div>
        </header>
    )
}
import Image from "next/image"
import Markdown from "react-markdown"

export default function AIMessage({ text }: { text: string }) {

    return (
        <div className='flex items-end'>
            <Image
                src='/gnh-dark-icon.png'
                width={240}
                height={240}
                alt="The bot's avatar"
                className='w-5 h-5 hidden dark:block'
            />
            <Image
                src='/gnh-light-icon.png'
                width={240}
                height={240}
                alt="The bot's avatar"
                className='w-5 h-5 block dark:hidden'
            />
            <div className='max-w-4/5 sm:max-w-3/5 mr-auto ml-2 rounded-xl bg-(--banner-blue) dark:bg-(--banner-black) p-4 wrap-break-word whitespace-pre-wrap prose dark:prose-invert'>
                <Markdown>
                    {text}
                </Markdown>
            </div>
        </div>
    )
}
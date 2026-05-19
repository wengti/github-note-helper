export default function HumanMessage({ text }: { text: string }) {

    return (
        <div className='max-w-4/5 sm:max-w-3/5 ml-auto mr-4 rounded-xl bg-(--banner-neutral) dark:bg-(--banner-neutral-dark) p-4 wrap-break-word whitespace-normal'>
            {text}
        </div>
    )
}
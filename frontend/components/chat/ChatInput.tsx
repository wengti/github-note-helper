'use client'
import { Dispatch, KeyboardEvent, SetStateAction, useState } from "react";
import { MdSend } from "react-icons/md";
import { MessageType } from "./ChatBox";

export default function ChatInput({ setMessages }: { setMessages: Dispatch<SetStateAction<MessageType[]>> }) {

    const [userInput, setUserInput] = useState<string>('')
    const [error, setError] = useState<null | Error>(null)

    function sendMessageByEnter(event: KeyboardEvent<HTMLTextAreaElement>) {
        if (event.shiftKey) {
        }
        else if (event.key === 'Enter') {
            event.preventDefault()
            sendMessage()
        }
    }

    function sendMessage() {
        setMessages((curMessage) => {
            const newMessage = structuredClone(curMessage)
            newMessage.push({
                role: 'human',
                text: userInput
            })
            return newMessage
        })
        setUserInput('')
    }

    return (
        <div className=''>
            {
                error &&
                <div className='text-red-500 -mb-4'>{error.message}</div>
            }
            <div className='border my-4 flex flex-col rounded-xl'>
                <div className='grow flex'>
                    <textarea
                        className='resize-none grow rounded-l-xl p-1 outline-0'
                        value={userInput}
                        onChange={(event) => setUserInput(event.currentTarget.value)}
                        onKeyDown={(event) => sendMessageByEnter(event)}
                    >
                    </textarea>
                    <button
                        className='bg-(--banner-neutral) dark:bg-(--banner-neutral-dark) w-10 rounded-r-xl flex justify-center items-center hover:opacity-70'
                        onClick={() => sendMessage()}
                    >
                        <MdSend />
                    </button>
                </div>
            </div>
        </div>
    )
}
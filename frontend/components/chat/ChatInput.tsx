'use client'
import { ChangeEvent, Dispatch, KeyboardEvent, SetStateAction, useEffect, useState } from "react";
import { MdSend } from "react-icons/md";
import { MessageType } from "./ChatBox";

export default function ChatInput({ messages, setMessages }: { messages: MessageType[], setMessages: Dispatch<SetStateAction<MessageType[]>> }) {


    /* State */
    const [userInput, setUserInput] = useState<string>('')
    const [error, setError] = useState<null | Error>(null)

    /* Update user input and move window down */
    function updateUserInput(event: ChangeEvent<HTMLTextAreaElement, HTMLTextAreaElement>) {

        setUserInput(event.currentTarget.value)
        setTimeout(() => {
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        }, 0)
    }

    /* Send Message by Enter but still allowing shift + enter to change to newline */
    function sendMessageByEnter(event: KeyboardEvent<HTMLTextAreaElement>) {
        if (event.shiftKey) {
        }
        else if (event.key === 'Enter') {
            event.preventDefault()
            sendMessage()
        }
    }

    /* Send Message */
    function sendMessage() {

        if (userInput === "") {
            setError(new Error("Invalid input"))
            return
        }

        setError(null)

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

    /* Effect - when error / messages change, scroll to bottom */
    useEffect(() => {
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    }, [error, messages])

    /* Components */
    return (
        <div className=''>
            {
                error &&
                <div className='text-red-500 -mb-4'>{error.message}</div>
            }
            <div className='border my-4 flex flex-col rounded-xl'>
                <div className='grow flex'>
                    <textarea
                        className='resize-none grow rounded-l-xl p-1 outline-0 max-h-32 overflow-y-auto'
                        value={userInput}
                        onChange={(event) => updateUserInput(event)}
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
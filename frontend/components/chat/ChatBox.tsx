'use client'
import { useState } from "react";
import ChatInput from "./ChatInput";
import ChatMessages from "./ChatMessages";

export type MessageType = {
    role: 'human' | 'ai'
    text: string
}

export default function ChatBox(){

    const [messages, setMessages] = useState<MessageType[]>([])

    return (
        <section className='min-h-(--content-min-height) mx-2 sm:mx-10 flex flex-col justify-end'>
            <ChatMessages messages={messages}/>
            <ChatInput setMessages={setMessages}/>
        </section>
    )
}
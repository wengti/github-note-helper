'use client'
import { useState } from "react";
import ChatInput from "./ChatInput";
import ChatMessages from "./ChatMessages";

export type MessageType = {
    role: 'human' | 'ai'
    text: string
}

export default function ChatBox(){

    const initialMessage: MessageType = {
        role: 'ai',
        text: 'I have access to a vector knowledge base of LCEL, LangChain and LangGraph.\nBut you can ask me anything even beyond that!'
    }
    const [messages, setMessages] = useState<MessageType[]>([initialMessage])

    return (
        <section className='min-h-(--content-min-height) mx-2 sm:mx-10 flex flex-col justify-end'>
            <ChatMessages messages={messages}/>
            <ChatInput messages={messages} setMessages={setMessages}/>
        </section>
    )
}
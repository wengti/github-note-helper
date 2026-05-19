import AIMessage from "./AIMessage";
import { MessageType } from "./ChatBox";
import HumanMessage from "./HumanMessage";

export default function ChatMessages({messages}: {messages: MessageType[]}){

    return (
        <div className='grow flex flex-col justify-end gap-3 my-3'>
            {messages.map( (message, idx) => {
                const {role, text} = message
                if (role === 'human') return <HumanMessage text={text} key={idx}/>
                else if (role === 'ai') return <AIMessage text={text} key={idx}/>
            })}
        </div>
    )
}
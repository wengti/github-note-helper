import ChatBox from "@/components/chat/ChatBox";
import FooterComponent from "@/components/footer/FooterComponent";
import HeaderComponent from "@/components/header/HeaderComponent";

export default function HomeComponent() {


    return (
        <div className='h-full bg-white dark:bg-black text-(--letter-black) dark:text-(--letter-white)'>
            <HeaderComponent />
            <ChatBox />
            <FooterComponent />
        </div>
    )
}
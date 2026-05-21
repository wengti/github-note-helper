# GitHub Note Helper
GitHub Note Helper is a RAG-based chatbot assistant that always provide grounded answer to the user with proper citation.
It has access to a vector database consisting of vector embeddings embedded from personal GitHub notes and a Tavily Search Tool.

## Demo
* Live Implementation: https://github-note-helper.vercel.app/
* Demo Video: https://www.youtube.com/watch?v=pL9cRjuaZUo

![Dark Mode on Landing](/demo/1.png)
![Dark Mode on Chat](/demo/2.png)
![Light Mode on Landing](/demo/3.png)
![Light Mode on Landing](/demo/4.png)

## Tech Stack
* Frontend: Next.js and TailwindCSS
* Backend: FastAPI
* AI: LangChain, LangGraph, Pinecone

## RAG Architecture
![RAG Architecture](/backend/graph.png)
It also features a RAG architecture that performs a multi-step workflow including:
1. **Query Refiner Node**
    * Interpret and refine a precise search key word from the chat history
2. **Router Node**
    * Decide whether to search online or from vector database
3. **Retriever Node**
    * Retrieve relevant vector embedding
4. **Retriever Grader Node**
    * Determine whether all the retrieved vector embeddings are relevant to the query
    * Redirect to web search node if any of them are not relevant
5. **Web Search Node**
    * Perform web search to collect real time latest information
6. **Response Generator Node**
    * Formulating a response based on the collected information / context
7. **Hallucination Grader Node**
    * Verify if the generated response contains content outside of the provided context
    * If so, redirects to response generator for regeneration
8. **Usefulness Grader Node**
    * Verify if the generated response is useful for the user query.
    * If not useful, it will be redirected to the web search node to perform a wider-scoped

To learn more regarding LangChain, LangGraph and RAG, visit: https://github.com/wengti/langchain-tutorial


## Some takeaways:
1. Render AI response in markdown format
    * Packages required:
    ```bash
    npm install react-markdown
    ```

    * Add the following lines to `globals.css`
    ```css
    @plugin "@tailwindcss/typography";
    ```

    * Applying it on the components 
        - wrap markdown in a `div` because it cant accept className attribute.
        - `prose` and `dark:prose-invert` handles markdown styling
    ```tsx
    import Markdown from "react-markdown"

    <div className='prose dark:prose-invert'>
        <Markdown>
            {text}
        </Markdown>
    </div>
    ```

2. How to deploy a FastAPI app on Render using `uv`
    * to build: `uv sync`
    * to start the server: `uv run fastapi run main.py --host 0.0.0.0`

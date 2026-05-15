from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

from langchain.prompts import PromptTemplate


def create_chatbot(vectorstore):

    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-large",
        max_new_tokens=256,
        temperature=0.2
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    template = """
    You are an intelligent HR assistant.

    Answer ONLY from the provided context.

    If answer is not present in context, say:
    "Answer not found in document."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    QA_PROMPT = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": QA_PROMPT},
        return_source_documents=True
    )

    return chain
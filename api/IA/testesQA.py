from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.document_loaders import DirectoryLoader, UnstructuredFileLoader, PyPDFLoader
from langchain.embeddings import LlamaCppEmbeddings
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms.llamacpp import LlamaCpp
from langchain.chains import RetrievalQA, RetrievalQAWithSourcesChain

"""
Carregamos o documento em um formato que a langchain consiga trabalhar.

Separamos o documento em pedaços para que possa ser processado depois pelo modelo.

Retornamos esses pedaços
"""


def preparing_documents(path):
    loader = DirectoryLoader(path, glob='*.pdf', loader_cls=PyPDFLoader)

    docs = loader.load()

    text_splitter = CharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100,
        length_function=len
    )

    splits = text_splitter.split_documents(docs)
    return splits


"""
Criando um banco de dados de vetores para armazenar os splits.

Armazenamos os splits como embeddings. Embeddings são textos transformados em números.
"""


def create_vector_db(splits, embedding, persist_directory):
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embedding,
        persist_directory=persist_directory
    )

    vectordb.persist()
    vectordb = None


def excloi(vectordb):
    vectordb.delete_collection()


"""
Carregando o banco de vetores
"""


def load_vector_db(pathDirectory, embedding):
    persist_directory = pathDirectory

    vectordb = Chroma(
        embedding_function=embedding,
        persist_directory=persist_directory,
    )
    return vectordb


def delete_documents(vectordb):
    vectordb.delete_collection()


"""
Recuperando os splits
"""


def retriever(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 1})
    return retriever


"""
Recuperando os splits
"""


def callback_manager():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    return callback_manager


"""
Carregando o modelo com os parâmetros necessários
"""


def return_llm(callback_manager, path):
    llm = LlamaCpp(
        model_path=path,
        temperature=0.0,
        n_gpu_layers=35,
        n_batch=512,
        n_threads=18,
        n_ctx=4096,
        repeat_penalty=1.1,
        top_k=10,
        top_p=0.5,
        max_tokens=1024,
        callback_manager=callback_manager
    )
    return llm


"""
Criando um template para o modelo
"""


def template():
    template = """Use some parts of summaries to make a answer. Make a answer that make sense with the summaries and 
    question. Use only the necessary to answer the question NOTHING ELSE. Do not reply using a complete sentence. You 
    are a assistant created to answer questions about Cartão Corporate and your name is Luiza. Be polite and fine.

        {summaries}

        {question}

        Answer only in Brazilian Portuguese:
    """

    prompt = PromptTemplate(
        input_variables=["question", "summaries"], template=template
    )
    return prompt


"""
Processamento para o retorno da resposta 
"""


def answer(llm, prompt, retriever, query):
    qa_stuff = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        verbose=True,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )

    response = qa_stuff(query, return_only_outputs=True)
    return response




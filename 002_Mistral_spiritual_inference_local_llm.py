import os
# import langchain.chains.LLMChain
from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
import chainlit as cl

local_llm = "mistral-trismegistus-7b.Q8_0.gguf"


config = {
    'max_new_tokens': 2048,
    'repetition_penalty': 1.1,
    'temprature': 0.5,
    'top_k': 50,
    'top_p': 0.9,
    'stream':False,
    # 'threads': 18

}

llm_init = CTransformers(
    model = local_llm,
    model_type = "mistral",
    # lib = "avx2",
    
    gpu_layers=50,

    **config
)

print(llm_init)

query = "What is the spiritual   meaning of life"

result =llm_init(query)
print(result)

# Give it customized prompt like you are an astrologer aND PEOPLE ARE PRESENTING YOU THEIR BIRTH REPORTS ALONG WITH PROBLEM WHICH THEY ARE FACING IN THEIR LIFE.
# YOU ARE SUPPOSED TO GIVE THEM RIGHT ADVICES
# tRAin on bhagwat geeta ramayana and other shastras to help with people 

template = """Question : {question}
Answer: Let's think step by step and answer it faithfully"""

# @cl.on_chat_start
# def main():
#     prompt = PromptTemplate(template= template, max_token = 1024, input_variables = ["question"])
#     llm_chain = LLMChain(prompt = prompt, llm = llm_init, verbose= True)

#     # Store the chain in user session
#     cl.user_session.set("llm_chain", llm_chain)

# @cl.on_message
# async def main(message: str):
#     #retrueve the chain from the user session
#     llm_chain = cl.user_session.get("llm_chain") 

#     # the the chain asynchronously
#     res = await llm_chain.acall(message, callback=[cl.AsyncLangchainCallbackHandler()])

#     # Return the result
#     await cl.Message(content = res["text"]).send()

# Go ahead and run chainlit run app.py
template = """Question: {question}

Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt = prompt, llm = llm_init, verbose= True)

    # llm_chain = LLMChain(prompt=template, llm=llm_init(temperature=0), verbose=True)

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

    # Call the chain asynchronously
    res = await llm_chain.acall(message, callback=[cl.AsyncLangchainCallbackHandler()])

    # Do any post processing here

    # "res" is a Dict. For this chain, we get the response by reading the "text" key.
    # This varies from chain to chain, you should check which key to read.
    await cl.Message(content=res["text"]).send()
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import asyncio
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
import copy


app = FastAPI(
    title="API Test for Mohamed Bin Zayed University of Artificial Intelligence LaMini",
    description="An API using MBZUAI/LaMini-Flan-T5-77M for Q&A",
    version="0.0.1",
)

# LaMini init
checkpoint = "./model/"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

base_model = AutoModelForSeq2SeqLM.from_pretrained(
    checkpoint,
    # device_map="auto", # for some reason not working with MB Air 202 M1.
    torch_dtype=torch.float32,
)

# Lanchain pipeline init
llm = HuggingFacePipeline.from_model_id(
    model_id=checkpoint,
    task="text2text-generation",
    model_kwargs={
        "temperature": 0.45,
        "min_length": 30,
        "max_length": 350,
        "repetition_penalty": 5.0,
    },
)
template = """{text}"""
prompt = PromptTemplate(template=template, input_variables=["text"])
chat = LLMChain(prompt=prompt, llm=llm)


@app.get("/")
async def root():
    return {"message": "Welcome !!!"}


@app.get("/lamini")
async def lamini(question: str):
    res = chat.run(question)
    result = copy.deepcopy(res)
    return {"result": result}

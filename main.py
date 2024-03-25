from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
import copy

app = FastAPI(
    title="API Test for Mohamed Bin Zayed University of Artificial Intelligence LaMini",
    description="An API using MBZUAI/LaMini-Flan-T5-77M for Q&A",
    version="0.0.1",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize tokenizer and model
checkpoint = "./model/"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(
    checkpoint, torch_dtype=torch.float32
)

# Initialize Langchain pipeline
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
    return {"message": "Welcome to the LaMini API!"}


@app.get("/lamini")
async def lamini(question: str):
    try:
        # Run LaMini
        result = chat.run(question)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

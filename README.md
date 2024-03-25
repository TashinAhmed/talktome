# talktome
Just another PoC with local LLM and FastAPI


## Model Used
- [LaMini-Flan-T5-77M](https://huggingface.co/MBZUAI/LaMini-Flan-T5-77M) for primary execution testing.
- [Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) for actual execution. Planned.


## Tests
- Primary backend test with - FastAPI.
- Python formatter used - Black.
- weight file is ignored for git. can be downladed from this [link](https://huggingface.co/MBZUAI/LaMini-Flan-T5-77M/tree/main), 308 MB in size.

## Project Structure
```
.
└── talktome/
    ├── README.md
    ├── main.py
    └── model/
        ├── weight_file
        └── utilities
```

## Usage


## Flow of completition

### 0.1 
load server:
 ```uvicorn main:app --reload```

run primary test:
 ```python test.py```

# Local ToT

Local ToT is my implementation of Tree of Thought, that allow us can use local model load from huggingface and update requirements is more

## Code Structure

```

tot/
├── config.py
├── main.py
├── models/
│   ├── llm_interface.py
│   └── hf_model.py
├── core/
│   ├── tree_manager.py
│   └── evaluator.py
├── tasks/
│   ├── __init__.py
│   ├── game24.py
│   └── creative_writing.py
├── requirements.txt
└── README.md
```

## Usage

```python
python main.py --task game24 --backend huggingface --hf_model facebook/opt-1.3b
```

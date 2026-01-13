app/
│
├── main.py
├── config.py
│
├── neo4j_client.py          # simple JSON store
│
├── original_processor.py    # extract + store original
├── template_processor.py    # extract_template + fetch_original + resolve_with_llm + fill_template
│
├── workflow.py              # LangGraph ONLY for template
│
└── router.py                # both APIs
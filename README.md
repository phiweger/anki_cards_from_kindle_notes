## README

When reading on the Kindle e-reader, my text annotations feel "lost" most of the time. Here I have GPT rewrite them as learning cards, and format them for direct import into a spaced repetition app called "Anki".

The prompt I use to guide GPT's card writing is a mainly a summarizing paragraph from Andy Matuschak's awesome blog post on ["How to write good prompts"](https://andymatuschak.org/prompts/) plus some further guardrails.


```python
# tested for python 3.10
pip install tqdm jinja2 pandas openai

export OPENAI_API_KEY=sk-...
python generate_cards.py --annotation notes.csv --out cards.csv --language German --replicates 2
```

Now open Anki and:

`"Import file" > select cards.csv > set "Notetype" to "Basic (and reversed card)" > Done.`

Enjoy.
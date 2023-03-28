#! /usr/bin/env python

import argparse
import json
import os
from tqdm import tqdm

from jinja2 import Template
import pandas as pd

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")  # 'sk-...'


def load_prompt(fp):
    """
    Load a prompt in markdown format (this is not enforced) and return as jinja2 template.

    from langchain.prompts import load_prompt

    ... does not support json examples (as in a markdown codeblock)
    """
    s = ""
    with open(fp, "r") as file:
        for line in file:
            s += line
    s = (
        s.strip()
    )  # GPT and other LLMs don't like to start their answers with a leading space
    return Template(s)


parser = argparse.ArgumentParser()
parser.add_argument('--annotation', required=True, help='Text highlights as exported from the Kindle e-reader')
parser.add_argument('--outfile', default='cards.csv', help='File for Anki import')
parser.add_argument('--prompt', default='prompt.md', help='GPT prompt in markdown format with Jinja2 placeholders')
parser.add_argument('--replicates', type=int, default=1, help='Generate that many cards per annotation segment')
parser.add_argument('--language', default='English', help='Language the cards should be in')
parser.add_argument('--tokens', type=int, default=200, help='How many tokens is GPT allowed to generate?')
parser.add_argument('--temperature', type=float, default=0.2, help='How deterministic should the answer be (0 being deterministic)? [0, 1]')
args = parser.parse_args()


def main(args):
    fp_notes = args.annotation
    fp_out = args.outfile
    fp_prompt = args.prompt

    pr = load_prompt(fp_prompt)

    df = pd.read_csv(fp_notes, skiprows=7)

    result = []

    for i in tqdm(df.itertuples()):
        query = i.Annotation
        prompt = pr.render({'annotation': query}, n_examples=args.replicates, language=args.language)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
            max_tokens=args.tokens,
            temperature=args.temperature,
        )
        r = response["choices"][0]["message"]["content"]
        # Validate format.
        try:
            jr = json.loads(r)
            result.append(jr)
        except JSONDecodeError:
            print(f'Card creation not successful for note: {query[:30]}...')
            continue

    # Anki import format: https://docs.ankiweb.net/importing.html
    with open(fp_out, 'w+') as out:
        for i in result:
            for k, v in i.items():
                fwd = v['front']
                rev = v['back']
                out.write(f'{fwd};{rev}\n')


if __name__ == '__main__':
    main(args)







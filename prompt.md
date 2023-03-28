{#
This template uses text from the following awesome introduction to (learning card) prompt construction:

https://andymatuschak.org/prompts/ 
#}
You are a student and want to prepare learning cards for spaced repetition practice.

A learning card has a front and a back page. On the front page there is a question (the "prompt"), to which an answer is formulated on the back.

A learning card expert wrote the following on how to write good prompts:

"Properties of effective retrieval practice prompts: Writing good prompts feels surprisingly similar to translating written text. When translating prose into another language, you're asking: which words, when read, would light a similar set of bulbs in readers' minds? It's not a rote operation. If the passage involves allusion, metaphor, or humor, you won't translate literally. You'll try to find words which recreate the experience of reading the original for a member of a foreign culture. When writing spaced repetition prompts meant to invoke retrieval practice, you're doing something similar to language translation. You're asking: which tasks, when performed in aggregate, require lighting the bulbs which are activated when you have that idea "fully loaded" into your mind? The retrieval practice mechanism implies some core properties of effective prompts. We'll review them briefly here, and the rest of this guide will illustrate them through many examples. These properties aren't laws of nature. They're more like rules you might learn in an English class. Good writers can (and should!) strategically break the rules of grammar to produce interesting effects. But you need to have enough experience to understand why doing something different makes sense in a given context. Retrieval practice prompts should be focused. A question or answer involving too much detail will dull your concentration and stimulate incomplete retrievals, leaving some bulbs unlit. Unfocused questions also make it harder to check whether you remembered all parts of the answer and to note places where you differed. It's usually best to focus on one detail at a time. Retrieval practice prompts should be precise about what they're asking for. Vague questions will elicit vague answers, which won't reliably light the bulbs you're targeting. Retrieval practice prompts should produce consistent answers, lighting the same bulbs each time you perform the task. Otherwise, you may run afoul of an interference phenomenon called "retrieval-induced forgetting". Retrieval practice prompts should be tractable. To avoid interference-driven churn and recurring annoyance in your review sessions, you should strive to write prompts which you can almost always answer correctly. This often means breaking the task down, or adding cues. Retrieval practice prompts should be effortful. It's important that the prompt actually involves retrieving the answer from memory. You shouldn't be able to trivially infer the answer. Cues are helpful, as we'll discuss later—just don't "give the answer away." In fact, effort appears to be an important factor in the effects of retrieval practice. That's one motivation for spacing reviews out over time: if it's too easy to recall the answer, retrieval practice has little effect. Achieving these properties is mostly about writing tightly-scoped questions. When a prompt's scope is too broad, you'll usually have problems: retrieval will often lack a focused target; you may produce imprecise or inconsistent answers; you may find the prompt intractable. But writing tightly-scoped questions is surprisingly difficult. You'll need to break knowledge down into its discrete components so that you can build those pieces back up as prompts for retrieval practice. This decomposition also makes review more efficient. The schedule will rapidly remove easy material from regular practice while ensuring you frequently review the components you find most difficult. Now imagine you've just read a long passage on a new topic. What, specifically, would have to be true for you to say you "know" it? To continue the translation metaphor, you must learn to "read" the language of knowledge—recognizing nouns and verbs, sentence structures, narrative arcs—so that you can write their analogues in the translated language. Some details are essential; some are trivial. And you can't stop with what's on the page: a good translator will notice allusions and draw connections of their own. So we must learn two skills to write effective retrieval practice prompts: how to characterize exactly what knowledge we'll reinforce, and how to ask questions which reinforce that knowledge."

- Pick the single most important fact from the QUERY.
- Formulate a corresponding learning card ONLY ABOUT THE QUERY with a "FRONT" and "BACK" side, taking into account the prompt advice cited above. 
- Do NOT just paraphrase the QUERY.
- Do NOT use any knowledge outside of the QUERY. 
- Do NOT repeat large parts of the FRONT side on the BACK side.
- The BACK side should only contain information that directly relates to the FRONT.
- Be concise.
- Generate up to {{n_examples}} learning cards depending on the length of the QUERY, numbered 1 to {{n_examples}}.
- Return the result as a json formatted string, like:

```json
{
    "1": {
        "front": FRONT here, "back": BACK here
    },
    "2": {
        "front": FRONT here, "back": BACK here
    },
    ...
}
```

The language in which to return your answer is {{language}}.

QUERY: {{annotation}}
ANSWER:
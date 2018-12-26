# Lecture 28: Natural Language Processing (by John Denero!)

## Syntactic Ambiguity in English

- Sentences hold tree recursive characteristics
- Sentences, unlike programming langs, have multiple potential structures and meanings
- Lexical ambiguity: `program` can be noun or a verb

```
Programs must be written for people to read
(for people to read)
(in order that people can read)
(programs can read)
```

## Syntax Trees

- A Tree represents a phrase
    - tag: kind of phrase
    - branches: sequence of Tree or Leaf components
- A Leaf represents a single word
    - tag: kind of word
    - word: the word

## Grammars

### Context-free Grammar rules

A grammar rule describes how a tag can be expanded into a sequence of tags or words.

For example:

```
S –> NP VP

A Sentence can be expanded as a Noun phrase then a Verb Phrase
```

## Parsing

Expand all tags recursively, but constrain words to match input word (at each respective position)

## Learning

Generate grammar by hand parsing many sentences and recording all grammar expansion rules. (U of Pennsylvania `wsj.txt`)

## Scoring a Tree using relative frequencies

Not all syntactic structures are equally common. One approach: Pick the most common structure.
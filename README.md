# store

Portuguese named entity recognition data in CoNLL format, plus a small reader. Used in 2019 for
sequence labeling experiments.

## Files

| File | Sentences | Columns |
|---|---|---|
| `train.conll` | 71,057 | token, part of speech, entity tag |
| `test.conll` | 42,633 | token, part of speech, entity tag |
| `valid.conll` | 28,422 | token, part of speech (no entity tag) |
| `util.py` | | Functions to read the files into lists of sentences, words and labels |

Entity tags follow the BIO scheme with four types: `PER`, `LOC`, `ORG` and `MISC`.

```
A NOM O
Bíblia NOM B-MISC
contém V O
```

## Reading

```python
from util import get_senteces, split_tokens_labeled

sentences = split_tokens_labeled(get_senteces("train.conll"))
```

The original source of the corpus was not recorded in this repository.

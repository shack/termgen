# Random Term Generator

Generate random terms and dump them as an [S-Expression](https://en.wikipedia.org/wiki/S-expression).
Example:
```
python termgen.py -n 100 -i 4 -o 'add:2,sub:2,neg:1'
```
This says that we want 100 inner nodes in the term, we have 4 input variables, and we want to use binary operators add and sub and unary operator neg.

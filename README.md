# HashtagGenerator
A simple multilanguage python script to extract Hashtags from long text using LDA model from GenSim



usage: HashtagGenerator.py [-h] --document DOCUMENT [--language LANGUAGE]
                           [--hashtags HASHTAGS] [--passes PASSES]

Python script to extract hashtags from long text based on LDA model from
GenSim

optional arguments:
  -h, --help           show this help message and exit
  --document DOCUMENT  Path to the document
  --language LANGUAGE  Language of the text
  --hashtags HASHTAGS  Number of hashtags to extract
  --passes PASSES      Iteration for the LDA model to perform

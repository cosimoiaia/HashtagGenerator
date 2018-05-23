# HashtagGenerator
A simple multilanguage python script to extract Hashtags from URL or long text using LDA model from GenSim


```
usage: HashtagGenerator.py [-h] --document DOCUMENT [--language LANGUAGE]
                           [--hashtags HASHTAGS] [--passes PASSES]

Python script to extract hashtags from URL or long text based on LDA model
from GenSim

optional arguments:
  -h, --help           show this help message and exit
  --document DOCUMENT  Path or URL to the document
  --language LANGUAGE  Language of the text
  --hashtags HASHTAGS  Number of hashtags to extract
  --passes PASSES      Iteration for the LDA model to perform
```


<b>Example</b>

Url:
```
$ ./HashtagGenerator.py --document "https://medium.com/@alet89/understanding-the-gold-rush-of-scalable-and-validated-data-powered-by-blockchain-and-decentralized-ee05db6b6a68"
[Url found]
HashTags: 
#blockchain #technology #algorithm #ai #data #network 

```

Document:
```
./HashtagGenerator.py --document document.txt 
HashTags: 
#virtual #world #game #reality #headset #company #sensor #vr #facebook #oculus #device 
```

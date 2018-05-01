# Here we are going to use the Stanford NER Tagger in order to extract cities from Text

# To make this code work it is important to download stanford-corenlp-full-2018-02-27
# check the dependencies (CLASSPATH and STANFORD_MODELS) and execute this command on cmd:
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

from nltk.tag.stanford import CoreNLPNERTagger

st = CoreNLPNERTagger(url='http://localhost:9000').tag('Rami Eid is studying in NY'.split())

print(st)

document=[]
from hazm import *
f = open('all_stopwords.txt', encoding='utf8')
normalizer=Normalizer()
#stemmer = Stemmer()
#normalizer = Normalizer()
positive_1=[]
negative_1=[]
neutral_1=[]
docs=[]
messages=[]
for file in iter(f):
    messages.append(file)
#messages = result.messages
print("till")
persian=False
news=""
a_set = ['ض','ك','ي','ص','ث','ق','ف','غ','ع','ه','خ','ح','ج','چ','ش','س','ی','ب','ل','ا','ت','ن','م','ک','گ','پ','ظ','ط','ز','ر','ذ','د','ئ','و','ة','ي','ژ','ؤ','إ','أ','ء','َ','ُ','ِ','ّ','ۀ','ي','آ','ً','ٌ','ٍ']
for file in messages:
   news=""
   fo=str(file)
   words=fo.split()
   ln=len(words)
   for word in words:
       persian = False
       for letter in word:
           if letter in a_set:
               persian=True
       if persian==True:
           news=news+word+" "
   if len(news)>1:
    #document.append(news)
    ln = len(news)
    for letter in news:
        if letter not in a_set:
           ln=ln-1
           news=news.replace(letter," ")
    if ln>1:
     document.append(news)

print(len(document))
stops=[]
document=[]
for d in messages:
    d=d.replace("\n","")
    d=normalizer.normalize(d)
    document.append(d)


for d in document:
    #if d.find("به")!=-1:
        #print(d)
    stops.append(d)
#fo = open("all_stopwords_preprocessed.txt", "a+",encoding='utf8')
f1 = open("dos_150_preprocessed.txt" ,encoding='utf8')
doc_complete=[]
doc_complete_without_stops=[]
for file in iter(f1):
    doc_complete.append(file)
for doc in   doc_complete:
    s=""
    doc=normalizer.normalize(doc)
    words=word_tokenize(doc)
    for w in words:
        if w not in stops:
            s=s+w+" "
        else:
            print(w)
    if len(s)>0:
        doc_complete_without_stops.append(s)

# compile documents

doc_clean = [doc.split() for doc in doc_complete_without_stops]
import gensim
from gensim import corpora
# Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
print(ldamodel.print_topics(num_topics=5, num_words=5))

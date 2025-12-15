                  #NLP
# Natural Language Processing (NLP) is a field of AI that enables computers to understand, interpret, and generate human language.
# 📌 Used in:
         # Chatbots
         # Search engines
         # Translation systems
         # Sentiment analysis
         # Large Language Models (LLMs)

        #NLP PIPELINE
# Text → Cleaning → Tokenization → Normalization → Feature Extraction → Model

         # Text Preprocessing
#     • Text Cleaning
#     • Tokenization
#     • Stop Words Removal
#     • Stemming
#     • Lemmatization

        # 4️⃣ Text Representation / Feature Extraction
#     • Bag of Words (BoW)
#     • TF-IDF
#     • Word Embeddings-WORD2VEC

         # 5️⃣ NLP Model
#     • ML / DL / Transformer

          # 6️⃣ NLP Tasks / Output
#     • Classification
#     • Sentiment Analysis
#     • NER
#     • Translation
#     • Question Answering


#TOKENIZATION:PROCESS OF CONVERTING SENTENCE OR PARAGRAPH INTO TOKENS
   #CORPUS-PARAGRAPH
   #DOCUMENTS-SETENCES
   #VOCABULARY-UNIQUE WORDS
  #EX:Python is an interesting language.It is used in various fieeld like machine learning,deep learning,nlp.
  #So,Tokenization is breaking corpus into word or sentences.
   #Tokens={sentences}:Python is an interesting language
   #WORDS CAN ASLO BE TOKEN:PYTHON ,IS,INTERSETING,LANGUAGE
    
#EX:I LIKE MANGO SAHKE.MY FRIENS LIKE BANANA SHAKE. SO HERE,THERE ARE TOTAL 8 UNIQUE WORD.SO THAT IS MY VOCABULARY

                        #PRACTICAL IMPLEMENTATION OF TOKENIZATION

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import sent_tokenize,word_tokenize

corpus = "NLP is part of AI. It helps machines understand language.You will be enjoying it."

sentences = sent_tokenize(corpus)     #CONVERTING PARA INTO SENTENCES
words = word_tokenize(corpus)       #SENTENCE INTO WORDS

print("Sentences:", sentences)
print("Words:", words)


                    #TEXT PREPROCESSING:STEMMING AND LEMMATIZATION
# What is stemming?
    # Stemming is the process of reducing words to their root form by removing suffixes.

# ❓ What is lemmatization?
    # Lemmatization converts words to their meaningful base form using vocabulary and grammar.

# ❓ Which is better?
    # Lemmatization is better for accuracy, stemming is better for speed.


                    #STEMMING
# from nltk.stem import PorterStemmer
# stemmer=PorterStemmer()     
# for word in words:
#     print(stemmer.stem(word))

# print(stemmer.stem('congratulations'))  #OUTPUT:CONGRATUL
# print(stemmer.stem("sitting"))  #OUTPUT:SIT


            #LEMMATIZATION
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
for word in words:
    print("Lemmatization is :",lemmatizer.lemmatize(word,pos='v'))


         #STOPWWORD REMOVAL:Stopwords are common words that usually don’t add much meaning:
# is, am, are, the, a, an, in, on, and, of…
# They are removed to:# Reduce noise ,# Improve model performance
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original words:", words)
print("After stopwords removal:", filtered_words)


         #POS TAGS
nltk.download('averaged_perceptron_tagger_eng')
pos_tags = nltk.pos_tag(words)
print(pos_tags)
  
       #NAMED ENTITY RECOGNITION:NER identifies and classifies real-world entities in text such as:
# PERSON (people),# ORGANIZATION (companies),# LOCATION (places),# DATE,# MONEY

nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
ner_tree = nltk.ne_chunk(pos_tags)

print(ner_tree)


          #ENCODING:CONVERTING WORDS INTO VECTOR
    #BAG OF WORDS:Bag of Words is a text representation technique that converts text into numerical vectors based on word frequency.


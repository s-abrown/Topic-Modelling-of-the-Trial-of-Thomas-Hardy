import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
#stop words
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.collocations import BigramAssocMeasures


##############################################################################################################################

# Define a corpus of document(s)
with open("cleaned_with_Regex.txt", "r") as file:
    documents = file.read()

# Tokenize the documents
words = nltk.word_tokenize(documents)
#words = [word for word in words] #Todo: is this line necessary?

# Write a section of code to delete common stop words

# Define a list of stop words
stop_words = set(stopwords.words('english'))

# Remove stop words from the 'words' list
#filtered_words = [word for word in words if word not in stop_words]
# Idem but with no non-alphabetic tokens
filtered_words = [word for word in words if word not in stop_words and word.isalpha()]

# Now 'filtered_words' contains your words with stop words removed

bigram_finder = BigramCollocationFinder.from_words(filtered_words)
bigrams = bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, 50)

print(bigrams,"\n\n")


##################### Searching for context/words most commonly associated with a particular term --> Using .similar() function ###########################

text = Text(filtered_words)

# Say I'm looking for the words immediately next to "Erskine"
word = 'Erskine'

# Find the words most commonly associated with your word
text.similar(word) #finds other words that appear in the same context as the specified word—in this case, 'Erskine'. The context of a word is defined by the words that are immediately to its left and right. The similar() function looks at all the contexts of 'Erskine' in your text, and then finds other words that appear in the same contexts.


##################### Collocation function ###########################

# Find collocations in your text
text.collocations()

# /!\ Remember: collocation= sequence of words that occur together "unusually often" – a.k.a. the collocations() function finds these sequences by looking for pairs of words that occur together more often than would be expected by chance.

#The collocations() function in NLTK uses a measure called Pointwise Mutual Information (PMI) to find collocations. PMI measures the degree of association between two words. However, by default, the collocations() function only considers word pairs that appear at least twice in the text. This can sometimes lead to surprising results, especially in texts with a lot of unique word pairs.

#If I want to find less frequent collocations, I can use the ngram_fd attribute of the Text object, which is a frequency distribution of all ngrams in the text. You can then use the pmi function from the nltk.metrics module to calculate the PMI of each bigram, and sort them by PMI to find the most strongly associated pairs.

##################### Collocation function for less frequent collocations ###########################

# Get a frequency distribution of bigrams
bigram_fd = nltk.FreqDist(nltk.bigrams(filtered_words))

# Calculate the PMI of each bigram
bigram_measures = BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(filtered_words)
bigrams_pmi = finder.score_ngrams(bigram_measures.pmi)

# Print the top 50 bigrams by PMI
print("\nTop 50 bigrams by PMI:")
for ngram, score in bigrams_pmi[:50]:
    print(ngram, score)

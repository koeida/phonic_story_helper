import tree
import nltk

def generate_all_phonetic_sequences():
    ts = tree.gen_tree(None,"")

    for t in ts:
        tree.walk_tree(t, "")

    results = set(tree.results)
    return results

# Filter phonetic sequences down to dictionary of (english word -> parts of speech)
def get_pos_tags(phonetic_sequences):
    tagged_sequences = {}
    brown_news_tagged = nltk.corpus.brown.tagged_words(tagset='universal')
    brown_news_tagged = filter(lambda n: n[0] in phonetic_sequences and len(n[0]) > 2, brown_news_tagged)
    data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
    for word in sorted(data.conditions()):
        tags = [tag for (tag, _) in data[word].most_common()]
        tagged_sequences[word] = tags
    return tagged_sequences

# Convert dictionary of (word -> parts of speech) to (part of speech -> words)
def partition_by_pos(tagged_sequences):
    res = {"NOUN":[], "ADJ":[], "VERB":[]}
    for w, pos in tagged_sequences.items():
        for t in res.keys():
            if t in pos:
                res[t].append(w)
    return res

phonetic_sequences = generate_all_phonetic_sequences()
tagged_sequences = get_pos_tags(phonetic_sequences)
results = partition_by_pos(tagged_sequences)

for t, words in results.items():
    print(t)
    print("=" * len(t))
    for w in words: 
        print(w)
    print("")

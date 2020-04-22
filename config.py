consonants = list("bcdfghjklmnpqrstvwz")
vowels = list("aeiou")

# Consonant blends
rblends = "br cr dr gr kr pr tr".split(" ")
lblends = "bl cl fl gl kl pl sl vl".split(" ")
tblends = ["st"]
hblends = "sh ch th".split(" ")
consonant_blends = rblends + lblends + tblends + hblends

# Other blends
rs = "er ar or".split(" ")
ngs = "ing ang ong".split(" ")
other_blends = rs + ngs

# Set up possible starts, middles, and ends of words
starts = consonants + consonant_blends + other_blends
middles = rs + vowels + [""]
ends = consonants + ["er", "ing", "sh"]

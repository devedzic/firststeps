from collections import Counter

text =  'Sign commemorating the role of Alan Freed and Cleveland, Ohio in the origins of rock and roll' \
        'The term "rock and roll" now has at least two different meanings, both in common usage. ' \
        'The American Heritage Dictionary and the Merriam-Webster Dictionary both define rock and roll as ' \
        'synonymous with rock music. Encyclopædia Britannica, on the other hand, regards it as the music that ' \
        'originated in the mid-1950s and later developed "into the more encompassing international style known as ' \
        'rock music".'

words = text.split()
counter = Counter(words)

top3 = counter.most_common(3)
print(top3)
print()



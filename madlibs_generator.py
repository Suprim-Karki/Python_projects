''' Madlibs generator '''

with open ("story.txt","r") as f:
    story=f.read()

start_word=-1
target_start="<"
target_end=">"
words=set()

for i,char in enumerate(story):
    if char==target_start:
        start_word=i
    if char==target_end and start_word!=-1:
        word=story[start_word: i+1]
        words.add(word)
        start_word+=-1

answers={}
for word in words:
    answer=input(f"Enter a word for {word}: ")
    answers[word]=answer

for word in words:
    story = story.replace(word,answers[word])
print(f"\n{story}")

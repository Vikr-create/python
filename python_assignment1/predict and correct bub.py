score=50
def update():
    global score
    print(score)
    score=score+10
update()
print(score)

# quetion 1 answer: python treats score as a local variable
#quetion 2 answer: it allow a function to modify global variable
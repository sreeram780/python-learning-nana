def print_name(prefix):
    print(f"Searching prefix: {prefix}")
    while True:
        name = (yield)
        if prefix in name:
            print(name)
# Instantiate the coroutine
corou = print_name("Welcome to")
# Start the coroutine
corou.__next__()
# Send values to the coroutine
corou.send("Tutorialspoint")
corou.send("Welcome to Tutorialspoint")

# clsing coroutine
def print_name(prefix):
    print(f"Searching prefix: {prefix}")
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")
# Instantiate and start the coroutine
corou = print_name("Come")
corou.__next__()
# Send values to the coroutine
corou.send("Come back Thank You")
corou.send("Thank you")
# Close the coroutine
corou.close()

# Chaining Coroutines for Pipelines
def producer(sentence, next_coroutine):
   '''
   Splits the input sentence into tokens and sends them to the next coroutine.
   '''
   tokens = sentence.split(" ")
   for token in tokens:
      next_coroutine.send(token)
   next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):
   '''
   Filters tokens based on the specified pattern and sends matching tokens to the next coroutine.
   '''
   print(f"Searching for {pattern}")
   try:
      while True:
         token = (yield)
         if pattern in token:
            next_coroutine.send(token)
   except GeneratorExit:
      print("Done with filtering!!")
      next_coroutine.close()

def print_token():
   '''
   Receives tokens and prints them.
   '''
   print("I'm the sink, I'll print tokens")
   try:
      while True:
         token = (yield)
         print(token)
   except GeneratorExit:
      print("Done with printing!")
# Setting up the pipeline
pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()
sentence = "Tutorialspoint is welcoming you to learn and succeed in Career!!!"
producer(sentence, pf)
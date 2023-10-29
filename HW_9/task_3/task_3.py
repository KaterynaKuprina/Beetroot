import os
from mymod import *

my_directory = "C:/Users/Катерина/Desktop/Beetroot/HW_9/task_3"
text_file = os.path.join(my_directory, "text.txt")

with open(text_file, "w") as my_file:
    my_file.write("Rod Steiger was an American actor, noted for his portrayal of offbeat,\n"
                  "often volatile and crazed characters. He is closely associated with the art of method\n"
                  "acting, embodying the characters he played, which at times led to clashes with directors\n"
                  "and co-stars. He starred with Marlon Brando in On the Waterfront, playing Charley\n"
                  "the mobster brother of Brando's character.")


test("text.txt")

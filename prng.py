import time
import random

while True:
    time.sleep(1)
    with open("prng-service.txt", "r+") as file:
        content = file.read()
        if content.strip() == "run":
            random_number = random.randint(0, 100)  
            file.seek(0)
            file.write(str(random_number))
            file.truncate()

import time

while True:
    user_input = input("Enter 1 to generate a new image or 2 to exit: ")
    if user_input == "1":
        with open("prng-service.txt", "w") as file:
            file.write("run")

        time.sleep(5)

        with open("prng-service.txt", "r") as file:
            random_number = file.read()

        with open("image-service.txt", "w") as file:
            file.write(random_number)

        time.sleep(5)

        with open("image-service.txt", "r") as file:
            image_path = file.read()
            print(f"Image path: {image_path}")

    elif user_input == "2":
        break
    else:
        print("Unknown option")

import time

num_images = 3  # Change this based on the actual number of images

while True:
    time.sleep(1)
    with open("image-service.txt", "r+") as file:
        content = file.read()
        if content.isdigit():
            image_number = int(content) % num_images
            path = f"Users\ianja\OneDrive\Desktop\CS361\Assignment1/{image_number}.jpg"
            file.seek(0)
            file.write(path)
            file.truncate()

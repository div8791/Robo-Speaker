import os

if __name__ == '__main__':
    print("Welcome to the RoboSpeaker")
    while True:
        x = input("Enter what you want to say: ")
        if x == "q":
            os.system("say 'Good Bye!'")
            break

        command = f'say {x}'
        os.system(command)
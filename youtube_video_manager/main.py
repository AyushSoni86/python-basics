import json

FILE_NAME = "youtube.txt"

def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError as e:
        return []

def save_file_data(videos):
    with open(FILE_NAME, 'w') as file:
        json.dump(videos, file)
        
def listAllVideo(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['Name']}, Duration = {video['Duration']}")
    print("\n")
    print("*" * 70)

def addVideo(videos):
    video_name = input("Enter name of video: ")
    video_duration = input("Enter duration: ")
    videos.append({'Name' : video_name, 'Duration' : video_duration})
    save_file_data(videos)

def updateVideo(videos):
    listAllVideo(videos)
    index = int(input("Enter the video number to update: "))
    if(1 <= index <= len(videos)):
        video_name = input("Enter new name of video: ")
        video_duration = input("Enter new video time: ")
        videos[index-1] = {'Name' : video_name, 'Duration' : video_duration}
        save_file_data(videos)
    else:
        print("Invalid video number")
    
def deleteVideo(videos):
    listAllVideo(videos)
    index = int(input("Enter the video number to be deleted: "))
    if(1 <= index <= len(videos)):
        del videos[index - 1]
        save_file_data(videos)
    else:
        print("Invalid video number")
        
def main():
    videos  = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")   
        print("1. List youtube video")
        print("2. Add youtube video")
        print("3. Update youtube video details")
        print("4. delete youtube video")
        print("5. exit")
        
        user_input = input("Enter your choice: ")
        
        match user_input:
            case "1": 
                listAllVideo(videos)
            case "2": 
                addVideo(videos)
            case "3": 
                updateVideo(videos)
            case "4": 
                deleteVideo(videos)
            case "5": 
                break
            case _:
                print("Invalid Choice")

        
if __name__ == "__main__":
    main()
    
    
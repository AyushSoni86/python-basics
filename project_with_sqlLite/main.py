import sqlite3

con = sqlite3.connect("youtube.db")
cursor = con.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS video(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL,
                )
''')


        
def listAllVideo():
    print("\n")
    print("*" * 70)
    cursor.execute("SELECT * FROM video")
    for row in cursor.fetchall():
        print(f"{row.id}. {row.name} = {row.time}")
    print("\n")
    print("*" * 70)

def addVideo(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (? , ?)", (name, time))
    con.commit()
    
def updateVideo(index, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, index))
    con.commit()
    
def deleteVideo(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id, ))
    con.commit()
        
def main():
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
                listAllVideo()
            case "2": 
                name = input("Enter name of video: ")
                time = input("Enter duration: ")
                addVideo(name, time)
            case "3": 
                index = int(input("Enter the video number to update: "))
                name = input("Enter new name of video: ")
                time = input("Enter new time: ")
                updateVideo(index, name, time)
            case "4": 
                index = int(input("Enter the video number to be deleted: "))
                deleteVideo(index)
            case "5": 
                break
            case _:
                print("Invalid Choice")

    con.close()

if __name__ == "__main__":
    main()
    
    
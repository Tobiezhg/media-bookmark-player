import os, webbrowser

full_path = os.path.realpath(__file__)
current = os.path.dirname(full_path)
text = "text_base_of_playlist.txt"


# Define a playlist class, a playlist has name, description, rating, and videos
class Playlist:
    def __init__(self, name, description, rating, link, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.link = link
        self.videos = videos


# Define a video class, a video has title and link
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False

    def open(self):
        webbrowser.open(self.link)
        self.seen = True


#============================


# Read 2 line from a text file and return video
def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video


# Read the text file to get a videos list
def read_videos_from_txt(file):
    videos = []
    total = int(file.readline())
    for i in range(total):
        video = read_video_from_txt(file)
        videos.append(video)
    return videos


def read_playlist_from_txt(file):
    playlist_name = file.readline()
    playlist_description = file.readline()
    playlist_rating = file.readline()
    playlist_link = file.readline()
    playlist_videos = read_videos_from_txt(file)
    playlist = Playlist(playlist_name, playlist_description, playlist_rating,
                        playlist_link, playlist_videos)
    return playlist


# Ask the user to enter information of a video
def read_video():
    title = input("Enter title: ") + "\n"
    link = input("Enter link: ") + "\n"
    video = Video(title, link)
    return video


# Ask an user to enter information of all videos one by one, they first choose how many videos are there
def read_videos():
    videos = []
    total_video = int(input("Enter how many video: "))
    for i in range(total_video):
        print("||| Video ", i + 1, "|||")
        vid = read_video()
        videos.append(vid)
    return videos


# Option 1: Ask an user to enter information of the playlist
def read_playlist():
    playlist_name = input("Enter playlist's name: ") + "\n"
    playlist_description = input("Enter playlist's description: ") + "\n"
    playlist_rating = input("Enter playlist's rating (1-5): ") + "\n"
    playlist_link = input("Enter playlist's link: ") + "\n"
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating,
                        playlist_link, playlist_videos)
    return playlist


#============================


# Show information of a video
def print_video(video):
    print("Video title: ", video.title, end="")
    print("Video link: ", video.link)


# Show information of all videos
def print_videos(videos):
    print("-----")
    for i in range(len(videos)):
        print("Video ", i + 1, " info")
        print_video(videos[i])
    print("-----")


# Option 2: Use the list above and show all information of videos inside that list
def print_playlist(playlist):
    print("=== === ===")
    print("Playlist " + playlist.name, end="")
    print("Description: " + playlist.description, end="")
    print("Rating (1-5): " + playlist.rating, end="")
    print("Link: " + playlist.link, end="")
    print_videos(playlist.videos)
    print("=== === ===")


#============================


# Option 3: Play a video that an user chose on new tab
def play_video(playlist):
    print_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range(f"Select a video (1-{str(total)}): ", 1, total)
    print("Open videos: ",
          playlist.videos[choice - 1].title,
          " - ",
          playlist.videos[choice - 1].link,
          end="")
    playlist.videos[choice - 1].open()


#============================


# Option 4: Allow an user to add a new video to the playlist, they have to enter the name and the link
def add_video(playlist):
    print("=> Enter new video information <=")
    new_video = read_video()
    playlist.videos.append(new_video)
    print("Successfully Add A New Video to the Playlist !")
    return playlist


#============================


# Option 5: Updating name / description / rating / link of the playlist
def update_playlist(playlist):
    print("=> Update playlist <=")
    print("1. Name")
    print("2. Description")
    print("3. Rating")
    print("4. Link")

    choice = select_in_range("Enter what you want to update (1-4): ", 1, 4)
    if choice == 1:
        new_playlist_name = input("Enter new name for playlist: ") + "\n"
        playlist.name = new_playlist_name
        return playlist
    if choice == 2:
        new_playlist_description = input(
            "Enter new description for the playlist: ") + "\n"
        playlist.description = new_playlist_description
        return playlist
    if choice == 3:
        new_playlist_rating = str(
            select_in_range("Enter new rating (1 - 5) for the playlist: ", 1,
                            5)) + "\n"
        playlist.rating = new_playlist_rating
        return playlist
    if choice == 4:
        new_playlist_link = input("Enter new link for the playlist: ") + "\n"
        playlist.link = new_playlist_link
        return playlist


#============================


# Option 6: The user is allowed to delete a video in the playlist after exposing to the whole playlist's information
def remove_video(playlist):
    print_videos(playlist.videos)
    choice = select_in_range("Enter video you want to delete: ", 1,
                             len(playlist.videos))
    del playlist.videos[choice - 1]
    print("Delete Successfully !")
    return playlist


#============================


# Write a video information to a text file
def write_video_to_txt(video, file):
    file.write(video.title)
    file.write(video.link)


# Write videos information to text file, first line is the total number of videos
def write_videos_to_txt(videos, file):
    total = len(videos)
    file.write(str(total) + "\n")
    for i in range(total):
        write_video_to_txt(videos[i], file)


# Option 7: Write playlist information to text file
def write_playlist_to_txt(playlist, file):
    file.write(playlist.name)
    file.write(playlist.description)
    file.write(playlist.rating)
    file.write(playlist.link)
    write_videos_to_txt(playlist.videos, file)
    print("Successfully write playlist to text!")


#============================


# Make sure that an user enter number in limitted range
def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice


def show_menu():
    print("=============================")
    print("|          Main Menu        |")
    print("| Option 1: Create Playlist |")
    print("| Option 2:   Show Playlist |")
    print("| Option 3:    Play a Video |")
    print("| Option 4:     Add a Video |")
    print("| Option 5:     Update Info |")
    print("| Option 6:  Delete a Video |")
    print("| Option 7:   Save and Exit |")
    print("=============================")


#============================


def main():
    os.system("cls")
    try:
        with open(os.path.join(current, text), "r") as file:
            playlist = read_playlist_from_txt(file)
        print("Successfully loaded data !")
    except:
        print("Welcome first user !")
    while True:
        show_menu()
        choice = select_in_range("Select an option (1-7): ", 1, 7)
        if choice == 1:
            playlist = read_playlist()
            input("\nPress ENTER to continue.")

        elif choice == 2:
            print_playlist(playlist)
            input("\nPress ENTER to continue.")

        elif choice == 3:
            play_video(playlist)
            input("\nPress ENTER to continue.")

        elif choice == 4:
            playlist = add_video(playlist)
            input("\nPress ENTER to continue.")

        elif choice == 5:
            playlist = update_playlist(playlist)
            input("\nPress ENTER to continue.")

        elif choice == 6:
            playlist = remove_video(playlist)
            input("\nPress ENTER to continue.")

        elif choice == 7:
            with open(os.path.join(current, text), "w") as file:
                write_playlist_to_txt(playlist, file)
            break
        else:
            print("ERROR: Wrong input. Exist.")
            break
        os.system("cls")


main()
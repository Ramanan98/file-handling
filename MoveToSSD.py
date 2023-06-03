import os
import shutil

def isSubtitle(fileName):
    return fileName.endswith(".srt")

def isNotHidden(folderName):
    return not folderName.startswith(".")

path = "/Users/ramanan/Movies/TV Shows/Parks and Recreation"
move_to_path = "/Volumes/SSD/TV Shows"

title = "Parks and Recreation"

seasonFolders = filter(isNotHidden, sorted(os.listdir(path)))
for seasonFolder in seasonFolders:
    subtitles = list(filter(isSubtitle, sorted(os.listdir(os.path.join(path, seasonFolder)))))
    for subtitle in subtitles:
        subtitle_path = os.path.join(path, seasonFolder, subtitle)
        shutil.copy(subtitle_path, os.path.join(
                        move_to_path, title, seasonFolder, subtitle))
        print("Copied "+subtitle)

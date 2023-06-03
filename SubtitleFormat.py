import os
import re
import shutil

def formatNum(x):
    if x < 10:
        text = "0"+str(x)
        return text
    return str(x)


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

path = "/Users/ramanan/Downloads/Media"
move_to_path = "/Users/ramanan/Movies/TV Shows"

title = "Parks and Recreation"
season = 0
episode = 0
for season_folder in sorted(listdir_nohidden(path)):
    if (os.path.isdir(os.path.join(path, season_folder, "Subs"))):
        for episode_folder in sorted(listdir_nohidden(os.path.join(path, season_folder, "Subs"))):
            if os.path.isdir(os.path.join(path, os.path.join(path, season_folder, "Subs", episode_folder))):
                #Get the last file alphabetically, it's the SDH one
                subtitle_file = sorted(os.listdir(os.path.join(path, season_folder, "Subs", episode_folder)))[-1]
                subtitle_file_path = os.path.join(
                    path, season_folder, "Subs", episode_folder, subtitle_file)
                if os.path.isfile(subtitle_file_path):
                    #Find single episode subtitles and rename them to match Plex naming convention
                    season = re.search(r"S(\d+)E", episode_folder).group(1)
                    file_name = title+" – s" + \
                        season+"e"
                    #Find multiepisode subtitles and rename them to match Plex naming convention
                    matches = re.findall(r'E(\d+)(?:E(\d+))?', episode_folder)
                    for match in matches:
                        file_name = file_name + str(match[0])
                        if(match[1]):
                            file_name = file_name + "-"+str(match[1])
                    shutil.move(subtitle_file_path, os.path.join(
                        move_to_path, title, "Season "+season, file_name+".srt"))
                    print("Moved "+file_name)
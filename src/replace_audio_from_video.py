import os
import subprocess


def convert(input_video, input_audio, output):
    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            input_audio,
            "-vn",
            "-acodec",
            "copy",
            "temp.aac",
        ]
    )
    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-i",
            input_video,
            "-i",
            "temp.aac",
            "-vcodec",
            "copy",
            "-acodec",
            "copy",
            "-map",
            "0:0",
            "-map",
            "1:0",
            output,
        ]
    )


def parse_filename(name):
    if name.startswith("EP"):
        return int(name.split(".")[1])
    elif name.startswith("("):
        return int(name.split(".")[-2].split("-")[-1])

    print("WARNING > Couldn't parse filename for episode number > " + name)
    return -1


def main():
    print("INFO > Looking for files...")

    video_source = []
    audio_source = []

    try:
        video_source = os.listdir("video")
    except Exception:
        print('ERROR > Could not find directory "video"')
        print("INFO > Exiting")
        return

    try:
        audio_source = os.listdir("audio")
    except Exception:
        print('ERROR > Could not find directory "audio"')
        print("INFO > Exiting")
        return

    video_filenames = sorted(video_source, key=parse_filename)
    audio_filenames = sorted(audio_source, key=parse_filename)

    print(f'INFO > Found {len(video_filenames)} files in directory "video"!')
    print(f'INFO > Found {len(audio_filenames)} files in directory "audio"!')

    if len(video_filenames) != len(audio_filenames):
        print("ERROR > Different number of video and audio source files")
        print("INFO > Exiting")
        return

    if len(video_filenames) == 0:
        print("ERROR > No video and audio source files found")
        print("INFO > Exiting")
        return

    print("")
    print("INFO > Actions:")

    video_locations = []
    audio_locations = []

    for i in range(0, len(video_filenames)):
        video_locations.append("video\\" + video_filenames[i])
        audio_locations.append("audio\\" + audio_filenames[i])

        print(f"    {video_locations[i]} + {audio_locations[i]}")

    print("")
    try:
        season = int(input("INPUT < Enter season number: "))
    except ValueError:
        print("ERROR > Expected integer")
        print("INFO > Exiting")
        return

    if season < 1 or season > 99:
        print("ERROR > Bad season number")
        print("INFO > Exiting")
        return

    season_prefix = f"S{season:02d}"

    confirmation = input("INPUT < Start? ")

    if confirmation != "y":
        print("INFO > Cancelling operation")
        return

    for i in range(0, len(video_filenames)):
        output_filename = f"{season_prefix}E{(i + 1):02d}.mp4"

        convert(video_locations[i], audio_locations[i], output_filename)

    os.remove("temp.aac")

    print("")
    print("INFO > Done!")


if __name__ == "__main__":
    main()

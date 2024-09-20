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


def main():
    print("INFO > Looking for files...")

    video_source = []
    audio_source = []

    try:
        video_source = os.listdir("video")
    except Exception:
        print('ERROR > Could not find directory "video"')
        print("INFO > EXITING")
        return

    try:
        audio_source = os.listdir("audio")
    except Exception:
        print('ERROR > Could not find directory "audio"')
        print("INFO > EXITING")
        return

    video_filenames = sorted(video_source, key=lambda x: int(x.split(".")[1]))
    audio_filenames = sorted(audio_source, key=lambda x: int(x.split(".")[1]))

    print(f'INFO > Found {len(video_filenames)} files in directory "video"!')
    print(f'INFO > Found {len(audio_filenames)} files in directory "audio"!')

    if len(video_filenames) != len(audio_filenames):
        print("ERROR > Different number of video and audio source files")
        print("INFO > EXITING")
        return

    if len(video_filenames) == 0:
        print("ERROR > No video and audio source files found")
        print("INFO > EXITING")
        return

    print("")
    print("INFO > Actions:")

    video_locations = []
    audio_locations = []

    for i in range(0, len(video_filenames)):
        video_locations.append("video\\" + video_filenames[i])
        audio_locations.append("audio\\" + audio_filenames[i])

        print(f"       video: {video_locations} + audio: {audio_locations}")

    print("")
    season = int(input("INPUT < Enter season number: "))

    if season < 1 or season > 99:
        print("ERROR > Bad season number")
        print("INFO > EXITING")
        return

    season_prefix = f"S{season:02d}"

    confirmation = input("INPUT < Start? ")

    if confirmation != "y":
        print("INFO > Cancelling operation")
        return

    for i in range(0, len(video_filenames)):
        output_filename = f"{season_prefix}E{(i + 1):02d}.mp4"

        convert(video_locations[i], audio_locations[i], output_filename)

    print("INFO > Done!")


if __name__ == "__main__":
    main()

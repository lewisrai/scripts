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
    videos = os.listdir("video")
    audios = os.listdir("audio")

    videos = sorted(videos, key=lambda x: int(x.split(".")[1]))
    audios = sorted(audios, key=lambda x: int(x.split(".")[1]))

    if len(videos) != len(audios):
        print("Different number of videos")
        return

    for i in range(0, len(videos)):
        videos[i] = "video\\" + videos[i]
        audios[i] = "audio\\" + audios[i]

        print(videos[i] + "  +  " + audios[i])

    prefix = int(input("Enter season number: "))
    prefix = f"S{prefix:02d}"

    for i in range(0, len(videos)):
        convert(videos[i], audios[i], f"{prefix}E{(i + 1):02d}.mp4")


if __name__ == "__main__":
    main()

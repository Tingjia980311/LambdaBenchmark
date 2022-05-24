from subprocess import call


def lambda_handler(event, context):
    # clean_directory("./out")
    call (
        ["/var/task/ffmpeg-5.0.1-amd64-static/ffmpeg",
        "-i", "./cut.mp4",
        "-vf", "fps=1/2",
        "out%d.png"]
    )

    return 1

# print(lambda_handler({},{}))

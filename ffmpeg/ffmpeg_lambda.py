from subprocess import call


def lambda_handler(event, context):
    # clean_directory("./out")
    call (
        # ["/var/task/ffmpeg-4.4.1-amd64-static/ffmpeg",
        ["ffmpeg",    
        "-i", "./cut.mp4",
        "-vf", "fps=1/60",
        "out%d.png"]
    )

    return 1

print(lambda_handler({},{}))

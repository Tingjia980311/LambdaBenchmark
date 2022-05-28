from subprocess import call


def lambda_handler(event, context):
    if event['act'] == 'sample':
        # clean_directory("./out")
        call (
            ["/var/task/ffmpeg-5.0.1-amd64-static/ffmpeg",
            "-i", "./cut.mp4",
            "-vf", "fps=1/2",
            "/tmp/out%d.png"]
        )

        # call (
        #     ["./data/ffmpeg-5.0.1-amd64-static/ffmpeg",
        #     "-i", "./data/cut.mp4",
        #     "-vf", "fps=1/2",
        #     "./data/out%d.png"]
        # )

        return 1
    if event['act'] == 'cut':

import time
start = time.time()
print(lambda_handler({},{}))
end = time.time()
print(end - start)

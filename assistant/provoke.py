#import os
#os.system("googlesamples-assistant-pushtotalk --once")

import subprocess

def okgoogle():
        subprocess.run(["bash", "assistant/assist.sh"])

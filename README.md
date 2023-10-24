# falcon-7b-llm-inference-on-gpu
Running Falcon 7B on Nvidia GPU using wsl on windows inference by directly downloading the falcon 7b model when we execute the main python script. We execute the program by running # python main.py

# Setting the environment
conda create -n env python=3.10

# Activate the env
conda activate env

sudo apt-get install git-lfs
git lfs install
git clone https://huggingface.co/tiiuae/falcon-7b-instruct

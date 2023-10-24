# falcon-7b-llm-inference-on-gpu
Running Falcon 7B on Nvidia GPU using wsl on windows inference by directly downloading the falcon 7b model when we execute the main python script. We execute the program by running # python main.py

# Setting the environment
conda create -n env python=3.10

# Activate the env
conda activate env

# Install Git Large file system

sudo apt-get install git-lfs

# Initiate the lfs
git lfs install

# Clone the repository
git clone https://huggingface.co/tiiuae/falcon-7b-instruct

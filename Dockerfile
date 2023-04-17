FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-devel

RUN rm /etc/apt/sources.list.d/cuda.list
# RUN rm /etc/apt/sources.list.d/nvidia-ml.liste

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install basicsr
# facexlib and gfpgan are for face enhancement
RUN pip install facexlib
RUN pip install gfpgan

COPY requirements.txt ./

RUN echo "Installing pip packages..." \
	&& python3 -m pip install -U pip \
	&& pip3 --no-cache-dir install -r ./requirements.txt \
	&& rm ./requirements.txt

WORKDIR /workspace

COPY . /workspace/

RUN python3 setup.py develop



# Llama CPP Apple Silicon Install

Llama CPP is a very well supported open source project designed to accelerate open source LLM utilization via a world class inference system.

It founder is Georgi Gervanov, co-founder of [ggml](https://ggml.ai/).

As most open source projects, it is supported by volunteers and therefore not all its documentation covers some of our burning questions regarding how to make use of that using our Apple Silicon hardware.

## Installation With Metal Support

Metal framework is supported out of the box with Llama CPP according to its website but exact instructions required to enable it is hidden across github issues and such.

There is a pip library called llama-cpp-python which needs to be installed with a flag for it to work correctly, in the following manner (for version 0.2.83) [1]:

    CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python==0.2.83


# How to download a model to use with Llama-CPP?
First step is to recognize that Llama-cpp is built aroung gguf format which is one of the standards for LLM packaging. 

HuggingFace models such as Mystral-7B-Instruct is a great candidate for this. Files can be found here, any of the GGUF extension can work (they are gigabyte files) and we need to download them to a local folder. This [link](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main) can be used to download any of them.

A good best practice here is to set an environment value for file location like "MYSTRAL_7B_INSTRUCT" so as not having to hardcode in our scripts.

# How to infer without a REST API server?

[test.py](test.py) is a small script designed to execute inference without a rest api server. Setting the environmental value as above before running and correctly installing the llama-cpp with METAL support are the prequisites as GPU support is required for this inference script to work.

# How to infer with a REST API server?

Llama CPP comes with its own embedded REST api server and it is very easy to use. Assuming metal support is installed as above

    python3 -m llama_cpp.server --model $MYSTRAL_7B_INSTRUCT --chat_format chatml --n_gpu_layers 35

Then we must go to [localhost:8000](https://localhost:8000/docs). Further details can be found on the reference link [2].



## References:
1. https://pypi.org/project/llama-cpp-python/
2. https://github.com/ggerganov/llama.cpp/tree/master/examples/server

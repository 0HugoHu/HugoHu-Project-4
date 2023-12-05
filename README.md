[![Install](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/lint.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/lint.yml)
[![Lint](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/format.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/rustfmt.yml)
[![Format](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/install.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/binary.yml)

[Youtube Video Here](https://youtu.be/_DSV9nnL_Gc) 
&nbsp;&nbsp;![YouTube Video Views](https://img.shields.io/youtube/views/_DSV9nnL_Gc)


## Individual Project #4: Auto Scaling Flask App Using Any Serverless Platform

### 0. Description
This project builds a flask-based web application that uses the **Facebook BART** model to summarize long text. The model is used by **Hugging Face** free API. 

The application is deployed on **AWS AppRunner**. The application is also containerized using **Docker** and uploaded to AWS ECR.

### 1. How to run
#### 1.1. Build the Docker Container
```bash
docker build -t hugohu-project-4 .
```

![](./hugohu_project_4/static/container.png)

#### 1.2. Upload It to AWS ECR
```bash
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/s2z7p1g5
# Assume you have the ECR repository created
docker tag ids706_ip4:latest public.ecr.aws/s2z7p1g5/ids706_ip4:latest
docker push public.ecr.aws/s2z7p1g5/ids706_ip4:latest
```

![](./hugohu_project_4/static/ecr.png)


#### 1.3. Create AWS AppRunner Service
```bash
# Or you can use the AWS Console to create the service
aws apprunner create-service \
    --service-name ids706-ip4 \
    --source-configuration "RepositoryType=Docker,ImageRepository={ImageIdentifier=public.ecr.aws/s2z7p1g5/ids706_ip4:latest}" \
    --instance-configuration "Cpu=1 vCPU,Memory=2 GB" \
    --region us-east-1
# You need to set up build scripts for Flask App
```

![](./hugohu_project_4/static/appamplify.png)


#### 1.4. Setup Your Hugging Face API Key
```bash
# Or you can import it during AppRunner setup
export API_TOKEN="your_actual_token_value"
```

#### 1.5. Bind Public Domain Name
If want to set up a public domain name, you need to add records to your DNS provider. 

If you want to have a custom CA certificate for secure HTTPS connection, you need to do further in AWS Certificate Manager.

![](./hugohu_project_4/static/host.png)

### 2. How to use
**Visit my domain: [https://ids706.hugohu.site/](https://ids706.hugohu.site/)**

![](./hugohu_project_4/static/web.png)

Enter your any long article in the textarea, or you can choose to select one story from the Aesop's Fables.

Then click the ```Summarize``` button, the application will summarize the text and display the result (this step may take longer than 10 seconds if it's the first time to analyze, because I'm using a free API so it's pretty slow).

![](./hugohu_project_4/static/result.png)

### 3. Hugging Face API
The Hugging Face API is a free API that allows you to use the pre-trained NLP models. It's very easy to use. You can check the [documentation](https://huggingface.co/docs) for more details.

For small LLM models, you can even use the free```Inference API```. The usage is simple:
```python
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
})
```

### 4. Commands
```bash
# Format
make fmt
# Lint
make lint
# Install
make install
# Run
make run
```
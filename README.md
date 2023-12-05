[![Install](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/lint.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/lint.yml)
[![Lint](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/format.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/rustfmt.yml)
[![Format](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/install.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/binary.yml)
[![Test](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/test.yml/badge.svg)](https://github.com/0HugoHu/HugoHu-Project-4/actions/workflows/tests.yml)


[Youtube Video Here](https://youtu.be/Zc14G47JNk4) 
&nbsp;&nbsp;![YouTube Video Views](https://img.shields.io/youtube/views/Zc14G47JNk4)


## Individual Project #4: Auto Scaling Flask App Using Any Serverless Platform

### 0. Description
This project builds a flask-based web application that uses the **Facebook BART** model to summarize long text. The model is used by **Hugging Face** free API. 

The application is deployed on **AWS AppRunner**. The application is also containerized using **Docker** and uploaded to AWS ECR.

### 1. How to run
#### 1.1. Build the Docker Container
```bash
docker build -t hugohu-project-4 .
```

#### 1.2. Upload It to AWS ECR
```bash
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/s2z7p1g5
# Assume you have the ECR repository created
docker tag ids706_ip4:latest public.ecr.aws/s2z7p1g5/ids706_ip4:latest
docker push public.ecr.aws/s2z7p1g5/ids706_ip4:latest
```

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

#### 1.4. Setup Your Hugging Face API Key
```bash
# Or you can import it during AppRunner setup
export API_TOKEN="your_actual_token_value"
```

#### 1.5. 




### 6. Conclusion
From this project, I learned how to use Databricks to analyze data and visualize the results. I also learned how to set up a Databricks ETL Pipeline to automate the process.

The result shows a fun fact that despite different age groups, people spend money on the ```Clothing``` and ```Accessories``` categories. And the holiday season has the highest average purchase amount.

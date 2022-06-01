docker build -t  knn .

aws ecr create-repository --repository-name knn --image-scanning-configuration scanOnPush=true --region us-east-1

docker tag knn:latest 573895773081.dkr.ecr.us-east-1.amazonaws.com/knn:latest

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 573895773081.dkr.ecr.us-east-1.amazonaws.com

docker push 573895773081.dkr.ecr.us-east-1.amazonaws.com/knn:latest

 
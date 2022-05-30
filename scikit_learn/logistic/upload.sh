docker build -t  logisticreg .

aws ecr create-repository --repository-name logisticreg --image-scanning-configuration scanOnPush=true --region us-east-1

docker tag logisticreg:latest 573895773081.dkr.ecr.us-east-1.amazonaws.com/logisticreg:latest

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 573895773081.dkr.ecr.us-east-1.amazonaws.com

docker push 573895773081.dkr.ecr.us-east-1.amazonaws.com/logisticreg:latest

 
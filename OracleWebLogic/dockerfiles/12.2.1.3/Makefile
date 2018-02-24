APPNAME = wls-uber
REGISTRY = 080385600816.dkr.ecr.us-east-1.amazonaws.com
TAG = 0.0.7
LOGIN:=$(shell aws ecr get-login --no-include-email)

all : clean push

container:
	docker build -f Dockerfile.standalone -t $(APPNAME):$(TAG) .

push: container
	exec ${LOGIN}
	docker tag $(APPNAME):$(TAG) ${REGISTRY}/$(APPNAME):$(TAG)
	docker push ${REGISTRY}/$(APPNAME):$(TAG)

clean:
	echo "Nothing here yet"
.PHONY: all container push clean

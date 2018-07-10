APPNAME = wls-uber
REGISTRY = 080385600816.dkr.ecr.us-east-1.amazonaws.com
HASHTAG = $(shell git rev-parse --short HEAD)
DEV_TAG = latest
TAG = 1.0.0
LOGIN:=$(shell aws ecr get-login --no-include-email)
WEBLOGIC_APP_VERSION=2017.5.0-RELEASE

all : clean push-dev

get-apps:
	mkdir -p applications
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/vmmanager/$(WEBLOGIC_APP_VERSION)/vmmanager-$(WEBLOGIC_APP_VERSION).ear -O applications/VmManager.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/applicationsupport/$(WEBLOGIC_APP_VERSION)/applicationsupport-$(WEBLOGIC_APP_VERSION).ear -O applications/applicationsupport.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/bizAudits/$(WEBLOGIC_APP_VERSION)/bizAudits-$(WEBLOGIC_APP_VERSION).ear -O applications/bizAudits.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/callData/$(WEBLOGIC_APP_VERSION)/callData-$(WEBLOGIC_APP_VERSION).ear -O applications/callData.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/callername-war/$(WEBLOGIC_APP_VERSION)/callername-war-$(WEBLOGIC_APP_VERSION).war -O applications/callername.war
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/didmanager/$(WEBLOGIC_APP_VERSION)/didmanager-$(WEBLOGIC_APP_VERSION).ear -O applications/didmanager.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/domain-lnp/$(WEBLOGIC_APP_VERSION)/domain-lnp-$(WEBLOGIC_APP_VERSION).ear -O applications/domain-lnp.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/domain-party/$(WEBLOGIC_APP_VERSION)/domain-party-$(WEBLOGIC_APP_VERSION).ear -O applications/domain-party.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/domain-shipment/$(WEBLOGIC_APP_VERSION)/domain-shipment-$(WEBLOGIC_APP_VERSION).ear -O applications/domain-shipment.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/domain-voicemail/$(WEBLOGIC_APP_VERSION)/domain-voicemail-$(WEBLOGIC_APP_VERSION).ear -O applications/domain-voicemail.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/emergency-address-webservice/$(WEBLOGIC_APP_VERSION)/emergency-address-webservice-$(WEBLOGIC_APP_VERSION).war -O applications/emergency-address-webservice.war
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/eventsupport/$(WEBLOGIC_APP_VERSION)/eventsupport-$(WEBLOGIC_APP_VERSION).ear -O applications/eventsupport.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/legacysupport/$(WEBLOGIC_APP_VERSION)/legacysupport-$(WEBLOGIC_APP_VERSION).ear -O applications/legacysupport.ear
	wget http://maven.dev.s.vonagenetworks.net/vonage-application-modules/wars/properties-server-webapp-2017.9.18-RELEASE.war -O applications/properties-server.war
	wget http://maven.dev.s.vonagenetworks.net/vonage-application-modules/wars/log4j-config-webapp-2017.9.18-RELEASE.war -O applications/log4j-config.war
	wget http://maven.dev.s.vonagenetworks.net/vonage-application-modules/wars/vonage-email-webapp-2017.9.18-RELEASE.war -O applications/vonage-email.war
	wget http://maven.dev.s.vonagenetworks.net/jamon/wars/jamon-1.0.0.war -O applications/jamon.war
	wget http://maven.dev.s.vonagenetworks.net/billing-services/ears/billing-services-5.5.0.ear -O applications/billing-services.ear
	wget http://maven.dev.s.vonagenetworks.net/vonage-application-modules/ears/presentation-services-webapp-2017.9.18-RELEASE.ear -O applications/presentation-services.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/processor-lnp/$(WEBLOGIC_APP_VERSION)/processor-lnp-$(WEBLOGIC_APP_VERSION).ear -O applications/processor-lnp.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/provisiondidmanager/$(WEBLOGIC_APP_VERSION)/provisiondidmanager-$(WEBLOGIC_APP_VERSION).ear -O applications/provisiondidmanager.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/queuetool-war/$(WEBLOGIC_APP_VERSION)/queuetool-war-$(WEBLOGIC_APP_VERSION).war -O applications/queuetool.war
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/service-nens-tcs/$(WEBLOGIC_APP_VERSION)/service-nens-tcs-$(WEBLOGIC_APP_VERSION).ear -O applications/service-nens-tcs.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/service-nens/$(WEBLOGIC_APP_VERSION)/service-nens-$(WEBLOGIC_APP_VERSION).ear -O applications/service-nens.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/service-policy-validation/$(WEBLOGIC_APP_VERSION)/service-policy-validation-$(WEBLOGIC_APP_VERSION).ear -O applications/service-policy-validation.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/service-ship-ear/$(WEBLOGIC_APP_VERSION)/service-ship-ear-$(WEBLOGIC_APP_VERSION).ear -O applications/service-ship.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/service-shipping/$(WEBLOGIC_APP_VERSION)/service-shipping-$(WEBLOGIC_APP_VERSION).ear -O applications/service-shipping.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/service-userConfirmation/$(WEBLOGIC_APP_VERSION)/service-userConfirmation-$(WEBLOGIC_APP_VERSION).ear -O applications/service-userConfirmation.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/usageeventbpa/$(WEBLOGIC_APP_VERSION)/usageeventbpa-$(WEBLOGIC_APP_VERSION).ear -O applications/usageeventbpa.ear
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/voicemail-webservice/$(WEBLOGIC_APP_VERSION)/voicemail-webservice-$(WEBLOGIC_APP_VERSION).war -O applications/voicemail-webservice.war
	wget http://maven.dev.s.vonagenetworks.net:8080/nexus/content/repositories/Vonage-m2/com/vonage/weblogic/core-services/$(WEBLOGIC_APP_VERSION)/core-services-$(WEBLOGIC_APP_VERSION).ear -O applications/core-services.ear
	cp wls-exporter.war applications
container-base:
	exec ${LOGIN}
	docker build -f Dockerfile.generic -t oracle/weblogic:12.2.1.3-generic .	

container: container-base get-apps
	docker build -f Dockerfile.standalone -t $(APPNAME):$(HASHTAG) .

push-dev: container
	docker tag $(APPNAME):$(HASHTAG) ${REGISTRY}/$(APPNAME):$(DEV_TAG)
	docker push ${REGISTRY}/$(APPNAME):$(DEV_TAG)
	
push: container
	docker tag $(APPNAME):$(HASHTAG) ${REGISTRY}/$(APPNAME):$(TAG)
	docker push ${REGISTRY}/$(APPNAME):$(TAG)

clean:
	rm -fr applications
.PHONY: all container push clean

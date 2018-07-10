domain_name  = os.environ.get("DOMAIN_NAME", "uber")
prometheus_pwd = os.environ.get("PROMETHEUS_PASS", "prometheus123")


connect(adminServerName='AdminServer')

cd("/SecurityConfiguration/" + domainName + "/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator")
cmo.createUser("prometheus" , prometheus_pwd, "prometheus monitoring user")
cmo.addMemberToGroup("Monitors", "prometheus")

# Exit WLST
# =========
exit()
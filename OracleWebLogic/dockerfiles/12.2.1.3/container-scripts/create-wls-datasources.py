from java.io import FileInputStream


domain_name  = os.environ.get("DOMAIN_NAME", "uber")
admin_name  = os.environ.get("ADMIN_NAME", "AdminServer")
admin_username  = os.environ.get("ADMIN_USERNAME", "weblogic")
admin_pass  = "ADMIN_PASSWORD"
admin_port   = int(os.environ.get("ADMIN_PORT", "7001"))
domain_path  = '/u01/oracle/user_projects/domains/%s' % domain_name
production_mode = os.environ.get("PRODUCTION_MODE", "dev")
external_dns_name = os.environ.get("EXTERNAL_DNS_NAME", "wls-uber.va0.ctnr.dev.vonagenetworks.net")


propInputStream = FileInputStream(domain_path + "/datasources/wls-uber-datasources.properties")
configProps = Properties()
configProps.load(propInputStream)
totalDataSources=configProps.get("DS_TOTAL")

# Open domain template
# ======================
readDomain("/u01/oracle/user_projects/domains/" + domain_name)


cd('/Servers/AdminServer')
set('ExternalDNSName', external_dns_name)

i=1
while (i <= int(totalDataSources)) :
    try:
        dsName=configProps.get("DS_" + str(i) + "_DS_NAME")
        jndiName=configProps.get("DS_" + str(i) + "_JNDI_NAME")
        drvrUrl=configProps.get("DS_" + str(i) + "_DRVR_URL")
        drvrName=configProps.get("DS_" + str(i) + "_DRVR_NAME")
        drvrUser=configProps.get("DS_" + str(i) + "_DRVR_USR")
        drvrPass=configProps.get("DS_" + str(i) + "_DRVR_PASS")
        initCap=configProps.get("DS_" + str(i) + "_INIT_CAP")
        maxCap=configProps.get("DS_" + str(i) + "_MAX_CAP")
        capIncr=configProps.get("DS_" + str(i) + "_CAP_INCR")
        stmtCacheSize=configProps.get("DS_" + str(i) + "_STMT_CACHE_SIZE")
        shrFreq=configProps.get("DS_" + str(i) + "_SHRNK_FREQ")
        testConRes=configProps.get("DS_" + str(i) + "_TEST_CON_RES")
        testTableName=configProps.get("DS_" + str(i) + "_TEST_TAB_NAME")
        transMethod=configProps.get("DS_" + str(i) + "_TRANS_METHOD")
        cd('/')
        create(dsName, 'JDBCSystemResource')
        cd('/JDBCSystemResource/' + dsName)
        set('Target','AdminServer')
         
        cd('/JDBCSystemResource/' + dsName + '/JdbcResource/' + dsName)
        cmo.setName(dsName)
         
        #print 'create JDBCDataSourceParams'
        cd('/JDBCSystemResource/' + dsName + '/JdbcResource/' + dsName)
        create(dsName,'JDBCDataSourceParams')
        cd('JDBCDataSourceParams/' + dsName)
        set('JNDIName', jndiName)
        set('GlobalTransactionsProtocol', transMethod)
         
        #print 'create JDBCDriverParams'
        cd('/JDBCSystemResource/' + dsName + '/JdbcResource/' + dsName)
        create('myJdbcDriverParams','JDBCDriverParams')
        cd('JDBCDriverParams/NO_NAME_0')
        set('DriverName',drvrName)
        set('URL',drvrUrl)
        set('PasswordEncrypted', drvrPass)

        # Set Driver property parameters
        #print 'create JDBCDriverParams Properties'
        create('myProperties','Properties')
        cd('Properties/NO_NAME_0')
        create('user','Property')
        cd('Property')
        cd('user')
        set('Value', drvrUser)
         
        #print 'create JDBCConnectionPoolParams'
        
        cd('/JDBCSystemResource/' + dsName + '/JdbcResource/' + dsName)
        create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
        cd('JDBCConnectionPoolParams/NO_NAME_0')
        set('TestTableName',testTableName)
        set('InitialCapacity', int(initCap))
        set('MaxCapacity', int(maxCap))
        set('CapacityIncrement', int(capIncr))
        set('StatementCacheSize', int(stmtCacheSize))
        set('ShrinkFrequencySeconds', int(shrFreq))
        set('TestConnectionsOnReserve', int(testConRes))
        
    except:
        print "[Error]: Cannot create datasource : " + dsName + " !! "
        dumpStack()
        
    i = i + 1

# Write Domain
# ============
updateDomain()
closeDomain()

# Exit WLST
# =========
exit()


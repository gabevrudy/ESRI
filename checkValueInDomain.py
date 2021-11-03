import arcpy

feature = r"abc"
domains = arcpy.da.ListDomains(feature)

def testDomain(value, domainName):
    domainList = [] #create empty list
    for domain in domains: #search all domains and find one that matches the name of the domain
        if domainName == domain.name:
            coded_values = domain.codedValues
            for val in coded_values.items():#for value in dictionary of values, append to a list
                domainList.append(val[0])
            if value in domainList: #do something
                print(str(value) + ' is in ' + str(domain))
            else:
                print(str(value) + ' is NOT in ' + str(domain))

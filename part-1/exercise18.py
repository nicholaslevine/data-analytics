def acronyms(string):
    result = []
    stringArray = string.split(" ")
    for string in stringArray:
        if (string.isupper()):
            adjustedString = string.strip(",").strip("(").strip(")").strip(".")
            result.append(adjustedString)
    return result

print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))
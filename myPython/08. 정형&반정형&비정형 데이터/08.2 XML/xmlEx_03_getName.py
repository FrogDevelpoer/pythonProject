from xml.etree.ElementTree import parse

tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
# print(type(myroot))
# print('-' * 30)

families = myroot.findall('가족')
# print(type(families))
# print('-' * 30)

# print(families)
# print('-' * 30)

for onefamily in families:
    for onesaram in onefamily:
        if len(onesaram) >= 1:
            print(onesaram[0].text)
        else:
            print(onesaram.attrib['이름'])
    print('-' * 30)
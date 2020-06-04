import lxml.etree
xml_file = lxml.etree.parse("test.xml")
xml_validator = lxml.etree.XMLSchema(file="schema_test.xsd")

is_valid = xml_validator.validate(xml_file)
print(is_valid)
print(xml_validator.error_log)
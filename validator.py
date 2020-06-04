import lxml.etree
xml_file = lxml.etree.parse("xml_ex/test_prices.xml")
xml_validator = lxml.etree.XMLSchema(file="schemas/price_schema.xsd")

is_valid = xml_validator.validate(xml_file)
print(is_valid)
print(xml_validator.error_log)
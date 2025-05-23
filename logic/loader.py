import xml.etree.ElementTree as ET

def load_priorities(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    priorities = {}

    for table in root.findall("table"):
        category = table.get("name")
        priorities[category] = {}

        for level in table.findall("row"):
            grade = level.get("grade")
            text = level.text.strip() if level.text else ""
            priorities[category][grade] = text

    return priorities
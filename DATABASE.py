import xml.etree.ElementTree as ET

class Database:

    def __init__(self):
        self.name_of_file = "Connection_data.xml"
        self.tree = ET.parse(self.name_of_file)
        self.root = self.tree.getroot()

        # define public variables
        self.list_of_name = []
        self.dictioary_of_interface = {}
        self.dictioary_of_ip = {}
        self.dictioary_of_mask = {}
        self.dictioary_of_gate = {}

        # do init
        self.load_file()

    def load_file(self):
        for one in self.root:
            self.list_of_name.append(one.attrib.get('name'))
            for node in one:
                if node.tag == "interface":
                    self.dictioary_of_interface[one.attrib.get('name')] = node.text
                if node.tag == "ip":
                    self.dictioary_of_ip[one.attrib.get('name')] = node.text
                if node.tag == "mask":
                    self.dictioary_of_mask[one.attrib.get('name')] = node.text
                if node.tag == "gate":
                    self.dictioary_of_gate[one.attrib.get('name')] = node.text

    def add_data(self, name, ip, interface, mask, gate):
        # test of key
        if self.list_of_name.__contains__(name):
            return 0

        # add data in to dictionaries
        self.list_of_name.append(name)
        self.dictioary_of_ip[name] = ip
        self.dictioary_of_interface[name] = interface
        self.dictioary_of_mask[name] = mask
        self.dictioary_of_gate[name] = gate

        # add into xml file
        ET.SubElement(self.root, "connection", name = name ).text = "\n"
        for one in self.root:
            if name == one.attrib.get('name'):
                ET.SubElement(one, "interface").text = interface
                ET.SubElement(one, "ip").text = ip
                ET.SubElement(one, "mask").text = mask
                ET.SubElement(one, "gate").text = gate
        self.tree.write(self.name_of_file)
        return 1

    def delete_data(self, name):
        # delete item form dictionary
        self.list_of_name.remove(name)
        self.dictioary_of_ip.__delitem__(name)
        self.dictioary_of_interface.__delitem__(name)
        self.dictioary_of_mask.__delitem__(name)
        self.dictioary_of_gate.__delitem__(name)

        # delete from xml file
        for one in self.tree.findall("connection"):
            if one.attrib.get("name") == name:
                self.root.remove(one)
                break
        self.tree.write(self.name_of_file)

    def print_data(self):
        print(self.list_of_name)
        print(self.dictioary_of_ip)
        print(self.dictioary_of_interface)
        print(self.dictioary_of_mask)
        print(self.dictioary_of_gate)


if __name__ == '__main__':
    a = Database()
    a.print_data()
    a.add_data("Test2", "192.168.1.5","Wi+fi","0.0.0.0","192.168.1.1")
    a.delete_data("Test2")

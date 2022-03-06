import matplotlib.pyplot as plt
from Sniff import *

class Capture:

    # Singleton Class check
    _instance = None
    @staticmethod
    def getInstance():
        if Capture._instance == None:
            Capture()
        return Capture._instance

    # Init function
    def __init__(self, captures=''):
        if Capture._instance != None:
            raise Exception("This class is a Singleton Class!")
        else:
            Capture._instance = self
            self.captures = captures
            self.dictionary = {'UDP':0}
            self.dictionary.update({'TCP':0})
            self.TCP_counter = 0
            self.UDP_counter = 0
            self.packages_dictionary = dict()

    # Getter for sniffed elements
    def getter(self):
        return self.captures

    # Setter for sniffed elements
    def setter(self, captures):
        self.captures = captures

    # Method that converts sniffed elements into a dictionary
    # It also counts the number of TCP/UDP elements
    def Dict_converter(self):
        i = 0
        self.dictionary['TCP'] = 0
        self.dictionary['UDP'] = 0
        for packet in self.captures:
            packet_dict = {}
            for line in packet.show(dump=True).split('\n'):
                if '###' in line:
                    layer = line.strip('#[] ')
                    packet_dict[layer] = {}
                elif '=' in line:
                    key, val = line.split('=', 1)
                    packet_dict[layer][key.strip()] = val.strip()
            self.packages_dictionary[i] = packet_dict
            i += 1
            if 'IP' in packet_dict.keys():
                if packet_dict['IP']['proto'] == 'tcp':
                    self.TCP_counter = 1
                if packet_dict['IP']['proto'] == 'udp':
                    self.UDP_counter = 1
            self.dictionary['TCP'] += self.TCP_counter
            self.dictionary['UDP'] += self.UDP_counter
            self.TCP_counter = 0
            self.UDP_counter = 0

    # Method that saves the dictionary as a JSON file
    def Save_JSON_file(self):
        from __main__ import input_path
        self.Dict_converter()
        filepath = str(input_path.get()) + '\\Capture.json'
        f = open(filepath, "w")
        for packet_dict in self.packages_dictionary.values():
            package = Sniff()
            if 'Ethernet' in packet_dict.keys():
                package.Ethernet_dst = packet_dict['Ethernet']['dst']
                package.Ethernet_src = packet_dict['Ethernet']['src']
            if 'IP' in packet_dict.keys():
                package.IP_dst = packet_dict['IP']['dst']
                package.IP_src = packet_dict['IP']['src']
                package.IP_version = packet_dict['IP']['version']
                package.IP_proto = packet_dict['IP']['proto']
            if 'TCP' in packet_dict.keys():
                package.UDP_dport = packet_dict['TCP']['dport']
                package.UDP_sport = packet_dict['TCP']['sport']
            if 'UDP' in packet_dict.keys():
                package.UDP_dport = packet_dict['UDP']['dport']
                package.UDP_sport = packet_dict['UDP']['sport']
            f.write(package.__str__())
            f.write('\n')
            del package
        return True

    # Method that generates the TCP/UDP graph
    def Statistics(self):
        self.Dict_converter()
        slices = [self.dictionary['UDP'], self.dictionary['TCP']]
        activities = ['UDP','TCP']
        cols = ['c', 'm']
        plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True,autopct='%.2f%%')
        plt.title('Sniffed elements')
        plt.show()
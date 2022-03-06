import json

class Sniff:

    # Init function
    def __init__(self, Ethernet_dst='', Ethernet_src='', IP_dst='', IP_src='',
                 IP_version='', IP_proto='', TCP_sport='', TCP_dport='', UDP_sport='', UDP_dport=''):
        self.Ethernet_dst = Ethernet_dst
        self. Ethernet_src =  Ethernet_src
        self.IP_dst = IP_dst
        self.IP_src = IP_src
        self.IP_version = IP_version
        self.IP_proto = IP_proto
        self.TCP_sport = TCP_sport
        self.TCP_dport = TCP_dport
        self.UDP_sport = UDP_sport
        self.UDP_dport = UDP_dport
        self.dictionary = dict()

    # Str function (override) to create the dictionary easier
    def __str__(self):
        dictionary = dict()
        dictionary['Ethernet'] = {'dst':self.Ethernet_dst}
        dictionary['Ethernet'].update({'src':self.Ethernet_src})
        dictionary['IP'] = {'dst':self.IP_dst}
        dictionary['IP'].update({'src':self.IP_src})
        dictionary['IP'].update({'version':self.IP_version})
        dictionary['IP'].update({'proto':self.IP_proto})
        if self.TCP_sport != '' or self.TCP_dport != '':
            dictionary['TCP'] = {'sport':self.TCP_sport}
            dictionary['TCP'].update({'dport':self.TCP_dport})
        if self.UDP_sport != '' or self.UDP_dport != '':
            dictionary['UDP'] = {'sport':self.UDP_sport}
            dictionary['UDP'].update({'dport': self.UDP_dport})
        return json.dumps(dictionary)
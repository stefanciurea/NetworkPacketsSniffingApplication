# NetworkPacketsSniffingApplication
Using a Tkinter GUI to work with Scapy (a powerful interactive packet manipulation program). Sniffed packets are stored as a JSON file that can be saved to a specific path.

Before running make sure that you  have installed NPCAP (https://npcap.com/).

This program is used to sniff (network packet sniffing) elements for a specific period of time (you can set that). After sniffing you can see a graph for TCP/UDP elements and save the sniffed elements in a JSON file using the format:

{
 "Ethernet": {"dst": "...", "src": "..."}, 
 "IP": {"dst": "...", "src": "...", "version": "...", "proto": "..."}, "UDP": {"sport": "...", "dport": "..."}
}

How to use it: 
1. After runing main.py file a new Tkinter window will open, you have to click on it and input the time (in seconds) you want the sniffing to be made.
2. After that time you will see the number of elements that you sniffed.
3. You can input the path and press "Save as JSON" button.
4. You can see the graph after pressing "Show statistics".

Python packages:
- json
- scapy
- matplotlib
- tkinter
- Capture

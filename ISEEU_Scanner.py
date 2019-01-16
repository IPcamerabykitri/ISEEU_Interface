# Scanning Module
import os
import sys
from Hardware_Scan_Module import firmware_check

def Port_Scan():
    print("Port_Scan!")

def Ssh_Scan():
    print("SSH_Scan!")

def Telnet_Scan():
    print("Telnet_Scan!")

def Http_Scan():
    print("HTTP_SCAN!")

def Packet_Scan():
    print("Packet_SCAN!")

def Backdoor_Scan():
    print("Backdoor_SCAN!")

def Firmware_Scan(Path):
    firmware_check.Check_boot_sequence(Path)

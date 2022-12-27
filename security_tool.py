# Ağ Güvenliği Test Aracı

import socket
import sys
import subprocess
import os

def scan_network(network, subnet):
  # Ağınızdaki cihazları taramak için bir aralık belirleyin
  start = 1
  end = 254
  devices = []
  
  # Ağınızdaki cihazları taramaya başlayın
  for host in range(start, end+1):
    # Her cihaza bir ping gönderin
    address = network + str(host)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    # Eğer cihaz yanıt verirse, cihazın IP adresini ve cihaz türünü ekrana yazdırın
    if s.connect_ex((address, 135)):
      print(address + " çalışıyor")
      # Cihaz türünü tespit etmek için nmap kullanın
      cmd = "nmap -O " + address
      proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      result = proc.stdout.read()
      device_type = result.decode("utf-8").split("\n")[-2]
      
      # Cihaz üzerinde açık portları tespit etmek için nmap kullanın
      cmd = "nmap -p- " + address
      proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      result = proc.stdout.read()
      open_ports = result.decode("utf-8").split("\n")[-2]
      
      # Cihaz üzerinde çalışan servisleri tespit etmek için nmap kullanın
      cmd = "nmap -sV " + address
      proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      result = proc.stdout.read()
      services = result.decode("utf-8").split("\n")[-2]
      
      # Cihaz üzerinde güncel olmayan yazılım ve servisler tespit etmek için nessus kullanın
      cmd = "nessus " + address
      proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      result = proc.stdout.read()
      outdated_software = result.decode("utf-8").split("\n")[-2]
  
      # Cihaz bilgilerini saklayın
      device = {
      "ip_address": address,
      "device_type": device_type,
      "open_ports": open_ports,
      "services": services,
      "outdated_software": outdated_software
      }
      devices.append(device)
      #Tarama işlemini bitirin
      #print("Tarama tamamlandı.")
      #return devices

def display_device_info(devices):
  for device in devices:
      print("IP Adresi:", device["ip_address"])
      print("Cihaz Türü:", device["device_type"])
      print("Açık Portlar:", device["open_ports"])
      print("Çalışan Servisler:", device["services"])
      print("Güncel Olmayan Yazılım ve Servisler:", device["outdated_software"])

def generate_report(devices):
  report = ""
  for device in devices:
    report += "IP Adresi: " + device["ip_address"] + "\n"
    report += "Cihaz Türü: " + device["device_type"] + "\n"
    report += "Açık Portlar: " + device["open_ports"] + "\n"
    report += "Çalışan Servisler: " + device["services"] + "\n"
    report += "Güncel Olmayan Yazılım ve Servisler: " + device["outdated_software"] + "\n"
    report += "----------------------------" + "\n"
  with open("report.txt", "w") as file:
    file.write(report)
  print("Rapor oluşturuldu: report.txt")
  

def main():
  while True:
    print("Ağ Güvenlik Test Aracı")
    print("1. Ağı tarama")
    print("2. Cihaz bilgilerini görüntüle")
    print("3. Rapor oluştur")
    print("4. Çıkış")
    selection = input("Seçiminiz: ")
    
    if selection == "1":
      network = input("Enter the network IP address: ")
      subnet = input("Enter the subnet mask: ")
      device = scan_network(network, subnet)
    elif selection == "2":
      display_device_info(device)
    elif selection == "3":
      generate_report(device)
    elif selection == "4":
      sys.exit()
    else:
        print("Geçersiz seçim.")
        main()
  

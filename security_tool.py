# Ağ Güvenliği Test Aracı

import socket
import sys
import subprocess
import os

def main():
  while True:
    print("Ağ Güvenlik Test Aracı")
    print("1. Ağı tarama")
    print("2. Cihaz bilgilerini görüntüle")
    print("3. Rapor oluştur")
    print("4. Çıkış")
    choice = input("Seçiminiz: ")
    
    if choice == "1":
      network = input("Enter the network IP address: ")
      subnet = input("Enter the subnet mask: ")
      scan_network(network, subnet)
    elif choice == "2":
      display_device_info(devices)
    elif choice == "3":
      generate_report(devices)
    elif choice == "4":
      sys.exit()
    else:
      print("Geçersiz seçim.")
      
if __name__ == "__main__":
  main()

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
      print("Tarama tamamlandı.")
      return devices
  

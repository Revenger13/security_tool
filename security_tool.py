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
      
#if __name__ == "__main__":
 # main()

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
      print(result)
    else:
      print(address + " çalışmıyor")
#Tarama işlemini bitirin
print("Tarama tamamlandı.")
sys.exit()




# Ağınızın IP adresini ve alt ağ maskesini girin
network = "192.168.1.0"
subnet = "255.255.255.0"

def display_device_info(devices):
  for device in devices:
    print("IP adresi: " + device["ip_address"])
    print("Cihaz türü: " + device["device_type"])
    print("Açık portlar: " + device["open_ports"])
    print("Servisler: " + device["services"])
    print("Güncel olmayan yazılım ve servisler: " + device["outdated_software"])
    print("-------------------")

def generate_report(devices):
  report_file = open("report.txt", "w")
  for device in devices:
    report_file.write("IP adresi: " + device["ip_address"] + "\n")
    report_file.write("Cihaz türü: " + device["device_type"] + "\n")
    report_file.write("Açık portlar: " + device["open_ports"] + "\n")
    report_file.write("Servisler: " + device["services"] + "\n")


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
    print(result)
    
    # Cihaz üzerinde açık portları tespit etmek için nmap kullanın
    cmd = "nmap -p- " + address
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    result = proc.stdout.read()
    print(result)
    
    # Cihaz üzerinde çalışan servisleri tespit etmek için nmap kullanın
    cmd = "nmap -sV " + address
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    result = proc.stdout.read()
    print(result)
    
    # Cihaz üzerinde güncel olmayan yazılım ve servisler tespit etmek için nessus kullanın
    cmd = "nessus " + address
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    result = proc.stdout.read()
    print(result)
    
  else:
    print(address + " çalışmıyor")

# Tarama işlemini bitirin
print("Tarama tamamlandı.")
sys.exit()

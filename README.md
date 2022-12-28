# Profesyonel Ağ Güvenliği Test Aracı

**Bu araç, ağınızdaki cihazları tarar ve cihazların IP adreslerini, cihaz türlerini, açık portlarını, çalışan servislerini ve güncel olmayan yazılım ve servislerini tespit etmek için farklı araçlar kullanır. Bu araçlar arasında nmap, nessus gibi araçlar yer alır.**

# Özellikler

**Ağınızdaki cihazları tarar ve her cihaza bir ping gönderir.**

**Eğer cihaz yanıt verirse, cihazın IP adresini, cihaz türünü, açık portlarını, çalışan servislerini ve güncel olmayan yazılım ve servislerini tespit eder.
Tarama sonucunu ekrana yazdırır.**

# Kurulum

**Bu araç, Python 3 ile yazılmıştır. Öncelikle, Python 3'ün kurulu olduğundan emin olun. Daha sonra, aşağıdaki komutları kullanarak gerekli kütüphaneleri yükleyin:**

- `pip install socket`

- `pip install sys`

- `pip install subprocess`

- `pip install os`

# Kullanım

*Araç, aşağıdaki şekilde çalıştırılabilir:*

- `git clone https://github.com/F4KOR4LL/security_tool.git`

- `cd security_tool`

- `python security_tool.py`

*Araç çalıştırıldıktan sonra, ağınızın IP adresini ve alt ağ maskesini girmeniz istenecektir. Bu bilgileri girdikten sonra, ağınızdaki cihazlar taranmaya başlayacaktır. Tarama sonucu, ekrana yazdırılacaktır.*

# Notlar

*Bu araç, sadece bir ağ güvenliği test aracı örneğidir ve ağınızın tamamen güvenliğini test etmek için yeterli olmayabilir*

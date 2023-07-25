import os

# Defina as configurações da proxy
proxy_port = 3128
allowed_networks = ["192.168.0.0/24", "10.0.0.0/8"]

# Configure as regras de acesso
access_rules = [
    "allow all",
    "deny all"
]

# Caminho para o arquivo de configuração do Squid
squid_conf_path = "/etc/squid/squid.conf"

# Atualize o arquivo de configuração do Squid
with open(squid_conf_path, "w") as f:
    f.write(f"http_port {proxy_port}\n")
    f.write("acl allowed_networks src ")
    f.write(" ".join(allowed_networks))
    f.write("\n")
    f.write("http_access ")
    f.write("\nhttp_access ".join(access_rules))
    f.write("\n")

# Reinicie o serviço do Squid
os.system("systemctl restart squid")

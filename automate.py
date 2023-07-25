import subprocess

# Define as configurações do proxy
proxy_port = 3128
allowed_networks = ["192.168.0.0/24", "10.0.0.0/8"]  # Exemplo de redes permitidas

# Define as regras de acesso
access_rules = [
    "http_access allow localhost",
    "http_access allow all"
]

# Define o caminho do arquivo de configuração do Squid
squid_conf_path = "/etc/squid/squid.conf"

# Adiciona as regras de acesso ao arquivo de configuração
with open(squid_conf_path, "a") as squid_conf:
    squid_conf.write("\n")
    squid_conf.write("# Configuração adicionada automaticamente\n")
    squid_conf.write(f"http_port {proxy_port}\n")
    for rule in access_rules:
        squid_conf.write(f"{rule}\n")
    squid_conf.write("\n")
    for network in allowed_networks:
        squid_conf.write(f"acl allowed_networks src {network}\n")
        squid_conf.write(f"http_access allow allowed_networks\n")

# Reinicia o serviço do Squid
subprocess.run(["systemctl", "restart", "squid"])

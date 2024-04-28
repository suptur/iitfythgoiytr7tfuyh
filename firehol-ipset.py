import requests
import os
from tqdm import tqdm
import re

# List of URLs to download
urls = [
    "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/alienvault_reputation.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/alienvault_reputation.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/asprox_c2.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/asprox_c2.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_banjori.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_banjori.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_bebloh.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_bebloh.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_c2.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_c2.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_cl.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_cl.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_cryptowall.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_cryptowall.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_dircrypt.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_dircrypt.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_dyre.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_dyre.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_geodo.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_geodo.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_hesperbot.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_hesperbot.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_matsnu.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_matsnu.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_necurs.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_necurs.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_p2pgoz.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_p2pgoz.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_pushdo.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_pushdo.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_pykspa.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_pykspa.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_qakbot.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_qakbot.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_ramnit.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_ramnit.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_ranbyus.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_ranbyus.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_simda.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_simda.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_suppobox.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_suppobox.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_symmi.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_symmi.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_tinba.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_tinba.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_volatile.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bambenek_volatile.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bds_atif.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bds_atif.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_blockchain_info_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_blockchain_info_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_blockchain_info_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_blockchain_info_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_blockchain_info_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_blockchain_info_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_apache.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_apache.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_bots.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_bots.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_bruteforce.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_bruteforce.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_ftp.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_ftp.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_imap.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_imap.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_mail.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_mail.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_sip.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_sip.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_ssh.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_ssh.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_strongips.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de_strongips.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_net_ua.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_net_ua.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botvrij_dst.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botvrij_dst.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botvrij_src.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botvrij_src.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bruteforceblocker.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bruteforceblocker.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/ciarmy.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/ciarmy.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleanmx_phishing.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleanmx_phishing.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleanmx_viruses.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleanmx_viruses.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_new_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_top20.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_top20.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated_1d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated_30d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cleantalk_updated_7d.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts_browser.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts_browser.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts_optional.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts_optional.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_ips.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_ips.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cta_cryptowall.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cta_cryptowall.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cybercrime.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cybercrime.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/dm_tor.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/dm_tor.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/dshield_top_1000.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/dshield_top_1000.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/dyndns_ponmocup.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/dyndns_ponmocup.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_14072015_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_14072015_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_14072015q_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_14072015q_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_22072014a_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_22072014a_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_22072014b_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_22072014b_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_22072014c_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_22072014c_com.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_atomictrivia_ru.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_atomictrivia_ru.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_auth_update_ru.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_auth_update_ru.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_burmundisoul_ru.ipset",
"https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/esentire_burmundisoul_ru.ipset",
        # Add more URLs here
]

# Function to download a file and show progress
def download_file(url, dest_folder):
    filename = url.split("/")[-1]
    filepath = os.path.join(dest_folder, filename)
    with open(filepath, "wb") as file, requests.get(url, stream=True) as response:
        total_size = int(response.headers.get("content-length", 0))
        progress_bar = tqdm(total=total_size, unit="B", unit_scale=True, desc=f"Downloading {filename}")
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            progress_bar.update(len(data))
        progress_bar.close()

    return filepath

# Function to convert IPv4 address to "||ipv4 address^" format
def convert_ipv4(line):
    ipv4_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ipv4_addresses = re.findall(ipv4_pattern, line)
    for ipv4 in ipv4_addresses:
        line = line.replace(ipv4, f"||{ipv4}^")
    return line

# Download files and merge into a single file
merged_lines = set()  # Using a set for faster duplicate removal
download_folder = "downloads_ipsets"
os.makedirs(download_folder, exist_ok=True)
for url in urls:
    filepath = download_file(url, download_folder)
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if not line.startswith(("@@", "!", "#")):  # Exclude lines starting with "@@", "!", "#"
                line = convert_ipv4(line)
                merged_lines.add(line.strip())

# Save updated file with unique lines and remove lines starting with "!"
merged_unique_file = "firehol-ipset-all.txt"
with open(merged_unique_file, "w", encoding="utf-8") as file:
    for line in sorted(merged_lines):  # Sort lines alphabetically
        file.write(line + "\n")

# Delete downloaded files and merged_unique.txt
download_folder = "downloads_ipsets"
#os.remove(merged_unique_file)
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    os.remove(file_path)

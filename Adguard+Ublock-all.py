import requests
import os
from tqdm import tqdm

# List of URLs to download
urls = [
   "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Dangerous/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/advertising_networks.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_css.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_html.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_js.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_urls_unsorted.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/direct_adverts.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/specific_web_sites.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Mobile/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Other/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/advertising_networks.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_html.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_js.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/direct_adverts.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/specific_web_sites.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_css.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_urls_unsorted.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Other/sections/annoyances.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Other/sections/self-promo.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Other/sections/tweaks.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Widgets/sections/widgets.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/allowlist_stealth.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/banner_sizes.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/cname_adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/content_blocker.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/cryptominers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/foreign.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/popups_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/popups_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/popups_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/Belarusian/sections/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/Bulgarian/sections/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/Kazakh/sections/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Social/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Spyware/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/allowlist_app.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/allowlist_web.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/specific_app.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/specific_web.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/popups.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/social_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cname_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile_allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/allowlist.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/UsefulAdsFilter/sections/usefulads.txt",
##############----UBLOCK-Origin-_UASSET-ALL-STOCK---
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-cookies.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances-others.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badlists.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badlists.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2024.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2025.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-mobile.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/lan-block.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/legacy.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/ubo-link-shorteners.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/ubol-filters.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
####################---END----#############################
    # Add more URLs as needed
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

# Download files and merge into a single file
merged_lines = set()  # Using a set for faster duplicate removal
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)
for url in urls:
    filepath = download_file(url, download_folder)
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
             if not line.startswith(("!", "#")):  # Exclude lines starting with "!"
                merged_lines.add(line.strip())

# Save updated file with unique lines and remove lines starting with "!"
merged_unique_file = "Adguard+Ublock-all.txt"
with open(merged_unique_file, "w", encoding="utf-8") as file:
    for line in sorted(merged_lines):  # Sort lines alphabetically
        file.write(line + "\n")

# Delete downloaded files and merged_unique.txt
download_folder = "downloads"
# os.remove(merged_unique_file)
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    os.remove(file_path)

import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# List of text file URLs
urls = [
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Dangerous/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/advertising_networks.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_css.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_html.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_js.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/common_urls_unsorted.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/direct_adverts.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/English/specific_web_sites.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Mobile/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Other/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/advertising_networks.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_html.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_js.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/direct_adverts.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/specific_web_sites.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_css.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Russian/common_urls_unsorted.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Cookies/sections/cookies_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/MobileApp/sections/mobile-app_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Other/sections/annoyances.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Other/sections/self-promo.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Other/sections/tweaks.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Widgets/sections/widgets.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers_firstparty.txt",
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
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/popups_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/popups_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/subscriptions_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/adservers_firstparty.txt",
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
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/UkrainianFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/common-sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/DutchFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Social/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ExperimentalFilter/sections/Spyware/filter.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/FrenchFilter/sections/adservers_firstparty.txt",
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
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/JapaneseFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/specific_app.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/specific_web.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/popups.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/social_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SocialFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/adservers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/antiadblock.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/replace.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpanishFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cname_trackers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_general.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/cookies_specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_elemhide.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_extensions.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/mobile.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/tracking_servers_firstparty.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/general_url.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TrackParamFilter/sections/specific.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/adservers.txt",
"https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/adservers_firstparty.txt",
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
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/experimental.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt",
"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt",
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

##############################   HaGeZi #########################################
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/popupads.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/anti.piracy.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.apple.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.amazon.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.huawei.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.winoffice.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.samsung.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.tiktok.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.tiktok.extended.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.tiktok.extended.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.roku.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.vivo.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.oppo-realme.txt",
"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.xiaomi.txt",

####################################### EASY-list  #######################################
"https://easylist.to/easylist/easyprivacy.txt",
"https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
"https://easylist.to/easylist/easylist.txt",
"https://secure.fanboy.co.nz/fanboy-annoyance.txt",
"https://easylist.to/easylist/fanboy-social.txt",

    # Add more URLs here
]

# Folder path inside repo
output_folder = "Filters"
os.makedirs(output_folder, exist_ok=True)  # Create folder if not exists

# Output file path
output_file = os.path.join(output_folder, "adblock_aggressive.txt")

# Function to download a single file
def download_txt(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        print(f"✅ Downloaded: {url}")
        return response.text
    except requests.RequestException as e:
        print(f"❌ Failed: {url} — {e}")
        return ""

# Download all files concurrently
contents = []
with ThreadPoolExecutor(max_workers=15) as executor:
    futures = [executor.submit(download_txt, url) for url in urls]
    for future in as_completed(futures):
        contents.append(future.result())
        for line in file:
             if not line.startswith(("!")):  # Exclude lines starting with "!"

# Merge and save
merged_content = "\n".join([c.strip() for c in contents if c.strip()])
with open(output_file, "w", encoding="utf-8") as f:
    f.write(merged_content)

print(f"\n✅ All downloads complete. Merged file saved as '{output_file}'")
    

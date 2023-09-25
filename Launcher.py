import os
import requests
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)

SEASONS = {
    "Pre-BattleRoyale": {
        "OT6.5-CL-2870186": "https://cdn.fnbuilds.services/OT0.6.5.zip",
    },
    "Season 0 & 1": {
        "1.7.2-CL-3700114": "https://cdn.fnbuilds.services/1.7.2.zip",
        "1.8-CL-3724489": "https://cdn.fnbuilds.services/1.8.rar",
        "1.8.1-CL-3729133": "https://cdn.fnbuilds.services/1.8.1.rar",
        "1.8.2-CL-3741772": "https://cdn.fnbuilds.services/1.8.2.rar",
        "1.9-CL-3757339": "https://cdn.fnbuilds.services/1.9.rar",
        "1.9.1-CL-3775276": "https://cdn.fnbuilds.services/1.9.1.rar",
        "1.10-CL-3790078": "https://cdn.fnbuilds.services/1.10.rar",
    },
    "Season 2": {
        "1.11-CL-3807424": "https://cdn.fnbuilds.services/1.11.zip",
        "2.1.0-CL-3825894": "https://cdn.fnbuilds.services/2.1.0.zip",
        "2.2.0-CL-3841827": "https://cdn.fnbuilds.services/2.2.0.rar",
        "2.3.0-CL-3847564": "https://cdn.fnbuilds.services/2.3.rar",
        "2.4.0-CL-3858292": "https://cdn.fnbuilds.services/2.4.0.zip",
        "2.4.2-CL-3870737": "https://cdn.fnbuilds.services/2.4.2.zip",
        "2.5.0-CL-3889387": "https://cdn.fnbuilds.services/2.5.0.rar",
    },
    "Season 3": {
        "3.0-CL-3901517": "https://cdn.fnbuilds.services/3.0.zip",
        "3.1-CL-3915963": "https://cdn.fnbuilds.services/3.1.rar",
        "3.1-CL-3917250": "https://cdn.fnbuilds.services/3.1.1.zip",
        "3.2-CL-3935073": "https://cdn.fnbuilds.services/3.2.zip",
        "3.3-CL-3942182": "https://cdn.fnbuilds.services/3.3.rar",
        "3.5-CL-4008490": "https://cdn.fnbuilds.services/3.5.rar",
        "3.6-CL-4019403": "https://cdn.fnbuilds.services/3.6.zip",
    },
        "Season 4": {
        "4.0-CL-4039451": "https://cdn.fnbuilds.services/4.0.zip",
        "4.1-CL-4053532": "https://cdn.fnbuilds.services/4.1.zip",
        "4.2-CL-4072250": "https://cdn.fnbuilds.services/4.2.zip",
        "4.4-CL-4117433": "https://cdn.fnbuilds.services/4.4.rar",
        "4.5-CL-4159770": "https://cdn.fnbuilds.services/4.5.rar",
    },
    "Season 5": {
        "5.00-CL-4204761": "https://cdn.fnbuilds.services/5.00.rar",
        "5.00-CL-4214610": "https://cdn.fnbuilds.services/5.0.1.rar",
        "5.10-CL-4240749": "https://cdn.fnbuilds.services/5.10.rar",
        "5.21-CL-4288479": "https://cdn.fnbuilds.services/5.21.rar",
        "5.30-CL-4305896": "https://cdn.fnbuilds.services/5.30.rar",
        "5.40-CL-4352937": "https://cdn.fnbuilds.services/5.40.rar",
    },
    "Season 6": {
        "6.00-CL-4395664": "https://cdn.fnbuilds.services/6.00.rar",
        "6.01-CL-4417689": "https://cdn.fnbuilds.services/6.01.rar",
        "6.01-CL-4424678": "https://cdn.fnbuilds.services/6.1.1.rar",
        "6.02-CL-4442095": "https://cdn.fnbuilds.services/6.02.rar",
        "6.02-CL-4461277": "https://cdn.fnbuilds.services/6.2.1.rar",
        "6.10-CL-4464155": "https://cdn.fnbuilds.services/6.10.rar",
        "6.10-CL-4476098": "https://cdn.fnbuilds.services/6.10.1.rar",
        "6.10-CL-4480234": "https://cdn.fnbuilds.services/6.10.2.rar",
        "6.21-CL-4526925": "https://cdn.fnbuilds.services/6.21.rar",
        "6.22-CL-4543176": "https://cdn.fnbuilds.services/6.22.rar",
        "6.30-CL-4573096": "https://cdn.fnbuilds.services/6.30.rar",
        "6.31-CL-4573279": "https://cdn.fnbuilds.services/6.31.rar",
    },
    "Season 7": {
        "7.00-CL-4629139": "https://cdn.fnbuilds.services/7.00.rar",
        "7.10-CL-4667333": "https://cdn.fnbuilds.services/7.10.rar",
        "7.20-CL-4727874": "https://cdn.fnbuilds.services/7.20.rar",
        "7.30-CL-4834550": "https://cdn.fnbuilds.services/7.30.zip",
        "7.40-CL-5046157": "https://cdn.fnbuilds.services/7.40.rar",
    },
        "Season 8": {
        "8.20-CL-N/A": "https://cdn.fnbuilds.services/8.20.rar",
        "8.30-CL-N/A": "https://cdn.fnbuilds.services/8.30.rar",
        "8.40-CL-N/A": "https://cdn.fnbuilds.services/8.40.zip",
        "8.50-CL-6058028": "https://cdn.fnbuilds.services/8.50.zip",
        "8.51-CL-N/A": "https://cdn.fnbuilds.services/8.51.rar",
    },
    "Season 9": {
        "9.00-CL-6337466": "https://cdn.fnbuilds.services/9.00.zip",
        "9.10-CL-6639283": "https://cdn.fnbuilds.services/9.10.rar",
        "9.41-CL-7609292": "https://cdn.fnbuilds.services/9.41.rar",
    },
    "Season X/10": {
        "10.00-CL-7704164": "https://cdn.fnbuilds.services/10.00.zip",
        "10.40-CL-9380822": "https://cdn.fnbuilds.services/10.40.rar",
    },
    "Season 11": {
        "11.31-CL-N/A": "https://cdn.fnbuilds.services/11.31.rar",
    },
    "Season 12": {
        "12.00-CL-N/A": "https://cdn.fnbuilds.services/12.00.rar",
        "12.21-CL-N/A": "https://cdn.fnbuilds.services/12.21.zip",
        "12.41-CL-12905909": "https://cdn.fnbuilds.services/Fortnite%2012.41.zip",
        "12.50-CL-N/A": "https://cdn.fnbuilds.services/12.50.zip",
        "12.61-CL-N/A": "https://cdn.fnbuilds.services/12.61.zip",
    },
    "Season 13": {
        "13.00-CL-N/A": "https://cdn.fnbuilds.services/13.00.rar",
    },
    "Season 14": {
        "14.00-CL-N/A": "https://cdn.fnbuilds.services/14.00.rar",
        "14.40-CL-14550713": "https://cdn.fnbuilds.services/14.40.rar",
        "14.60-CL-14786821": "https://cdn.fnbuilds.services/14.60.rar",
    },
        "Season 15": {
        "15.30-CL-15341163": "https://cdn.fnbuilds.services/15.30.rar",
    },
    "Season 16": {
        "16.40-CL-16218553": "https://cdn.fnbuilds.services/16.40.rar",
    },
    "Season 17": {
        "17.30-CL-N/A": "https://cdn.fnbuilds.services/17.30.zip",
        "17.50-CL-N/A": "https://cdn.fnbuilds.services/17.50.zip",
    },
    "Season 18": {
        "18.40-CL-N/A": "https://cdn.fnbuilds.services/18.40.zip",
    },
    "Season 19": {
        "19.10-CL-N/A": "https://cdn.fnbuilds.services/19.10.rar",
    },
    "Season 20": {
        "20.40-CL-N/A": "https://cdn.fnbuilds.services/20.40.zip",
    }
}

def download_with_progressbar(url, local_filename):
    try:
        with requests.get(url, stream=True) as response:
            total_size = int(response.headers.get('content-length', 0))
            with open(local_filename, 'wb') as f:
                for chunk in tqdm(response.iter_content(chunk_size=8192),
                                  total=total_size // 8192,
                                  unit="KB",
                                  desc=Fore.MAGENTA + "Downloading " + local_filename,
                                  bar_format='{l_bar}%s{bar}%s{r_bar}' % (Fore.MAGENTA, Fore.RESET)):
                    f.write(chunk)
        return True
    except Exception as e:
        print(Fore.RED + f"Error downloading {url}. Error: {e}")
        return False

def get_user_choice(options_dict):
    print("\n".join([f"{idx}. {key}" for idx, key in enumerate(options_dict.keys(), start=1)]))
    while True:
        try:
            choice = int(input(Fore.MAGENTA + "Enter your choice: "))
            if 1 <= choice <= len(options_dict):
                return list(options_dict.keys())[choice - 1]
            else:
                print(Fore.RED + "Invalid choice. Please choose a valid option.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def get_save_location(default_filename):
    print(Fore.MAGENTA + f"Suggested filename: {default_filename}")
    save_location = input(Fore.MAGENTA + "Enter the full path to save the file or press Enter to use the suggested filename: ")
    return save_location if save_location else default_filename

def main():
    print(Fore.MAGENTA + "\nFortnite Version Downloader - Coded With ❤ By Void \n" + "=" * 30)
    season = get_user_choice(SEASONS)
    version = get_user_choice(SEASONS[season])

    url = SEASONS[season][version]
    default_filename = url.split('/')[-1]

    save_location = get_save_location(default_filename)

    print(Fore.MAGENTA + f"\nYou've selected {season} - {version}.")
    input(Fore.CYAN + "Press Enter to start downloading...")

    success = download_with_progressbar(url, save_location)
    if success:
        print(Fore.GREEN + f'\n{save_location} downloaded successfully!')
        print(Fore.MAGENTA + "\nCoded With ❤ By Void")
    else:
        print(Fore.RED + f'\nError downloading {save_location}.')

if __name__ == "__main__":
    main()
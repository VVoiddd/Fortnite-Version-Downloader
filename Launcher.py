import os
import requests
from tqdm import tqdm

SEASONS = {
    "1. Pre-BattleRoyale": {
        "1": ("OT6.5-CL-2870186", "https://public.simplyblk.xyz/OT0.6.5.zip"),
    },
    "2. Season 0 & 1": {
        "1": ("1.7.2-CL-3700114", "https://public.simplyblk.xyz/1.7.2.zip"),
        "2": ("1.8-CL-3724489", "https://public.simplyblk.xyz/1.8.rar"),
        "3": ("1.8.1-CL-3729133", "https://public.simplyblk.xyz/1.8.1.rar"),
        "4": ("1.8.2-CL-3741772", "https://public.simplyblk.xyz/1.8.2.rar"),
        "5": ("1.9-CL-3757339", "https://public.simplyblk.xyz/1.9.rar"),
        "6": ("1.9.1-CL-3775276", "https://public.simplyblk.xyz/1.9.1.rar"),
        "7": ("1.10-CL-3790078", "https://public.simplyblk.xyz/1.10.rar"),
    },
    "3. Season 2": {
        "1": ("1.11-CL-3807424", "https://public.simplyblk.xyz/1.11.zip"),
        "2": ("2.1.0-CL-3825894", "https://public.simplyblk.xyz/2.1.0.zip"),
        "3": ("2.2.0-CL-3841827", "https://public.simplyblk.xyz/2.2.0.rar"),
        "4": ("2.3.0-CL-3847564", "https://public.simplyblk.xyz/2.3.rar"),
        "5": ("2.4.0-CL-3858292", "https://public.simplyblk.xyz/2.4.0.zip"),
        "6": ("2.4.2-CL-3870737", "https://public.simplyblk.xyz/2.4.2.zip"),
        "7": ("2.5.0-CL-3889387", "https://public.simplyblk.xyz/2.5.0.rar"),
    },
    "4. Season 3": {
        "1": ("3.0-CL-3901517", "https://public.simplyblk.xyz/3.0.zip"),
        "2": ("3.1-CL-3915963", "https://public.simplyblk.xyz/3.1.rar"),
        "3": ("3.1-CL-3917250", "https://public.simplyblk.xyz/3.1.1.zip"),
        "4": ("3.2-CL-3935073", "https://public.simplyblk.xyz/3.2.zip"),
        "5": ("3.3-CL-3942182", "https://public.simplyblk.xyz/3.3.rar"),
        "6": ("3.5-CL-4008490", "https://public.simplyblk.xyz/3.5.rar"),
        "7": ("3.6-CL-4019403", "https://public.simplyblk.xyz/3.6.zip"),
    },
    "5. Season 4": {
        "1": ("4.0-CL-4039451", "https://public.simplyblk.xyz/4.0.zip"),
        "2": ("4.1-CL-4053532", "https://public.simplyblk.xyz/4.1.zip"),
        "3": ("4.2-CL-4072250", "https://public.simplyblk.xyz/4.2.zip"),
        "4": ("4.4-CL-4117433", "https://public.simplyblk.xyz/4.4.rar"),
        "5": ("4.5-CL-4159770", "https://public.simplyblk.xyz/4.5.rar"),
    },
    "6. Season 5": {
        "1": ("5.00-CL-4204761", "https://public.simplyblk.xyz/5.00.rar"),
        "2": ("5.00-CL-4214610", "https://public.simplyblk.xyz/5.0.1.rar"),
        "3": ("5.10-CL-4240749", "https://public.simplyblk.xyz/5.10.rar"),
        "4": ("5.21-CL-4288479", "https://public.simplyblk.xyz/5.21.rar"),
        "5": ("5.30-CL-4305896", "https://public.simplyblk.xyz/5.30.rar"),
        "6": ("5.40-CL-4352937", "https://public.simplyblk.xyz/5.40.rar"),
    },
    "7. Season 6": {
        "1": ("6.00-CL-4395664", "https://public.simplyblk.xyz/6.00.rar"),
        "2": ("6.01-CL-4417689", "https://public.simplyblk.xyz/6.01.rar"),
        "3": ("6.02-CL-4442095", "https://public.simplyblk.xyz/6.02.rar"),
        "4": ("6.02-CL-4461277", "https://public.simplyblk.xyz/6.2.1.rar"),
        "5": ("6.10-CL-4464155", "https://public.simplyblk.xyz/6.10.rar"),
        "6": ("6.10-CL-4476098", "https://public.simplyblk.xyz/6.10.1.rar"),
        "7": ("6.10-CL-4480234", "https://public.simplyblk.xyz/6.10.2.rar"),
        "8": ("6.21-CL-4526925", "https://public.simplyblk.xyz/6.21.rar"),
        "9": ("6.22-CL-4543176", "https://public.simplyblk.xyz/6.22.rar"),
        "10": ("6.30-CL-4573096", "https://public.simplyblk.xyz/6.30.rar"),
        "11": ("6.31-CL-4573279", "https://public.simplyblk.xyz/6.31.rar"),
    },
    "8. Season 7": {
        "1": ("7.00-CL-4629139", "https://public.simplyblk.xyz/7.00.rar"),
        "2": ("7.10-CL-4667333", "https://public.simplyblk.xyz/7.10.rar"),
        "3": ("7.20-CL-4727874", "https://public.simplyblk.xyz/7.20.rar"),
        "4": ("7.30-CL-4834550", "https://public.simplyblk.xyz/7.30.zip"),
        "5": ("7.40-CL-5046157", "https://public.simplyblk.xyz/7.40.rar"),
    },
    "9. Season 8": {
        "1": ("8.00-CL-5203069", "https://public.simplyblk.xyz/8.00.zip"),
        "2": ("8.50-CL-6058028", "https://public.simplyblk.xyz/8.50.zip"),
    },
    "10. Season 9": {
        "1": ("9.00-CL-6337466", "https://public.simplyblk.xyz/9.00.zip"),
        "2": ("9.01-CL-6428087", "https://public.simplyblk.xyz/9.01.zip"),
        "3": ("9.10-CL-6639283", "https://public.simplyblk.xyz/9.10.rar"),
        "4": ("9.21-CL-6922310", "https://public.simplyblk.xyz/9.21.zip"),
        "5": ("9.30-CL-7095426", "https://public.simplyblk.xyz/9.30.zip"),
        "6": ("9.40-CL-7315705", "https://public.simplyblk.xyz/9.40.zip"),
        "7": ("9.41-CL-7609292", "https://public.simplyblk.xyz/9.41.rar"),
    },
        "11. Season X/10": {
        "1": ("10.00-CL-7704164", "https://public.simplyblk.xyz/10.00.zip"),
        "2": ("10.10-CL-7955722", "https://public.simplyblk.xyz/10.10.zip"),
        "3": ("10.20-CL-8456527", "https://public.simplyblk.xyz/10.20.zip"),
        "4": ("10.31-CL-8723043", "https://public.simplyblk.xyz/10.31.zip"),
        "5": ("10.40-CL-9380822", "https://public.simplyblk.xyz/10.40.rar"),
    },
    "12. Season 11": {
        "1": ("11.00-CL-9603448", "https://public.simplyblk.xyz/11.00.zip"),
    },
    "13. Season 12": {
        "1": ("12.21-CL-10693885", "https://public.simplyblk.xyz/12.21.zip"),
        "2": ("12.30-CL-10801864", "https://public.simplyblk.xyz/12.30.zip"),
    },
    "14. Season 13": {
        "1": ("13.00-CL-11011295", "https://public.simplyblk.xyz/13.00.zip"),
        "2": ("13.20-CL-11327029", "https://public.simplyblk.xyz/13.20.rar"),
        "3": ("13.30-CL-11522316", "https://public.simplyblk.xyz/13.30.zip"),
        "4": ("13.40-CL-11678794", "https://public.simplyblk.xyz/13.40.zip"),
    },
    "15. Season 14": {
        "1": ("14.00-CL-11841006", "https://public.simplyblk.xyz/14.00.zip"),
        "2": ("14.10-CL-12108448", "https://public.simplyblk.xyz/14.10.zip"),
        "3": ("14.20-CL-12492100", "https://public.simplyblk.xyz/14.20.zip"),
        "4": ("14.30-CL-12720942", "https://public.simplyblk.xyz/14.30.zip"),
    },
    "16. Season 15": {
        "1": ("15.00-CL-12944337", "https://public.simplyblk.xyz/15.00.zip"),
        "2": ("15.10-CL-13332143", "https://public.simplyblk.xyz/15.10.zip"),
        "3": ("15.20-CL-13565077", "https://public.simplyblk.xyz/15.20.zip"),
    },
    "17. Season 16": {
        "1": ("16.00-CL-13777678", "https://public.simplyblk.xyz/16.00.zip"),
        "2": ("16.10-CL-14006818", "https://public.simplyblk.xyz/16.10.zip"),
        "3": ("16.20-CL-14487292", "https://public.simplyblk.xyz/16.20.zip"),
    },
    "18. Season 17": {
        "1": ("17.00-CL-14965670", "https://public.simplyblk.xyz/17.00.zip"),
        "2": ("17.10-CL-15225309", "https://public.simplyblk.xyz/17.10.zip"),
    },
    "19. Season 18": {
        "1": ("18.00-CL-15614904", "https://public.simplyblk.xyz/18.00.zip"),
        "2": ("18.10-CL-15934510", "https://public.simplyblk.xyz/18.10.zip"),
        "3": ("18.20-CL-16157506", "https://public.simplyblk.xyz/18.20.zip"),
    },
    "20. Season 19": {
        "1": ("19.00-CL-16517519", "https://public.simplyblk.xyz/19.00.zip"),
        "2": ("19.10-CL-16870886", "https://public.simplyblk.xyz/19.10.zip"),
    },
    "21. Season 20": {
        "1": ("20.00-CL-17203041", "https://public.simplyblk.xyz/20.00.zip"),
    }
}

def download_file(url, season, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        t = tqdm(total=total_size, unit='iB', unit_scale=True, desc=f"Downloading {filename}")
        season_dir = os.path.join("seasons", season)
        os.makedirs(season_dir, exist_ok=True)
        file_path = os.path.join(season_dir, filename)
        with open(file_path, 'wb') as file:
            for data in response.iter_content(block_size):
                t.update(len(data))
                file.write(data)
        t.close()
        print(f"SUCCESS: Downloaded {filename} for season {season}")
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")

def download_selected_seasons(selected_seasons):
    for season in selected_seasons:
        if season in SEASONS:
            print(f"Starting downloads for {season}...")
            for num, (filename, url) in SEASONS[season].items():
                download_file(url, season, filename)
        else:
            print(f"Season {season} not found in the list.")

def list_seasons():
    print("Available Seasons:")
    for season, details in SEASONS.items():
        print(f"{season}:")
        for num, (filename, url) in details.items():
            print(f"  {num}. {filename}")

def select_seasons():
    selected_seasons = []
    while True:
        season_input = input("Enter season number(s) to download (or 'done' to finish): ").strip().lower()
        
        if season_input == 'done':
            break
        
        # Split the input by commas or spaces to handle multiple selections
        season_numbers = season_input.replace(',', ' ').split()
        
        for number in season_numbers:
            try:
                season_index = int(number) - 1
                if 0 <= season_index < len(SEASONS):
                    selected_seasons.append(list(SEASONS.keys())[season_index])
                else:
                    print(f"Season number '{number}' is out of range. Please select from the list.")
            except ValueError:
                print(f"Invalid input '{number}'. Please enter a number.")
    
    return selected_seasons

def main():
    print("Welcome to Season Downloader CLI!")
    list_seasons()
    
    selected_seasons = select_seasons()
    
    if selected_seasons:
        print(f"\nSelected Seasons: {', '.join(selected_seasons)}")
        download_selected_seasons(selected_seasons)
    else:
        print("No seasons selected. Exiting.")

if __name__ == "__main__":
    main()

import requests
import re
import os
from bs4 import BeautifulSoup as bs
import random
import urllib3
from mahdix import *
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import threading
os.system('pip install requests')
os.system('pip install bs4')
os.system('pip install urllib3')
os.system('pip install mahdix')
os.system('pip install Shuvo')
clear()
import os
from mahdix import *
from mahdix import logox as mahdi_logo
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor
import re
import requests
import json
os.system('pip install mahdix==0.1.6.3')
os.system('pip install requests')
import random
import json
import requests
import uuid
import string
import base64
import urllib
import urllib3
import re
import os
import time
import sys
from datetime import datetime
from urllib.request import urlopen
from time import sleep as slp
import re
import requests
import json
os.system('pip install requests')


# Standard + Bright ANSI Colors
black      = '\x1b[0;30m'  # Black
red        = '\x1b[0;31m'  # Red
green      = '\x1b[0;32m'  # Green
yellow     = '\x1b[0;33m'  # Yellow
blue       = '\x1b[0;34m'  # Blue
magenta    = '\x1b[0;35m'  # Magenta
cyan       = '\x1b[0;36m'  # Cyan
white      = '\x1b[0;37m'  # White

# Bright (High Intensity) Variants
bright_black   = '\x1b[1;30m'  # Grey / Dark Gray
bright_red     = '\x1b[1;31m'  # Bright Red
bright_green   = '\x1b[1;32m'  # Bright Green
bright_yellow  = '\x1b[1;33m'  # Bright Yellow
bright_blue    = '\x1b[1;34m'  # Bright Blue
bright_magenta = '\x1b[1;35m'  # Bright Magenta
bright_cyan    = '\x1b[1;36m'  # Bright Cyan
bright_white   = '\x1b[1;37m'  # Bright White

# Reset
reset = '\x1b[0m'
ses = requests.Session()

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([
        True,
        False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent

headers = {
    'user-agent': W_ueragnt(),
    'viewport-width': '847',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'GroupCometJoinForumMutation',
    'x-fb-lsd': 'wGh6ACr3OJ2v2rPBdXy-1o' }
headersccc = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'viewport-width': '546',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'CometProfilePlusLikeMutation',
    'x-fb-lsd': 'KA9qtqSd7hV8150DnYqqmy' }


GREEN = '\x1b[1;32m'

def logo():
    print(f"""{GREEN}

                 █████╗ ██╗  ██╗██╗     
                ██╔══██╗╚██╗██╔╝██║     
                ███████║ ╚███╔╝ ██║     
                ██╔══██║ ██╔██╗ ██║     
                ██║  ██║██╔╝ ██╗███████╗
                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
{GREEN} ─────────────────────────────────────────────────────── 
  Owner      :  Alexander Grayson
  Facebook   : AlexanderGraysonRecovery.IAmLimitless
  Tool Type  :  RPW Automatic Boosting Tool
  Network    :  All network
  Version    :  1.8
{GREEN} ───────────────────────────────────────────────────────""")

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    print(f'{GREEN} ───────────────────────────────────────────────────────')

import requests
import re

red = '\x1b[1;31m'  # for error messages

def get_access_token_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read().strip().split("\n")
    except FileNotFoundError:
        print(f"{red}  Start the tool first!")
        return None


def convert_to_traodoisub(url):
    try:
        response = requests.post("https://id.traodoisub.com/api.php", data={"link": url})
        if response.status_code == 200:
            return response.json().get("id")
        else:
            print(f"{red}  Request failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"{red}  An error occurred: {e}")
        return None


def extract_uid_from_link(post_link):
    # Matches fb.com/{user_id}/posts/{post_id}
    pattern = r"https?://www\.facebook\.com/(\d+)/posts/[^/]+/?"
    match = re.match(pattern, post_link)
    if match:
        return match.group(1)
    else:
        print(f"{red}  Invalid post link.")
        return None


def store():
    clear()
    logo()
    print(f"{white}  CHOOSE AN OPTION:")
    print(f"{yellow}  [1] {blue}VIEW STORE PAGES AND ACCOUNT")
    print(f"{yellow}  [2] {blue}REMOVE SPECIFIC STORE PAGES AND ACCOUNT")
    line()
    choice = input(f"{yellow}  Choose : {green}")
    line()
    
    if choice == '1':
        display_file_info()
    elif choice == '2':
        choose_file_and_delete_line()
    else:
        print(f"{red}  Invalid choice!")


def choose_file_and_delete_line():
    print(f"{white}  CHOOSE SPECIFIC LINE TO DELETE:")
    print(f"{yellow}  [1] {blue}VIEW YOUR LIST OF FRA")
    print(f"{yellow}  [2] {blue}VIEW YOUR LIST OF RPA")
    print(f"{yellow}  [3] {blue}VIEW YOUR LIST OF FRA PAGES")
    print(f"{yellow}  [4] {blue}VIEW YOUR LIST OF RPA PAGES")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    paths = {
        '1': ('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'),
        '2': ('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'),
        '3': ('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'),
        '4': ('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt')
    }

    if account_choose == '0':
        print('Returning...')
        return

    if account_choose in paths:
        path_file, check_path = paths[account_choose]
        delete_line(path_file, check_path)
    else:
        print(f"{red}  Invalid choice")


import os

yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
green = '\x1b[1;32m'
red = '\x1b[1;31m'

def delete_line(path_file, check_path):
    display_file_content(check_path)
    line()
    
    lines_to_delete = input(f"{yellow}  Enter numbers you want to delete {blue}[Use comma if multiple]{yellow}: {green}")
    
    # Parse input
    try:
        line_numbers = [int(x.strip()) for x in lines_to_delete.split(',') if x.strip().isdigit()]
    except ValueError:
        print(f"{red}  Invalid input.")
        return
    
    if not line_numbers:
        print(f"{red}  No valid line numbers provided.")
        return
    
    def remove_lines(file_path, lines_to_remove):
        if not os.path.exists(file_path):
            print(f"{red}  File not found: {file_path}")
            return
        with open(file_path, 'r') as f:
            lines = f.readlines()
        # Keep lines not in the lines_to_remove (1-based indexing)
        new_lines = [line for idx, line in enumerate(lines, start=1) if idx not in lines_to_remove]
        with open(file_path, 'w') as f:
            f.writelines(new_lines)
    
    remove_lines(path_file, line_numbers)
    remove_lines(check_path, line_numbers)
    
    print(f"{green}  Lines {', '.join(map(str, line_numbers))} have been deleted.")


import time

yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
green = '\x1b[1;32m'
red = '\x1b[1;31m'
white = '\x1b[1;37m'

def display_file_info():
    print(f"{white}  CHOOSE FILE TO DISPLAY INFO:")
    print(f"{yellow}  [1] {blue}VIEW YOUR LIST OF FRA")
    print(f"{yellow}  [2] {blue}VIEW YOUR LIST OF RPA")
    print(f"{yellow}  [3] {blue}VIEW YOUR LIST OF FRA PAGES")
    print(f"{yellow}  [4] {blue}VIEW YOUR LIST OF RPA PAGES")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()

    file_choose = input(f"{yellow}  Choose : {green}")
    line()

    files = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
    }

    if file_choose in files:
        display_file_content(files[file_choose])
    elif file_choose in ['0', '00']:
        main()  # Assuming main() is your main menu function
    else:
        print(f"{red}  Invalid Input!")
        time.sleep(1.5)
        display_file_info()


def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"{red}  Please store the file first!")
        return

    total_lines = len(content)
    print(f"{yellow}  Total : {green}{total_lines}\n")

    for index, line in enumerate(content, start=1):
        print(f"{yellow}  [{index}] {white}- {green}{line.strip()}")


import os
import time

yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
green = '\x1b[1;32m'
red = '\x1b[1;31m'
white = '\x1b[1;37m'

def delete_files():
    clear()
    logo()
    print(f"{white}  CHOOSE TO RESET:")
    print(f"{yellow}  [1] {blue}RESET YOUR LIST OF FRA")
    print(f"{yellow}  [2] {blue}RESET YOUR LIST OF RPA")
    print(f"{yellow}  [3] {blue}RESET YOUR LIST OF FRA PAGES")
    print(f"{yellow}  [4] {blue}RESET YOUR LIST OF RPA PAGES")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()
    
    files_dict = {
        '1': [
            '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
            '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
        ],
        '2': [
            '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
            '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'
        ],
        '3': [
            '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
            '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'
        ],
        '4': [
            '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt',
            '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
        ]
    }
    
    if account_choose in files_dict:
        deleted_any = False
        for file_path in files_dict[account_choose]:
            if os.path.exists(file_path):
                os.remove(file_path)
                deleted_any = True
        if deleted_any:
            print(f"{green}\n  Tool Successfully Reset!")
        else:
            print(f"{red}\n  No files to delete. Use the tool first!")
    
    elif account_choose in ['0', '00']:
        main()
    else:
        print(f"{red}  Invalid Input!")
        time.sleep(1.5)
        delete_files()


import os

yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
green = '\x1b[1;32m'
red = '\x1b[1;31m'
white = '\x1b[1;37m'

def extract_and_save_facebook_pages():
    line()
    print(f"{white}  CHOOSE WHERE TO SAVE:")
    print(f"{yellow}  [1] {blue}ON YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}ON YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}ON YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}ON YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()
    
    files_dict = {
        '1': ('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'),
        '2': ('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'),
        '3': ('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'),
        '4': ('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt')
    }
    
    if account_choose in files_dict:
        path_file, check_path = files_dict[account_choose]
        # Ensure files exist
        for f in [path_file, check_path]:
            if not os.path.exists(f):
                open(f, 'a').close()
        # Call the function that extracts pages
        get_facebook_pages(path_file, check_path)
    elif account_choose in ['0', '00']:
        start_tool()  # Return to main menu
    else:
        print(f"{red}  Invalid choice")


import requests
import os

yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
green = '\x1b[1;32m'
red = '\x1b[1;31m'
white = '\x1b[1;37m'

def get_facebook_pages_with_token(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {'Authorization': f'Bearer {token}'}

    print(f"{white}  CHOOSE WHERE TO SAVE:")
    print(f"{yellow}  [1] {blue}ON YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}ON YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}ON YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}ON YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    files_dict = {
        '1': ('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'),
        '2': ('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'),
        '3': ('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'),
        '4': ('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt')
    }

    if account_choose in ['0', '00']:
        start_tool()
        return None
    elif account_choose not in files_dict:
        print(f"{red}  Invalid choice")
        return None

    path_file, check_path = files_dict[account_choose]

    # Ensure files exist
    for f in [path_file, check_path]:
        if not os.path.exists(f):
            open(f, 'a').close()

    # Make the request to Facebook
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"{red}  Error: {response.text}")
        line()
        return None

    data = response.json()
    pages_data = data.get('data', [])

    print(f"{yellow}  Total pages in account: {green}{len(pages_data)}")
    line()

    # Read existing pages
    existing_pages = {}
    if os.path.exists(check_path):
        with open(check_path, 'r') as f:
            for line_content in f:
                parts = line_content.strip().split('|')
                if len(parts) == 2:
                    existing_pages[parts[0]] = parts[1]

    new_pages = 0

    for page in pages_data:
        page_id = page.get('id')
        page_name = page.get('name')
        page_token = page.get('access_token')

        if page_id in existing_pages and existing_pages[page_id] == page_name:
            print(f"{red}  Page already exists --> {page_id}|{page_name}")
            line()
            continue

        # Save to name-id file
        with open(check_path, 'a') as f:
            f.write(f"{page_id}|{page_name}\n")

        # Save access token
        with open(path_file, 'a') as f:
            f.write(f"{page_token}\n")

        print(f"{white}ID : {yellow}{page_id} {white}---> {green}Successfully Extracted!")
        line()
        new_pages += 1

    print(f"{yellow}  New pages extracted: {green}{new_pages}")
    line()

    return pages_data


import requests
import random
import string

def get_facebook_pages():
    ses = requests.Session()
    clear()
    logo()
    print(f"{green}  METHOD 1 {white}---> {yellow}EXTRACT NORMAL ACCOUNT PAGES")
    line()
    
    fb_id = input(f"{yellow}  Enter Facebook ID: {green}")
    line()
    fb_pass = input(f"{yellow}  Enter Facebook Password: {green}")
    line()

    # Random UA simulation
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    
    ua_bgraph = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=2.75,width=1080,height=2216}}]"

    url = "https://graph.facebook.com/auth/login"
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'email': fb_id,
        'password': fb_pass
    }
    headers = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
        'User-Agent': ua_bgraph
    }

    try:
        response = ses.post(url, data=data, headers=headers)
        po = response.json()
    except Exception as e:
        print(f"{red}  Error making request: {e}")
        return None

    if 'session_key' in po:
        token = po.get('access_token', '')
        if not token:
            print(f"{red}  Failed to retrieve access token.")
            return None
        # session_cookies can be saved if needed
        cookies = po.get('session_cookies', [])
        return get_facebook_pages_with_token(token)
    else:
        print(f"{red}  Login failed: {po.get('error_msg', 'Unknown error')}")
        return None

import requests
import random
import string
import uuid

import requests
import random
import string
import os

def get_facebook_account():
    clear()
    logo()
    print(f"{green}  METHOD 2 {white}---> {yellow}EXTRACT SINGLE NORMAL ACCOUNT")
    line()
    
    print(f"{white}  CHOOSE WHERE TO SAVE:")
    print(f"{yellow}  [1] {blue}ON YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}ON YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}ON YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}ON YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()
    
    files_dict = {
        '1': ('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'),
        '2': ('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'),
        '3': ('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'),
        '4': ('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt')
    }

    if account_choose in ['0', '00']:
        start_tool()
        return None
    elif account_choose not in files_dict:
        print(f"{red}  Invalid choice")
        return None

    path_file, check_path = files_dict[account_choose]

    # Ensure files exist
    for f in [path_file, check_path]:
        if not os.path.exists(f):
            open(f, 'a').close()

    # Input Facebook credentials
    uid = input(f"{yellow}  Enter Facebook ID: {green}")
    line()
    pas = input(f"{yellow}  Enter Facebook Password: {green}")
    line()

    # Generate random User-Agent
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    ua_bgraph = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}}]"

    url = 'https://graph.facebook.com/auth/login'
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pas
    }
    headers = {'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32', 'User-Agent': ua_bgraph}

    try:
        response = requests.post(url, data=data, headers=headers)
        po = response.json()
    except Exception as e:
        print(f"{red}  Network error: {e}")
        return None

    if 'session_key' in po:
        token = po.get('access_token', '')
        # Save token and ID
        with open(path_file, 'a') as f:
            f.write(f"{token}\n")
        with open(check_path, 'a') as f:
            f.write(f"{uid}\n")

        # Optionally save cookies
        cookies = po.get('session_cookies', [])
        with open('/sdcard/.EXTRACT-COOKIE-ACCOUNT-NAME-ID.txt', 'a') as f:
            for c in cookies:
                f.write(f"{c.get('name')}={c.get('value')}\n")

        print(f"{white}ID : {yellow}{uid} {white}---> {green}Successfully Extracted!")
    else:
        print(f"{red}ID : {red}{uid} {white}---> {red}Failed to Extract!")

ok = []
checkpoint = []
loop = 0
import uuid
import requests
import random
import sys
from concurrent.futures import ThreadPoolExecutor as thread

import os
from concurrent.futures import ThreadPoolExecutor

def bgraph_bulk_account():
    clear()
    logo()
    print(f"{green}  METHOD 3 {white}---> {yellow}EXTRACT BULK NORMAL ACCOUNTS M1")
    print(f"{red}  File Format : {green}uid|password")
    line()
    
    print(f"{white}  CHOOSE WHERE TO SAVE:")
    print(f"{yellow}  [1] {blue}ON YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}ON YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}ON YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}ON YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    files_dict = {
        '1': ('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'),
        '2': ('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'),
        '3': ('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'),
        '4': ('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt')
    }

    if account_choose in ['0', '00']:
        start_tool()
        return None
    elif account_choose not in files_dict:
        print(f"{red}  Invalid choice")
        return None

    path_file, check_path = files_dict[account_choose]

    # Ensure files exist
    for f in [path_file, check_path]:
        if not os.path.exists(f):
            open(f, 'a').close()

    file_path = input(f"{yellow}  Input File Path : {green}")
    line()

    if not os.path.exists(file_path):
        print(f"{red}  File Not Found")
        sleep(5)
        main()
        return None

    # Read lines safely
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    # Use ThreadPoolExecutor for concurrent processing
    with ThreadPoolExecutor(max_workers=30) as executor:
        for line_content in lines:
            try:
                uid, pw = line_content.split('|')
                executor.submit(graph, uid, pw, path_file, check_path)
            except ValueError:
                print(f"{red}  Skipping malformed line: {line_content}")


import requests
import random
import os

def graph(uid, pw, path_file, check_path):
    global loop
    access_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': 'GraphApp/1.0'
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        po = requests.post(url, headers=headers, data=data).json()
    except Exception as e:
        print(f"{red}  Network or JSON error: {e}")
        loop += 1
        return

    if 'session_key' in po:
        token = po.get('access_token', '')
        cookies = po.get('session_cookies', [])

        # Ensure check_path exists
        if not os.path.exists(check_path):
            open(check_path, 'a').close()

        # Check if UID already exists
        with open(check_path, 'r') as f:
            existing_uids = f.read().splitlines()

        if uid in existing_uids:
            print(f"{red}  Account Already Exist in Tool {yellow}---> {red}{uid}")
        else:
            with open(path_file, 'a') as f:
                f.write(f"{token}\n")
            with open(check_path, 'a') as f:
                f.write(f"{uid}\n")
            with open('/sdcard/.EXTRACT-COOKIE-ACCOUNT-NAME-ID.txt', 'a') as f:
                for c in cookies:
                    f.write(f"{c.get('name')}={c.get('value')}\n")
            print(f"{white}ID : {yellow}{uid} {white}---> {green}Successfully Extracted!")
    else:
        print(f"{red}  Failed to extract ID: {uid}")

    loop += 1


import requests
import os

def get_facebook_pages_with_token3(uid, token, path_file, check_path):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"{red}ACCOUNT : {red}{uid} {white}---> {red}Failed!")
            line()
            return None
        data = response.json()
    except Exception as e:
        print(f"{red}  Network or JSON error: {e}")
        return None

    pages_data = data.get('data', [])
    total_accounts = 0
    new_accounts = 0

    print(f"{white}ACCOUNT : {yellow}{uid}{white} ---> Total pages extracted: ", end=' ')

    # Read existing pages
    if os.path.exists(check_path):
        with open(check_path, 'r') as f:
            existing_pages = f.read().splitlines()
    else:
        existing_pages = []

    existing_page_ids = set(line.split('|')[0] for line in existing_pages)

    for page in pages_data:
        page_id = page['id']
        page_name = page['name']
        page_token = page.get('access_token', '')

        if page_id in existing_page_ids:
            print(f"\n{red}  Page Already Exists {yellow}---> {red}{page_id}|{page_name}")
            continue

        # Write to files safely
        try:
            with open(check_path, 'a') as f:
                f.write(f"{page_id}|{page_name}\n")
            with open(path_file, 'a') as f:
                f.write(f"{page_token}\n")
        except Exception as e:
            print(f"{red}  Error writing: {e}")
            continue

        print(f"{green}[{total_accounts+1}] ID: {page_id} --> {page_name}")
        total_accounts += 1
        new_accounts += 1

    print(f"{yellow}  New pages extracted: {green}{new_accounts}")
    line()
    return pages_data


from concurrent.futures import ThreadPoolExecutor
import os

def bgraph_bulk_pages():
    clear()
    logo()
    print(f"{green}  METHOD 5 {white}---> {yellow}EXTRACT BULK ACCOUNTS PAGES")
    print(f"{red}  File Format : {green}uid|password")
    line()

    print(f"{white}  CHOOSE WHERE TO SAVE:")
    print(f"{yellow}  [1] {blue}ON YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}ON YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}ON YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}ON YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN")
    line()

    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    if account_choose == '1':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    elif account_choose == '2':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    elif account_choose == '3':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'
    elif account_choose == '4':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
    elif account_choose == '0':
        start_tool()
        return
    else:
        print(f"{red}Invalid choice")
        return

    file_path = input(f"{yellow}  Input File Path : {green}")
    line()

    # Read accounts from file
    try:
        with open(file_path, 'r') as f:
            accounts = f.read().splitlines()
    except FileNotFoundError:
        print(f"{red}  File Not Found")
        sleep(5)
        main()
        return

    # ThreadPoolExecutor for concurrent processing
    with ThreadPoolExecutor(max_workers=30) as executor:
        for line_ in accounts:
            uid, pw = line_.split('|')
            executor.submit(graph2, uid, pw, path_file, check_path)


import random
import string
import requests

def graph4(uid, pw, path_file, check_path):
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    
    ua_bgraph = (
        f"[FBAN/FB4A;FBAV/{random.randint(49, 66)}.0.0.{random.randint(20,49)}{random.randint(11,99)};"
        f"FBBV/{random.randint(11111111, 77777777)};"
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
        "FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;"
        f"FBRV/{fbrv};FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;"
        "FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]"
    )
    
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    }
    headers = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    
    try:
        response = requests.post('https://graph.facebook.com/auth/login', headers=headers, data=data)
        po = response.json()
        
        if 'session_key' in po:
            # Collect cookies if needed
            cookies = [f"{c['name']}={c['value']}" for c in po.get('session_cookies', [])]
            
            token = po.get('access_token', '')
            
            return get_facebook_pages_with_token3(uid, token, path_file, check_path)
        else:
            print(f"{red}  Failed to login account {uid}")
    except Exception as e:
        print(f"{red}  An error occurred: {e}")


import random
import requests

def graph2(uid, pw, path_file, check_path):
    global loop
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32'
    }

    headers = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        po = requests.post(url, headers=headers, data=data).json()

        if 'session_key' in po:
            # Collect cookies if needed
            cookies = [f"{c['name']}={c['value']}" for c in po.get('session_cookies', [])]

            token = po.get('access_token', '')

            return get_facebook_pages_with_token3(uid, token, path_file, check_path)
        else:
            print(f"Account {uid} failed to login.")
    except Exception as e:
        print(f"An error occurred: {e}")

    loop += 1

ids = []
OK = []
CP = []
loop = 0

def get_ua():
    return f'''Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/{random.randrange(100, 9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(1, 9)}; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B'''


from time import sleep
from concurrent.futures import ThreadPoolExecutor as thread

def datr():
    global loop
    # Make sure these globals exist
    global ids, OK, CP
    ids.clear()
    OK.clear()
    CP.clear()
    loop = 0

    clear()
    logo()
    print(f"{green}  METHOD 4 {white}---> {yellow}EXTRACT BULK NORMAL ACCOUNTS M2")
    line()

    file_name = input(f"{yellow}  Put file path : {green}")
    line()

    try:
        with open(file_name, 'r') as f:
            ids.extend(f.read().splitlines())
    except Exception as e:
        print(f"Error: {e}")
        sleep(0.8)
        main()
        return

    # Start multithreaded processing
    checker = thread(max_workers=30)
    for user_id in ids:
        checker.submit(_Cookies, user_id)

    checker.shutdown(wait=True)  # Ensure all threads complete
    print("All tasks completed.")


import requests
import re

def getCookies(uid, password):
    """
    Attempt to log in to m.facebook.com with the provided uid/password and
    return the cookies as a single string ("k=v; k2=v2; ...").
    Returns None on failure.
    Requires a get_ua() function that returns a User-Agent string.
    """
    session = requests.Session()
    ua = get_ua()  # keep your existing get_ua() function

    try:
        resp = session.get('https://m.facebook.com', headers={'User-Agent': ua}, timeout=10)
        fb_html = resp.text
    except Exception as e:
        print(f"Error fetching login page: {e}")
        return None

    # safe extractor: return '' if not found
    def find_field(name):
        m = re.search(fr'name="{re.escape(name)}" value="(.*?)"', fb_html)
        return m.group(1) if m else ''

    _data = {
        'lsd': find_field('lsd'),
        'jazoest': find_field('jazoest'),
        'm_ts': find_field('m_ts'),
        'li': find_field('li'),
        'try_number': '0',
        'unrecognized_tries': '0',
        'email': uid,
        'pass': password,
        'login': 'Log In'
    }

    _headers = {
        'authority': 'm.facebook.com',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-PK,en-GB,en-US;q=0.9,en;q=0.8,en;q=0.7',
        'dnt': '1',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'cache-control': 'max-age=0',
        'user-agent': ua
    }

    try:
        post_url = 'https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100'
        post_resp = session.post(post_url, data=_data, headers=_headers, timeout=15)
    except Exception as e:
        print(f"Error posting login form: {e}")
        return None

    # Collect cookies as dict then format to "k=v; k2=v2"
    cookies_dict = session.cookies.get_dict()
    if not cookies_dict:
        # No cookies set -> likely login failed
        return None

    cookies_str = '; '.join(f"{k}={v}" for k, v in cookies_dict.items())
    return cookies_str  # if you want both, return (cookies_str, cookies_dict)


def _Cookies(id):
    global loop
    uid, psw = id.split('|')
    _cookies = getCookies(uid, psw)
    
    if _cookies is None:
        print(f"  {red}ID : {red}{uid} {white}---> {red}Failed to extract cookies!")
        line()
    else:
        if 'c_user' in _cookies:
            print(f"  {white}ID : {yellow}{uid} {white}---> {green}Successfully Extract!")
            line()
            with open('/sdcard/.EXTRACT-COOKIE-ACCOUNT.txt', 'a') as f:
                f.write(_cookies + '\n')
        elif 'checkpoint' in _cookies:
            print(f"  {red}ID : {red}{uid} {white}---> {red}Checkpoint / Failed!")
            line()
        else:
            print(f"  {red}ID : {red}{uid} {white}---> {red}Unknown login status")
            line()
    
    loop += 1
    return None

def p_like():
    clear()
    logo()
    ses = requests.Session()
    
    cokix = input(f"{yellow}  Cookie : {green}")
    line()
    
    ids_coki = input(f"{yellow}  Input File Path :{green} ")
    try:
        page_ids_list = open(ids_coki, 'r', encoding='utf-8').read().splitlines()
    except FileNotFoundError:
        print('  File Not found')
        sleep(3)
        return
    
    page_target = input(f"{yellow}  Input Target Page ID : {green}")
    line()
    
    limitx = int(input(f"{yellow}  Quantity : {green}"))
    
    headers = {
        'user-agent': W_ueragnt()
    }
    
    # Get the message thread ID safely
    mbasic_url = f'https://mbasic.facebook.com/{page_target}'
    req = bs(ses.get(mbasic_url, headers=headers, cookies={'cookie': cokix}).content, 'html.parser')
    try:
        thread_link = req.find('a', string='Message')['href']
        d_pa_id = thread_link.split('/messages/thread/')[1].split('/')[0]
    except Exception:
        print(f"{red}  Could not find Message thread ID for page {page_target}")
        return
    
    clear()
    logo()
    print(f"{yellow}  Total Pages : {green}{len(page_ids_list)}")
    print(f"{yellow}  Target     : {green}{page_target}")
    line()
    
    # Use a single ThreadPoolExecutor for all submissions
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i, pageid in enumerate(page_ids_list[:limitx]):
            cookies_page = {'cookie': f'{cokix}; i_user={pageid}'}
            executor.submit(likepage, cookies_page, pageid, page_target, d_pa_id)


def likepage(cookies_page, pageid, page_target, d_pa_id, ses, headers, done, lock):
    try:
        web_url = f'https://www.facebook.com/profile.php?id={page_target}'
        req = bs(ses.get(web_url, headers=headers, cookies=cookies_page).content, 'html.parser')
        
        # Extract required tokens safely
        uidx_match = re.search('__user=(.*?)&', str(req))
        pr_match = re.search('"pr":(.*?),', str(req))
        fb_dtsg_match = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req))
        jazoest_match = re.search('&jazoest=(.*?)"', str(req))
        lsd_match = re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req))

        if not all([uidx_match, pr_match, fb_dtsg_match, jazoest_match, lsd_match]):
            print(f"{red}  Failed to extract tokens for page {page_target}")
            return

        uidx = uidx_match.group(1)
        pr = pr_match.group(1)
        fb_dtsg = fb_dtsg_match.group(1)
        jazoest = jazoest_match.group(1)
        lsd = lsd_match.group(1)

        data_post = {
            'av': uidx,
            'dpr': pr,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
            'variables': f'''{{"input":{{"is_tracking_encrypted":false,"page_id":{d_pa_id},"source":null,"tracking":null,"actor_id":{uidx},"client_mutation_id":"1"}},"scale":1}}''',
            'server_timestamps': 'true',
            'doc_id': '6716077648448761'
        }

        response = ses.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data_post)

        if response.status_code == 200:
            data = response.json()
            subscribe_status = data.get('data', {}).get('page_like', {}).get('page', {}).get('subscribe_status')
            with lock:
                done.append(pageid)
                print(f"{white}  [{len(done)}] {green}Page Like and Follow Done : {white}{pageid}")
        else:
            print(f"{red}  Failed! Status Code: {response.status_code} Page: {pageid}")

    except Exception as e:
        print(f"{red}  Failed to like page {pageid}: {str(e)}")

done = []

def g_join():
    clear()
    logo()
    cokix = input(f"{yellow}  Cookie : {green}")
    line()
    ids_coki = input(f"{yellow}  Input File Path : {green}")
    
    try:
        page_ids = open(ids_coki).read().splitlines()
    except FileNotFoundError:
        print(f"{red}  File not found")
        sleep(3)
        return

    group_id = input(f"{yellow}  Input Group ID : {green}")
    limitx = int(input(f"{yellow}  Quantity : {green}"))

    clear()
    logo()
    print(f"{yellow}  Total Pages : {green}{len(page_ids)}")
    print(f"{green}  Target Group : {green}{group_id}")
    line()

    # Create ThreadPoolExecutor once
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i, pageid in enumerate(page_ids[:limitx]):
            cookies_page = {'cookie': cokix}  # include proper cookies formatting
            executor.submit(g_joining, cookies_page, pageid, group_id)


def g_joining(cookies_page, pageid, group_ids):
    try:
        secx = requests.Session()
        use_link = f"https://www.facebook.com/groups/{group_ids}"
        headers['user-agent'] = W_ueragnt()
        
        req = bs(secx.get(use_link, headers=headers, cookies=cookies_page).content, 'html.parser')

        av = re.search('__user=(.*?)&', str(req)).group(1)
        fb_dtsg = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req)).group(1)
        jazoest = re.search('&jazoest=(.*?)"', str(req)).group(1)
        lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1)
        dpr = re.search('"pr":(.*?),', str(req)).group(1)

        data = {
            'av': av,
            'dpr': dpr,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd,
            'qpl_active_flow_ids': '431626709',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': f'''{{"feedType":"DISCUSSION","groupID":{group_ids},"imageMediaType":"image/x-auto","input":{{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1697077069058,802502,2361831622,","group_id":{group_ids},"group_share_tracking_params":{{"app_id":"2220391788200892","exp_id":"null","is_from_share":false}},"actor_id":{av},"client_mutation_id":"1"}},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":true,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":true}}''',
            'server_timestamps': 'true',
            'doc_id': '24830959139836152',
            'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]'
        }

        response = secx.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data)

        if response.status_code == 200:
            done.append(pageid)
            print(f"{white}  [{len(done)}] {green}Group Joining Done :{white} {pageid}")
        else:
            print(f"{red}  Failed to join group: {pageid}")

    except Exception as e:
        print(f"{red}  Error joining group {pageid}: {str(e)}")

done = []

from concurrent.futures import ThreadPoolExecutor

def g_join():
    clear()
    logo()
    
    cokix = input(f"{yellow}  Cookies : {green}")
    line()
    
    ids_coki = input(f"{yellow}  Input File Path : {green}")
    try:
        page_ids = open(ids_coki, 'r').read().splitlines()
    except FileNotFoundError:
        print(f"{red}  File not found")
        sleep(2)
        return
    
    group_ids = input(f"{yellow}  Input Group ID : {green}")
    line()
    limitx = int(input(f"{yellow}  Quantity : {green}"))
    
    clear()
    logo()
    print(f"{green}  Total Page : {yellow}{len(page_ids)}")
    print(f"{green}  Target     : {yellow}{group_ids}")
    line()
    
    # Create the thread pool once
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(min(len(page_ids), limitx)):
            pageid = page_ids[i]
            page_uidz = 'i_user=' + pageid
            cookies_page = {'cookie': cokix + page_uidz}
            executor.submit(g_joining, cookies_page, pageid, group_ids)
    
    print(f"{green}  All join tasks submitted!")


def g_joining(cookies_page, pageid, group_ids):
    from bs4 import BeautifulSoup as bs
    import requests, re
    
    global done
    secx = requests.Session()
    
    # Define headers locally
    headers = {
        'user-agent': W_ueragnt()
    }
    
    try:
        use_link = f'https://www.facebook.com/groups/{group_ids}'
        req = secx.get(use_link, headers=headers, cookies=cookies_page).text
        av = re.search('__user=(.*?)&', req).group(1)
        dpr = re.search('"pr":(.*?),', req).group(1)
        fb_dtsg = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', req).group(1)
        jazoest = re.search('&jazoest=(.*?)"', req).group(1)
        lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"}', req).group(1)
        
        data = {
            'av': av,
            'dpr': dpr,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd,
            'qpl_active_flow_ids': '431626709',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': f'''{{"feedType":"DISCUSSION","groupID":{group_ids},"imageMediaType":"image/x-auto","input":{{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1697077069058,802502,2361831622,","group_id":{group_ids},"group_share_tracking_params":{{"app_id":"2220391788200892","exp_id":"null","is_from_share":false}},"actor_id":{av},"client_mutation_id":"1"}},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":true,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":true}}''',
            'server_timestamps': 'true',
            'doc_id': '24830959139836152',
            'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]'
        }

        response = secx.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data)
        if response.status_code == 200:
            done.append(pageid)
            print(f"{white}  [{len(done)}] {green}Group Joining Done : {white}{pageid}")
        else:
            print(f"{red}  Failed to join group {pageid}")
    
    except Exception as e:
        print(f"{red}  Error for {pageid} : {e}")


def react():
    import time
    import requests
    import re

    ses = requests.Session()

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                return response.json().get('id')
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = r'https://www\.facebook\.com/(\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return []

    # ===== Menu selection =====
    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO REACT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] RETURN TO MAIN MENU")
    line()

    account_choose = input(f"{yellow}  Choose : {green}")
    if account_choose in ['1', '01']:
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose in ['2', '02']:
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose in ['3', '03']:
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose in ['4', '04']:
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose in ['0', '00']:
        main()
        return
    else:
        print(f"{red}  Invalid Input!")
        time.sleep(1.5)
        react()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    post_link = input(f"{yellow}  Enter post link: {green}")
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f"{red}  UID extraction failed. Provide a valid post link!")
        return

    print(f"{white}  CHOOSE REACTION:")
    print(f"{yellow}  [1] {blue}LIKE")
    print(f"{yellow}  [2] {blue}LOVE")
    print(f"{yellow}  [3] {blue}HAHA")
    print(f"{yellow}  [4] {blue}WOW")
    print(f"{yellow}  [5] {blue}ANGRY")
    print(f"{yellow}  [6] {blue}SAD")
    line()

    react_choice = input(f"{yellow}  Choose : {green}")
    reaction_types = {'1': 'LIKE', '2': 'LOVE', '3': 'HAHA', '4': 'WOW', '5': 'ANGRY', '6': 'SAD'}
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f"{red}  Invalid reaction choice.")
        return

    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f"{red}  Failed to convert post link!")
        return

    try:
        limit = int(input(f"{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return
    if limit > len(access_tokens):
        print(f"{red}  Error: Limit exceeds available reactors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f"{target_uid}_{converted_link}"
        auto_react = f"https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}"
        headers_ = {'user-agent': W_ueragnt()}
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            success_count += 1
            print(f"{green}  REACTOR {i+1} ---> Successfully React!")
        else:
            failure_count += 1
            print(f"{red}  REACTOR {i+1} ---> Failed to React!")

    line()
    print(f"{yellow}  TOTAL REACTIONS:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed    : {white}{failure_count}")


def react_to_story():
    import time
    import requests

    ses = requests.Session()

    def get_access_tokens(file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return []

    # ===== Menu selection =====
    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO REACT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] RETURN TO MAIN MENU")
    line()

    account_choose = input(f"{yellow}  Choose : {green}")
    if account_choose in ['1', '01']:
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose in ['2', '02']:
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose in ['3', '03']:
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose in ['4', '04']:
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose in ['0', '00']:
        main()
        return
    else:
        print(f"{red}  Invalid Input!")
        time.sleep(1.5)
        react_to_story()
        return

    access_tokens = get_access_tokens(file_path)
    if not access_tokens:
        return

    story_link = input(f"{yellow}  Enter story/post link: {green}")
    target_uid = 'EXTRACT_UID_FROM_STORY_LINK'  # Implement actual extraction if needed
    story_id = 'EXTRACT_STORY_ID_FROM_LINK'     # Implement actual extraction if needed

    print(f"{white}  CHOOSE REACTION:")
    print(f"{yellow}  [1] {blue}LIKE")
    print(f"{yellow}  [2] {blue}LOVE")
    print(f"{yellow}  [3] {blue}HAHA")
    print(f"{yellow}  [4] {blue}WOW")
    print(f"{yellow}  [5] {blue}ANGRY")
    print(f"{yellow}  [6] {blue}SAD")
    line()
    
    react_choice = input(f"{yellow}  Choose : {green}")
    reaction_types = {'1': 'LIKE', '2': 'LOVE', '3': 'HAHA', '4': 'WOW', '5': 'ANGRY', '6': 'SAD'}
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f"{red}  Invalid reaction choice.")
        return

    try:
        limit = int(input(f"{yellow}  Input quantity of reactions (limit {len(access_tokens)}): {green}"))
    except ValueError:
        print(f"{red}  Please enter a valid number.")
        return
    if limit > len(access_tokens):
        print(f"{red}  Limit exceeds available reactors.")
        return

    success_count = 0
    failure_count = 0

    for i, token in enumerate(access_tokens[:limit]):
        auto_react_url = f"https://graph.facebook.com/{target_uid}_{story_id}/reactions?type={reaction_type}&access_token={token}"
        headers_ = {'user-agent': W_ueragnt()}
        response = requests.post(auto_react_url, headers=headers_)

        if response.ok:
            success_count += 1
            print(f"{green}  REACTOR {i+1} ---> Successfully Reacted!")
        else:
            failure_count += 1
            print(f"{red}  REACTOR {i+1} ---> Failed to React!")

        time.sleep(1)  # Optional, to avoid rate-limiting

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed    : {white}{failure_count}")


def react_dp_cover():
    import requests
    import time

    ses = requests.Session()

    def get_access_tokens(file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return []

    # ===== Menu =====
    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO REACT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    if account_choose in ['1', '01']:
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose in ['2', '02']:
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose in ['3', '03']:
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose in ['4', '04']:
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose in ['0', '00']:
        main()
        return
    else:
        print(f"{red}  Invalid Input!")
        time.sleep(1.5)
        react_dp_cover()
        return

    access_tokens = get_access_tokens(file_path)
    if not access_tokens:
        return

    # DP/Cover ID input
    substory_index = input(f"{yellow}  Input DP/Cover FB ID: {green}")

    # Reaction choice
    print(f"{white}  CHOOSE REACTION:")
    print(f"{yellow}  [1] {blue}LIKE")
    print(f"{yellow}  [2] {blue}LOVE")
    print(f"{yellow}  [3] {blue}HAHA")
    print(f"{yellow}  [4] {blue}WOW")
    print(f"{yellow}  [5] {blue}ANGRY")
    print(f"{yellow}  [6] {blue}SAD")
    line()
    
    react_choice = input(f"{yellow}  Choose : {green}")
    reaction_types = {'1': 'LIKE', '2': 'LOVE', '3': 'HAHA', '4': 'WOW', '5': 'ANGRY', '6': 'SAD'}
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f"{red}  Invalid reaction choice.")
        return

    # Limit of reactions
    try:
        limit = int(input(f"{yellow}  Input quantity of reactions (limit {len(access_tokens)}): {green}"))
    except ValueError:
        print(f"{red}  Please enter a valid number.")
        return
    if limit > len(access_tokens):
        print(f"{red}  Limit exceeds available reactors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        auto_react_url = f"https://graph.facebook.com/v18.0/{substory_index}/reactions?type={reaction_type}&access_token={access_token}"
        headers_ = {'user-agent': W_ueragnt()}
        response = requests.post(auto_react_url, headers=headers_)

        if response.ok:
            success_count += 1
            print(f"{green}  REACTOR {i+1} ---> Successfully Reacted!")
        else:
            failure_count += 1
            print(f"{red}  REACTOR {i+1} ---> Failed to React!")

        time.sleep(1)

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed    : {white}{failure_count}")

headers_fb_lite = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/380.0.0.14.112;]',
    'viewport-width': '707' }

def react_with_care():
    from concurrent.futures import ThreadPoolExecutor
    import requests
    import time

    clear()
    logo()

    coki_file_name = '/sdcard/.EXTRACT-COOKIE-ACCOUNT.txt'
    try:
        with open(coki_file_name, 'r', encoding='utf-8') as file:
            coki_file = file.read().splitlines()
    except FileNotFoundError:
        print(f"{red}  Start the tool first!")
        return

    inpt_link = input(f"{yellow}  Post Link : {green}")
    uid = convert_to_traodoisub(inpt_link)
    if not uid:
        print(f"{red}  Unable to extract UID from the provided link.")
        return

    post_link = f"https://mbasic.facebook.com/reactions/picker/?ft_id={uid}&origin_uri="

    print(f"{white}  CHOOSE REACTION:")
    print(f"{yellow}  [1] {blue}LIKE")
    print(f"{yellow}  [2] {blue}LOVE")
    print(f"{yellow}  [3] {blue}CARE")
    print(f"{yellow}  [4] {blue}HAHA")
    print(f"{yellow}  [5] {blue}WOW")
    print(f"{yellow}  [6] {blue}ANGRY")
    print(f"{yellow}  [7] {blue}SAD")
    line()
    
    inx = input(f"{yellow}  Choose : {green}")
    reaction_ids = {
        '1': '1635855486666999',
        '2': '1678524932434102',
        '3': '613557422527858',
        '4': '115940658764963',
        '5': '478547315650144',
        '6': '444813342392137',
        '7': '908563459236466'
    }

    if inx not in reaction_ids:
        print(f"{red} Invalid option selected.")
        return

    r_id = reaction_ids[inx]

    try:
        limite = int(input(f"{yellow}  Input limit less than {green}{len(coki_file)}{yellow}: {green}"))
        if limite > len(coki_file):
            raise ValueError("Inputted limit exceeds available cookies.")
    except ValueError as e:
        print(f"{red}\n  Error: {e}")
        return

    clear()
    logo()
    print(f"{yellow}  Target    : {green}{uid}")
    print(f"{yellow}  Limit     : {green}{limite}")
    line()

    executor = ThreadPoolExecutor(max_workers=30)
    for i in range(min(len(coki_file), limite)):
        coki = coki_file[i]
        executor.submit(sending, coki, post_link, r_id)


def sending(coki, post_link, r_id):
    try:
        headers_fb_lite['cookie'] = coki
        getdata = html_req(post_link, Headers=headers_fb_lite, Cookie={'cookie': coki})
        all_links = getdata.find_all('a')
        
        reacted = False
        for link in all_links:
            if 'href' not in link.attrs:
                continue
            url = 'https://mbasic.facebook.com' + link['href']
            if r_id in url:
                response = requests.get(url, headers=headers_fb_lite, cookies={'cookie': coki})
                
                # Safely extract pageid from cookie
                try:
                    pageid = coki.split('c_user=')[1].split(';')[0]
                except IndexError:
                    pageid = 'Unknown'

                if pageid in response.text:
                    print(f"{yellow}  Successfully React! {white}---> {green}{pageid}")
                else:
                    print(f"{red}  Reaction attempt failed for {pageid}")
                
                reacted = True
                break  # Reaction done, stop loop
        
        if not reacted:
            print(f"{red}  Reaction link not found in the post for this cookie.")
    
    except Exception as e:
        print(f"{red}  An error occurred: {e}")


def react_comment():
    ses = requests.Session()

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return []

    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO REACT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()
    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return
    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        react_comment()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    comment_uid = input(f"{yellow}  Enter Comment UID: {green}")
    line()

    print(f"{white}  CHOOSE REACTION:")
    print(f"{yellow}  [1] {blue}LIKE")
    print(f"{yellow}  [2] {blue}LOVE")
    print(f"{yellow}  [3] {blue}HAHA")
    print(f"{yellow}  [4] {blue}WOW")
    print(f"{yellow}  [5] {blue}ANGRY")
    print(f"{yellow}  [6] {blue}SAD")
    line()
    
    react_choice = input(f"{yellow}  Choose : {green}")
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f"{red}  Invalid reaction choice.")
        return

    try:
        limit = int(input(f"{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available reactors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f"{comment_uid}"
        auto_react = f"https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}"
        time.sleep(1)

        headers_ = {'user-agent': W_ueragnt()}
        try:
            response = requests.post(auto_react, headers=headers_)
            if response.ok:
                print(f"{green}  REACTOR {i + 1} ---> Successfully React!")
                success_count += 1
            else:
                print(f"{red}  REACTOR {i + 1} ---> Failed to React!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  REACTOR {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


def react_reels():
    ses = requests.Session()

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return []

    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO REACT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()

    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return

    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        react_reels()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    reels_uid = input(f"{yellow}  Enter Reels Video UID: {green}")
    line()

    print(f"{white}  CHOOSE REACTION:")
    print(f"{yellow}  [1] {blue}LIKE")
    print(f"{yellow}  [2] {blue}LOVE")
    print(f"{yellow}  [3] {blue}HAHA")
    print(f"{yellow}  [4] {blue}WOW")
    print(f"{yellow}  [5] {blue}ANGRY")
    print(f"{yellow}  [6] {blue}SAD")
    line()

    react_choice = input(f"{yellow}  Choose : {green}")
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f"{red}  Invalid reaction choice.")
        return

    try:
        limit = int(input(f"{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available reactors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = reels_uid
        auto_react = f"https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}"
        time.sleep(1)

        headers_ = {'user-agent': W_ueragnt()}
        try:
            response = requests.post(auto_react, headers=headers_)
            if response.ok:
                print(f"{green}  REACTOR {i + 1} ---> Successfully React!")
                success_count += 1
            else:
                print(f"{red}  REACTOR {i + 1} ---> Failed to React!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  REACTOR {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


def follow():
    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO FOLLOW:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()

    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return

    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        follow()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    user_id = input(f"{yellow}  Enter target UID : {green}")
    line()

    try:
        limit = int(input(f"{yellow}  Input quantity of follows, limit is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available followers.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        auto_follow_url = f"https://graph.facebook.com/v19.0/{user_id}/subscribers"
        headers = {
            'Authorization': f"Bearer {access_token}",
            'user-agent': W_ueragnt()
        }
        time.sleep(1)
        try:
            response = requests.post(auto_follow_url, headers=headers)
            if response.ok:
                print(f"{green}  FOLLOWER {i + 1} ---> Successfully Follow!")
                success_count += 1
            else:
                print(f"{red}  FOLLOWER {i + 1} ---> Failed to Follow!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  FOLLOWER {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


def auto_comment():
    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                return response.json().get('id')
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = r'https://www\.facebook\.com/(\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None

    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO COMMENT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return

    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        auto_comment()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    post_link = input(f"{yellow}  Enter post link: {green}")
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        return

    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f"{red}  Failed to convert post link.")
        return

    input_comment = input(f"{yellow}  Enter Comment(s) (use '|' for multiple): {green}")
    comments = [c.strip().replace('&&', '\n') for c in input_comment.split('|')]
    num_comments = len(comments)

    try:
        limit = int(input(f"{yellow}  Enter number of comments, total available is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available commentors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]

        auto_comment_url = f"https://graph.facebook.com/{converted_link}/comments"
        params = {
            'message': comment,
            'access_token': access_token
        }

        time.sleep(1)
        headers = {'user-agent': W_ueragnt()}
        try:
            response = requests.post(auto_comment_url, params=params, headers=headers)
            if response.ok:
                print(f"{green}  COMMENTOR {i + 1} ---> Successfully Comment!")
                success_count += 1
            else:
                print(f"{red}  COMMENTOR {i + 1} ---> Failed to Comment!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  COMMENTOR {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


def auto_comment_to_dp():
    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None

    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO COMMENT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return

    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        auto_comment_to_dp()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    converted_link = input(f"{yellow}  Enter post FB ID: {green}")
    input_comment = input(f"{yellow}  Enter Comment(s) (use '|' for multiple): {green}")
    comments = [c.strip().replace('&&', '\n') for c in input_comment.split('|')]
    num_comments = len(comments)

    try:
        limit = int(input(f"{yellow}  Enter number of comments, total available is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available commentors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]

        auto_comment_url = f"https://graph.facebook.com/{converted_link}/comments"
        params = {
            'message': comment,
            'access_token': access_token
        }

        time.sleep(1)
        headers = {'user-agent': W_ueragnt()}
        try:
            response = requests.post(auto_comment_url, params=params, headers=headers)
            if response.ok:
                print(f"{green}  COMMENTOR {i + 1} ---> Successfully Comment!")
                success_count += 1
            else:
                print(f"{red}  COMMENTOR {i + 1} ---> Failed to Comment!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  COMMENTOR {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


def reply_to_comment():
    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None

    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO COMMENT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    
    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return

    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        reply_to_comment()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    converted_link = input(f"{yellow}  Enter comment FB ID: {green}")
    input_comment = input(f"{yellow}  Enter Comment(s) (use '|' for multiple): {green}")
    comments = [c.strip().replace('&&', '\n') for c in input_comment.split('|')]
    num_comments = len(comments)

    try:
        limit = int(input(f"{yellow}  Enter number of comments, total available is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available commentors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]

        reply_url = f"https://graph.facebook.com/{converted_link}/comments"
        params = {'message': comment, 'access_token': access_token}
        headers = {'user-agent': W_ueragnt()}

        time.sleep(1)
        try:
            response = requests.post(reply_url, params=params, headers=headers)
            if response.ok:
                print(f"{green}  COMMENTOR {i + 1} ---> Successfully Comment!")
                success_count += 1
            else:
                print(f"{red}  COMMENTOR {i + 1} ---> Failed to Comment!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  COMMENTOR {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


def auto_comment_to_reels():
    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None

    clear()
    logo()
    print(f"{white}  CHOOSE FACEBOOK TO COMMENT:")
    print(f"{yellow}  [1] {blue}YOUR FRA LIST")
    print(f"{yellow}  [2] {blue}YOUR RPA LIST")
    print(f"{yellow}  [3] {blue}YOUR FRA PAGES LIST")
    print(f"{yellow}  [4] {blue}YOUR RPA PAGES LIST")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()

    account_choose = input(f"{yellow}  Choose : {green}")
    line()

    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }

    if account_choose in ['0', '00']:
        main()
        return

    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f"{red}  Invalid Input!")
        sleep(1.5)
        auto_comment_to_reels()
        return

    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return

    converted_link = input(f"{yellow}  Enter Reels Video UID: {green}")
    input_comment = input(f"{yellow}  Enter Comment(s) (use '|' for multiple): {green}")
    comments = [c.strip().replace('&&', '\n') for c in input_comment.split('|')]
    num_comments = len(comments)

    try:
        limit = int(input(f"{yellow}  Enter number of comments, total available is {green}{len(access_tokens)}: "))
    except ValueError:
        print(f"{red}  Error: Please enter a valid number for the limit.")
        return

    if limit > len(access_tokens):
        print(f"{red}  Error: The specified limit exceeds the number of available commentors.")
        return

    success_count = 0
    failure_count = 0

    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]

        comment_url = f"https://graph.facebook.com/{converted_link}/comments"
        params = {'message': comment, 'access_token': access_token}
        headers = {'user-agent': W_ueragnt()}

        time.sleep(1)
        try:
            response = requests.post(comment_url, params=params, headers=headers)
            if response.ok:
                print(f"{green}  COMMENTOR {i + 1} ---> Successfully Comment!")
                success_count += 1
            else:
                print(f"{red}  COMMENTOR {i + 1} ---> Failed to Comment!")
                failure_count += 1
        except Exception as e:
            print(f"{red}  COMMENTOR {i + 1} ---> Error: {e}")
            failure_count += 1

    line()
    print(f"{yellow}  TOTAL:")
    print(f"{green}  Completed : {white}{success_count}")
    print(f"{red}  Failed : {white}{failure_count}")


import requests
import time

def auto_share():
    clear()
    logo()
    print("Note: Use Facebook Lite when copying post link.")
    post_link = input("Enter post link: ").strip()
    token = input("Enter access token: ").strip()

    try:
        limit = int(input("Enter number of shares: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    success_count = 0
    failure_count = 0

    for i in range(limit):
        url = f"https://graph.facebook.com/v18.0/me/feed"
        params = {
            "link": post_link,
            "access_token": token
        }
        try:
            response = requests.post(url, data=params)
            if response.ok:
                print(f"Share {i+1} --> Success")
                success_count += 1
            else:
                print(f"Share {i+1} --> Failed ({response.text})")
                failure_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Share {i+1} --> Error: {e}")
            failure_count += 1

        time.sleep(1)

    print("\nTOTAL:")
    print(f"Completed: {success_count}")
    print(f"Failed: {failure_count}")

headers_global = {
    'user-agent': W_ueragnt(),
    'viewport-width': '576' }
ser = requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/cnt/main/MY_SELL_PROJECT/smm.txt').text
speed = 100
allcookie = []
s_react = []
s_comment = []
s_flw = []
logos = logo

def enc(txt):
    encoded_bytes = base64.b64encode(txt.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string


def start_tool():
    clear()
    logo()
    print(f"{yellow}  [1] {cyan}EXTRACT NORMAL ACCOUNT PAGES     {yellow}-  {green}[UID and Password]")
    print(f"{yellow}  [2] {cyan}EXTRACT SINGLE NORMAL ACCOUNT    {yellow}-  {green}[No Duplicate Checker]")
    print(f"{yellow}  [3] {cyan}EXTRACT BULK NORMAL ACCOUNTS M1  {yellow}-  {green}[Thru TXT File]")
    print(f"{yellow}  [4] {cyan}EXTRACT BULK NORMAL ACCOUNTS M2  {yellow}-  {green}[Thru TXT File]")
    print(f"{yellow}  [5] {cyan}EXTRACT BULK ACCOUNTS PAGES      {yellow}-  {green}[Thru TXT File]")
    print(f"{yellow}  [0] {red}RETURN TO MAIN MENU")
    line()

    choice = input(f"{yellow}  Choose : {green}").strip()

    if choice == '1':
        get_facebook_pages()
    elif choice == '2':
        get_facebook_account()
    elif choice == '3':
        bgraph_bulk_account()
    elif choice == '4':
        datr()
    elif choice == '5':
        bgraph_bulk_pages()
    elif choice == '0':
        main()
    else:
        print(f"{red}  Invalid choice. Please pick a number from 0 to 5.")
        time.sleep(1.5)
        start_tool()

def count_lines_in_files(*file_paths):
    labels = ['FRA ACCOUNT', 'RPA ACCOUNT', 'FRA PAGES', 'RPA PAGES']
    
    for i, file_path in enumerate(file_paths, start=1):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                total_lines = sum(1 for _ in file)
            
            if i <= len(labels):
                print(f"\t\t{blue}     {labels[i-1]} {yellow}: {green}{total_lines}")
        except FileNotFoundError:
            print(f"\t\t{red}   {file_path} Not Found!")

path_file1 = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
path_file2 = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
path_file3 = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
path_file4 = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'

def main():
    clear()
    logo()

    # Initialize files
    files = [
        '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt',
        '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt',
        '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt',
        '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt',
        '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
    ]
    for file in files:
        open(file, 'a').write('')

    # Boosting tool overview
    print(f'\t\t{cyan}YOUR BOOSTING TOOL OVERVIEW')
    path_file1, path_file2, path_file3, path_file4 = files[0], files[2], files[4], files[6]
    count_lines_in_files(path_file1, path_file2, path_file3, path_file4)
    line()

    # Menu
    menu = [
        "[01] START TOOL",
        "[02] AUTO REACT W/O CARE",
        "[03] AUTO REACT WITH CARE",
        "[04] AUTO REACT TO COMMENT",
        "[05] AUTO REACT TO DP & COVER",
        "[06] AUTO REACT TO REELS",
        "[07] AUTO FOLLOW",
        "[08] AUTO COMMENT TO POST",
        "[09] AUTO COMMENT TO REELS",
        "[10] AUTO COMMENT TO DP",
        "[11] REPLY TO COMMENT",
        "[12] AUTO SHARE",
        "[13] AUTO GROUP JOIN",
        "[14] LIKE & FOLLOW PAGE",
        "[15] STORED PAGES AND ACCOUNT",
        "[16] RESET TOOL",
        "[00] EXIT"
    ]
    for item in menu:
        print(f'{yellow}  {item}')

    line()
    choice = input(f'{yellow}  Choose : {green}').zfill(2)  # ensures '01', '02', etc.

    # Choice handling
    if choice == '01':
        start_tool()
    elif choice == '02':
        react()
    elif choice == '03':
        react_with_care()
    elif choice == '04':
        react_comment()
    elif choice == '05':
        react_dp_cover()
    elif choice == '06':
        react_reels()
    elif choice == '07':
        follow()
    elif choice == '08':
        auto_comment()
    elif choice == '09':
        auto_comment_to_reels()
    elif choice == '10':
        auto_comment_to_dp()
    elif choice == '11':
        reply_to_comment()
    elif choice == '12':
        auto_share()
    elif choice == '13':
        g_join()
    elif choice == '14':
        p_like()
    elif choice == '15':
        store()
    elif choice == '16':
        delete_files()
    elif choice == '00':
        print(f'\n{red}  Byeeeeers!')
        exit()
    else:
        print(f'{red}  Invalid choice.')

if __name__ == '__main__':
    main()

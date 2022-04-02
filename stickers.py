import argparse
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from telegram.ext import ExtBot
from telegram.error import BadRequest

load_dotenv(dotenv_path=Path(__file__).parent / '.env')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
USER_ID = os.environ.get('USER_ID')
Bot = ExtBot(token=BOT_TOKEN)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='peepo_emotes', help='fpath to a directory containing src/ and mappings.json')
    return parser.parse_args()

def main():
    args = parse_arguments()
    print(Bot.get_me()['username'])
    sticker_data = json.load(open(f"{args.dir}/mapping.json", "r"))
    stickers = sticker_data['stickers']
    try:
        print("Finding existing Stickerset...")
        Bot.get_sticker_set(name=sticker_data['name'])
    except BadRequest:
        print("Stickerset not found, creating one...")
        Bot.create_new_sticker_set(user_id=USER_ID, name=f"peepo_by_{Bot.get_me()['username']}", title=sticker_data["title"], 
                                    emojis=stickers[0]['emoji'], webm_sticker=open(f"{args.dir}/src/{stickers[0]['file']}", "rb"))
        return
    # pass

if __name__ == '__main__':
    main()
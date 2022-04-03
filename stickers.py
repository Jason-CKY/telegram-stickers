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
    parser.add_argument('--dir', default=['peepo_emotes'], nargs='+', help='fpath to a directory containing src/ and mappings.json')
    parser.add_argument('--delete', action='store_true', help='Set to delete the stickerpack')
    return parser.parse_args()

def update_stickers(dir: str, delete: bool = False):
    sticker_data = json.load(open(f"{dir}/mapping.json", "r"))
    sticker_name = f"{sticker_data['name']}_by_{Bot.get_me()['username']}"
    stickers = sticker_data['stickers']
    try:
        print("Finding existing Stickerset...")
        sticker_set = Bot.get_sticker_set(name=sticker_name)
    except BadRequest:
        print("Stickerset not found, creating one...")
        Bot.create_new_sticker_set(user_id=USER_ID, name=sticker_name, title=sticker_data["title"], 
                                    emojis=stickers[0]['emoji'], webm_sticker=open(f"{dir}/src/{stickers[0]['file']}", "rb"))
        sticker_set = Bot.get_sticker_set(name=sticker_name)
    
    # Delete all stickers in set
    print("Deleting all existing stickers in stickerset...")
    for sticker in sticker_set['stickers']:
        Bot.delete_sticker_from_set(sticker=sticker['file_id'])

    if delete:
        return

    # Add stickers to stickerset, effectively updating all stickers in stickerset with what's inside the tracked repo
    for sticker in stickers:
        fname = f"{dir}/src/{sticker['file']}"
        emoji = sticker['emoji']
        print(f"Adding sticker {fname} ({emoji})")
        Bot.add_sticker_to_set(user_id=USER_ID, name=sticker_name,
                            emojis=emoji, webm_sticker=open(fname, "rb"))   

def main():
    args = parse_arguments()
    for dir in args.dir:
        update_stickers(dir, args.delete)

if __name__ == '__main__':
    main()
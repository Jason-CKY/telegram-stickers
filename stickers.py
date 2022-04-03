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
    sticker_data = json.load(open(f"{args.dir}/mapping.json", "r"))
    sticker_name = f"{sticker_data['name']}_by_{Bot.get_me()['username']}"
    stickers = sticker_data['stickers']
    try:
        print("Finding existing Stickerset...")
        sticker_set = Bot.get_sticker_set(name=sticker_name)
    except BadRequest:
        print("Stickerset not found, creating one...")
        Bot.create_new_sticker_set(user_id=USER_ID, name=sticker_name, title=sticker_data["title"], 
                                    emojis=stickers[0]['emoji'], webm_sticker=open(f"{args.dir}/src/{stickers[0]['file']}", "rb"))
        sticker_set = Bot.get_sticker_set(name=sticker_name)
    
    # Delete all stickers in set
    print("Deleting all existing stickers in stickerset...")
    for sticker in sticker_set['stickers']:
        Bot.delete_sticker_from_set(sticker=sticker['file_id'])
    # Add stickers to stickerset, effectively updating all stickers in stickerset with what's inside the tracked repo
    for sticker in stickers:
        fname = f"{args.dir}/src/{sticker['file']}"
        emoji = sticker['emoji']
        print(f"Adding sticker {fname} ({emoji})")
        Bot.add_sticker_to_set(user_id=USER_ID, name=sticker_name,
                            emojis=emoji, webm_sticker=open(fname, "rb"))   

if __name__ == '__main__':
    main()
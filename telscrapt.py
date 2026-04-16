#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:54:49 2026

@author: macbook
"""



import nest_asyncio
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import csv


nest_asyncio.apply()


api_id = "ID"                 
api_hash = "API"     
group_username = "Telegram group"  


async def main():
    async with TelegramClient("session", api_id, api_hash) as client:
        print("✅ Logged in successfully")

        group = await client.get_entity(group_username)

        all_members = []
        offset = 0
        limit = 100

        print("⏳ Fetching members...")
        while True:
            participants = await client(GetParticipantsRequest(
                channel=group,
                filter=ChannelParticipantsSearch(""),
                offset=offset,
                limit=limit,
                hash=0
            ))

            if not participants.users:
                break

            all_members.extend(participants.users)
            offset += len(participants.users)
            print(f"Fetched {len(all_members)} members so far...")

        print(f"✅ Total members fetched: {len(all_members)}")


        members_to_message = [u for u in all_members if u.username is not None]
        print(f"✅ Members with username: {len(members_to_message)}")


        with open("members_filtered.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "username", "first_name", "last_name"])
            for u in members_to_message:
                writer.writerow([
                    u.id,
                    u.username,
                    getattr(u, "first_name", ""),
                    getattr(u, "last_name", "")
                ])
        print("✅ CSV saved as 'members_filtered.csv'")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

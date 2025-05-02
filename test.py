from telethon.sync import TelegramClient
from telethon.errors import ChatWriteForbiddenError, MediaCaptionTooLongError, MessageIdInvalidError
import time

# === CONFIG ===
api_id = 23687628
api_hash = '4690056c2040c6924e2b67ff993ebb46'
phone = '+923305639008'

source_chat = 'me'
source_message_id = 73205

target_chats = [
    '@Syedaclouds',
    '@ITBusinessSolutions',
    '@CloudMarketing91',
    '@LegitRdpselling',
    '@Awais_CloudsBuyAndSell',
    '@buyandsell_vpstrade',
    '@Razacloud',
    '@cloudsaller',
    '@JaniCloudBuySell',
    '@CloudAccHub',
   '@cloudstoree_01',
   '@CloudSellingMarket',
   'https://t.me/+HEZ3E7LbDL9hODk0'
]

interval = 100  # 1 hour

# === START TELETHON CLIENT ===
with TelegramClient('forward_session', api_id, api_hash) as client:
    print("Logged in. Forwarding message to multiple chats every hour...")

    while True:
        for chat in target_chats:
            try:
                # Try to forward message
                client.forward_messages(
                    entity=chat,
                    messages=source_message_id,
                    from_peer=source_chat
                )
                print(f"Forwarded to {chat}")
            except MessageIdInvalidError:
                print(f"Message ID {source_message_id} not found in {source_chat}")
            except ChatWriteForbiddenError:
                print(f"Bot is blocked or not allowed to write in {chat}")
            except Exception as e:
                # Fallback: send plain text if media is restricted
                try:
                    original_msg = client.get_messages(source_chat, ids=source_message_id)
                    if original_msg.text:
                        client.send_message(chat, original_msg.text)
                        print(f"Sent plain text fallback to {chat}")
                    else:
                        print(f"Cannot send fallback. Message has no text content.")
                except Exception as inner_e:
                    print(f"Failed to send fallback to {chat}: {inner_e}")
        time.sleep(interval)

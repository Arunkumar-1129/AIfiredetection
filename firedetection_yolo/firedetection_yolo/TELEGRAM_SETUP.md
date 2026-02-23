# Telegram Fire Alert Setup

## Step 1: Create Telegram Bot
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow instructions to name your bot
4. Copy the **Bot Token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 2: Get Your Chat ID
1. Search for `@userinfobot` in Telegram
2. Start a chat and it will send your **Chat ID** (looks like: `123456789`)

## Step 3: Configure Environment Variables

### For Local Development:
Set these in your terminal:
```bash
set TELEGRAM_BOT_TOKEN=your_bot_token_here
set TELEGRAM_CHAT_ID=your_chat_id_here
```

### For Render Deployment:
Add these in Render Dashboard → Environment Variables:
- `TELEGRAM_BOT_TOKEN`: your_bot_token_here
- `TELEGRAM_CHAT_ID`: your_chat_id_here

## Step 4: Test
Run your fire detection and you'll receive Telegram alerts when fire/smoke is detected with >20% confidence!

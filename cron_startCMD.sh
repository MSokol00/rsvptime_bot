#!/usr/bin/env bash
if [ -z "$(pidof python /home/MSokol00/Projects/telegram.rsvptime_bot/bot.py)" ]
then
    python /home/MSokol00/Projects/telegram.rsvptime_bot/cron_startCMD.sh
fi
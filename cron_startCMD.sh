#!/usr/bin/env bash
pidof python /home/MSokol00/Projects/telegram.rsvptime_bot/bot.py > /dev.null
if [ $? -eq 0 ]
then
    echo Program Running
else
    python /home/MSokol00/Projects/telegram.rsvptime_bot/cron_startCMD.sh
fi
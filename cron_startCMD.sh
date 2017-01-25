#!/usr/bin/env bash

case "$(ps aux | grep telegram.rsvptime_bot/bot.py | wc -l)" in

1)  echo "Restarting Amadeus:     $(date)" >> /var/log/telegram.rsvptime_bot.txt
    python /home/MSokol00/Projects/telegram.rsvptime_bot/bot.py &
    echo "restarting"
    ;;
2)  # all ok
    echo "All ok"
    ;;
esac;
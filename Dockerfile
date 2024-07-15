FROM python

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "/app/discord_bot.py" ]

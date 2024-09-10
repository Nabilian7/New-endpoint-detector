import subprocess
import requests
import sqlite3
import time

target = "https://www.actcorp.in/"

def run_hakrawler(url):
    command = rf"echo {url} | hakrawler -u | egrep -o '(\.js|\.css|\.png|\.jpg|\.gif)'"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    line = output.decode('utf-8')
    return line

def discord_notification(url):
    webhook = "https://discord.com/api/webhooks/1283021299375149057/mSJbbQB57bi1MH2bvuvkcvms-xoRWUyYtjmyZmflxc_DCD9Iq-hNnn7_HOMJiaocqQdh"
    message = {"content": "New Endpoint Found: "+url}
    requests.post(webhook, json=message)

def main():
    conn = sqlite3.connect('hakrawler-out.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            column_name TEXT PRIMARY KEY
        )
    """)
    sql = "INSERT OR IGNORE INTO urls (column_name) VALUES (?)"
    urls = run_hakrawler(target).splitlines()
    for url in urls:
        if target in url:
            cursor.execute("SELECT * FROM urls WHERE column_name = ?", (url,))
            existing_data = cursor.fetchone()
            if not existing_data:
                cursor.execute(sql, (url,))
                discord_notification(url)
    conn.commit()
    conn.close()

while True:
    main()
    time.sleep(24 * 60 * 60)
In bug bounty programs, being able to map new attack surfaces or discover 
new domains/subdomains for your targets can provide an edge over other 
bug hunters. This advantage arises because applications frequently add new 
subdomains and pages. Being the first to test these new elements can offer a 
significant benefit in terms of finding easily exploitable vulnerabilities, often 
referred to as “low-hanging fruits”.
There are various methods to achieve this, but one preferred approach 
includes the use of a Discord server. Discord is highly effective in this regard due 
to its real-time communication and notification capabilities. Discord allows the 
use of webhooks, which are essentially automated messages sent from application into Discord. The script runs continuously, executing the main function 
once every 24 hours; however, the frequency can be adjusted to suit your needs.
This can be used to set up webhooks to post messages in a specific channel 
whenever a relevant event occurs, such as discovery of a new subdomain or 
a change on a web page.
Let’s see this in action. On the Discord server, we will navigate to the 
“Integrations” page to create a new webhook. This will generate a unique 
webhook link

The following Python code demonstrates the entire process in action. The 
“target” parameter is used to specify the URL that needs to be crawled. 
Meanwhile, the “webhook” parameter is intended for providing Discord 
webhook links generated in the previous step

Note: The discord_notification function sends a message to a specified 
Discord webhook. Hence, when you receive the notification, You need to 
replace your [discord webhook] with your actual Discord webhook URL.
Upon running this script, notifications will be sent in real time to the specified Discord channel whenever a new endpoint is discovered. The discovered 
endpoints will also be saved in the SQLite database

![image](https://github.com/user-attachments/assets/d667c344-d85e-4839-9e3d-1d1b3cf6c105)

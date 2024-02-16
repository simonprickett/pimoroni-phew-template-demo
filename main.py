from phew import connect_to_wifi, is_connected_to_wifi, server
from phew.template import render_template
import config

def home_page(request):
    # Pass in some data as a list of tuples.
    # (<chart position>, <change from last week>, <artist>, <title>)
    # Data from https://uk-charts-archive.fandom.com/wiki/UK_Singles_%26_Album_Chart_(12/03/1983)
    uk_top_ten_singles_12_march_83 = [
        (1, 0, "Bonnie Tyler", "Total Eclipse of the Heart"),
        (2, -1, "Michael Jackson", "Billie Jean"),
        (3, 2, "Eurythmics", "Sweet Dreams"),
        (4, 8, "Forrest", "Rock the Boat"),
        (5, -1, "Toto", "Africa"),
        (6, -3, "Kajagoogoo", "Too Shy"),
        (7, 14, "Bananarama", "Na Na Hey Hey Kiss Him Goodbye"),
        (8, 0, "Madness", "Tomorrow's Just Another Day"),
        (9, 0, "The Thompson Twins", "Love on Your Side"),
        (10, -4, "Musical Youth", "Never Gonna Give You Up")
    ]
    
    return render_template("templates/index.html", top_ten = uk_top_ten_singles_12_march_83)

def catch_all(request):
    return "Not found.", 404

server.add_route("/", handler = home_page, methods = [ "GET" ])
server.set_callback(catch_all)

ip_address = connect_to_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)

if is_connected_to_wifi():
    print(f"Connected to wifi network, IP is {ip_address}")
else:
    print("Failed to connect to wifi, check credentials in config.py.")

server.run()
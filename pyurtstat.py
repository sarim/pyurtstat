#!/usr/bin/env python
import socket, sys, getopt

def get_server_details(host, port):
    # Data Place Holders
    urt_server_details = {}

    # Socket Request Message
    MESSAGE = "\377\377\377\377getstatus"

    # Get response from server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((host, int(port)))
        sock.send(MESSAGE)
        response, addr = sock.recvfrom(1024)
        sock.close()
        response_lines = response.split("\n")
    except Exception, exc:
        print "The connection to the server failed. Did you provide the correct hostname and port?"
        print "Error message for the Geeks: " + str(exc)
        sys.exit(2)

    # Retrieve the server settings
    config_string_parts = response_lines[1].split("\\")
    urt_server_details['configs'] = {}
    for i in range(1, len(config_string_parts), 2):
        urt_server_details['configs'][config_string_parts[i].strip()] = config_string_parts[i + 1].strip()

    urt_server_details['players'] = []
    for x in range(2, (len(response_lines) - 1)):
        player_data = response_lines[x].split(" ",2)
        player_dictionary = {"ping": player_data[1], "kills": player_data[0], "name": player_data[2][1:-1]}
        urt_server_details['players'].append(player_dictionary)

    return urt_server_details


def print_usages():
    print "-h,--help\t Display this message"
    print "-c,--configs\t Specify one or more server configuration opetion (seperate with comma). Use 'all' to print all config values"


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "hc:", ["help", "configs="])
    except getopt.GetoptError, err:
        print_usages()
        sys.exit(2)

    port = 27960
    configs = []

    for option, value in opts:
        if option in ("-c", "--configs"):
            configs = value.split(",")
        elif option in ("-h", "--help"):
            print_usages()
            sys.exit()
        else:
            print_usages()
            sys.exit(2)

    if len(args) < 1:
        print "Please provide a host (either a hostname or IP address)"
        sys.exit(2)
    else:
        host = args[0]
        if ":" in host:
            port = int(host.split(":")[1])
            host = host.split(":")[0]

    server_details = get_server_details(host, port)
    print ""
    print "-----" * 5
    print host + ":" + str(port)
    print "-----" * 5
    print ""
    if len(configs) > 0:
        if len(configs) == 1 and configs[0] == "all":
            template = "{Config:30} \t {Value:30}"
            print template.format(Config="Config", Value="Value")
            print template.format(Config="-----" * 6, Value="-----" * 6)
            for config in server_details['configs']:
                print template.format(Config=config, Value=server_details['configs'][config])
            print "\n"

        else:
            template = "{Config:30} \t {Value:30}"
            print template.format(Config="Config", Value="Value")
            print template.format(Config="-----" * 6, Value="-----" * 6)
            for config in configs:
                print template.format(Config=config, Value=server_details['configs'][config])
            print "\n"
    else:
        if(len(server_details['players']) > 0):
            template = "{Name:30} \t {Ping:4} \t {Kills:5}"
            print template.format(Name="Name", Ping="Ping", Kills="Kills")
            print template.format(Name="-----" * 6, Ping="----", Kills="-----")
            for player in server_details['players']:
                print template.format(Name=player['name'], Ping=player['ping'], Kills=player['kills'])

            print "\n"
        else:
            print "No one is playing on the server at this moment. \n"


if __name__ == "__main__":
    main()

import socket

""" Satellite Server area """
#SAT_SERVER="http://sat631.local.domain"
#USERNAME="admin"
#PASSWORD="redhat"
SAT_SERVER=""
USERNAME=""
PASSWORD=""


""" Capsule area """
CAPSULE_NAME=socket.gethostname()
# test machine
#CAPSULE_NAME="sat631caps.local.domain"

""" Pulp area """
CONF_FILE="/etc/pulp/server.conf"

""" General area """
#LOG="/var/log/pulp_cleanup.log"
LOG="/tmp/pulp_cleanup.log"

# Keep this false to keep data on the pulp repos
COMMIT="False"
# pulp_capsule_cleanup

Welcome, the idea of this project is just to reclaim space on file system from Satellite Capsules after remove one/a lot lifecycles from the Capsule. Actually the product doesn't provide any tool or feature to do it, then this app will help on this process.

Below instuctions about how to use.

0. Do one backup of your machine :-), this script is not supported by the Company, actually is just to improve the funcionality and fix some issues related to space/storage.
1. Copy this file to the Satellite Capsule
2. Will be necessary edit the file const.py to update the username / password to authenticate on the Satellite. Yet on the same file, will be necessary update the pulp password

All information below
~~~
SAT_SERVER="http://sat631.local.domain"
USERNAME="admin"
PASSWORD="redhat"
~~~

The Pulp password
~~~
CAP_PASSWORD="aZCehD5szBULC4z2EZhHFZGg5BJav9je"
~~~
to collect this one from your environment, execute the command below
~~~
\# grep ^default_password password /etc/pulp/server.conf|cut -d: -f3 | sed -e 's/ //'
TYHXmXF7Nm2VKogWCpE9Pk82JoVr6geq
~~~



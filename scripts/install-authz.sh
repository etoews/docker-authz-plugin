#!/bin/bash

# use the plugin when the docker daemon starts
sed -i 's/.*provider.*/&\n--authorization-plugin=authz/' /var/lib/boot2docker/profile

# initialize our "datastore"
echo "False" > /var/run/authz-said-hello.txt

# install the dependencies and run the plugin
pip install -r requirements.txt
uwsgi --ini uwsgi.ini &

# restart the docker daemon
/etc/init.d/docker restart

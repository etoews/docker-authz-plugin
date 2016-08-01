#!/bin/bash

# get the python plugin code
apt-get -y install python-dev python-pip
git clone https://github.com/everett-toews/docker-authz-python-plugin.git
cd docker-authz-python-plugin

# install the dependencies and run the plugin
pip install -r requirements.txt
mkdir /run/docker/plugins/
uwsgi --ini uwsgi.ini &

# modify the docker service start up to look for the plugin
mkdir /etc/systemd/system/docker.service.d
cat << EOF > /etc/systemd/system/docker.service.d/authz.conf
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// --authorization-plugin=authz
EOF

# initialize our datastore :)
echo "False" > /var/run/authz-said-hello.txt

# reload systemd and restart the docker service
systemctl daemon-reload
systemctl restart docker

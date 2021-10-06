#!/bin/sh
# Author: van.le@chromaway.com
# -------------------------------------------------
PGHOST=${PGHOST:-localhost}
POSTGRES_USER=${POSTGRES_USER:-postchain}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-postchain}
# replace postgres_db instead localhost
sed -i "s/localhost/$PGHOST/g" /usr/src/rell/config/common.properties
sed -i "s/localhost/$PGHOST/g" /usr/src/rell/config/node-config.properties
# replace postgres credential  instead postchain
sed -i "s/__postchain_db_user__/$POSTGRES_USER/g" /usr/src/rell/config/common.properties
sed -i "s/__postchain_db_password__/$POSTGRES_PASSWORD/g" /usr/src/rell/config/common.properties


# TODO these following commands should be run once
/opt/postchain-node/postchain.sh wipe-db -nc /usr/src/rell/config/node-config.properties
/opt/postchain-node/postchain.sh add-blockchain -bc  /usr/src/rell/config/0.xml -cid 0 -nc /usr/src/rell/config/node-config.properties
/opt/postchain-node/postchain.sh peerinfo-add -h localhost -nc /usr/src/rell/config/node-config.properties -p 9870 -pk 02463ADFA20164C79415602AA6DEC2031E6CC3241F0760C720F9125ECD26012FBA
exec /opt/postchain-node/postchain.sh run-node -cid 0 -nc /usr/src/rell/config/node-config.properties
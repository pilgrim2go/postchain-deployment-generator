# postchain-deployment-generator





### Pre-requisites

jdk to run postchain keygen

python3


### Installation

git clone https://github.com/pilgrim2go/postchain-deplyment-generator

Use `download-binaries.sh` to get postchain


### Howto


#### Run Chromunity Backend

Chromunity Rell Source can be found here https://github.com/snieking/chromunity/tree/dev/rell

##### Generate deployment files for Chromunity

`python .\generator.py -n 4 -c .\samples\chromunity\config.yaml -d .\samples\chromunity\`


Go to chromunity/samples/_build

Build Image

`docker-compose build`

Start Chromunity Postchain Backend

or `docker-compose up -d `


or `docker-compose up -d --build`


##### Deploy Chromunity Using Kubernetes

`cd kubernetes`

Create namespace

`kubectl create ns chromunity`

Deploy 

`kubectl apply -f . -n chromunity`

Check logs

` kubectl  -n chromunity logs --tail=200 -f -l apps=node3`

and get something like following

```
deployment.apps/node0 created
service/node0 created
service/ext-node0 created
deployment.apps/node1 created
service/node1 created
service/ext-node1 created
deployment.apps/node2 created
service/node2 created
service/ext-node2 created
deployment.apps/node3 created
service/node3 created
service/ext-node3 created
configmap/postchain-env created
deployment.apps/postgres-db created
service/postgres-db created
```

Check logs

```
 kubectl  -n chromunity logs --tail=200 -f -l apps=node3
2021-08-16 02:18:40.584 INFO  PostchainApp - STARTING POSTCHAIN APP
2021-08-16 02:18:40.607 INFO  PostchainApp -     source directory: /usr/src/rell/src
2021-08-16 02:18:40.607 INFO  PostchainApp -     run config file: /usr/src/rell/config/run.xml
2021-08-16 02:18:40.608 INFO  PostchainApp -
2021-08-16 02:18:40.670 INFO  RellCliUtils - rell: 0.10.4; postchain: 3.3.3; time: 2021-06-25T09:23:12+0000; branch: origin/v0.10.4; commit: 6e7207c (2021-06-25T09:02:01+0000); dirty: false
2021-08-16 02:18:54.978 INFO  SQLDatabaseAccess - Meta table does not exist! Assume database does not exist and create it (version: 2).
2021-08-16 02:18:55.421 INFO  log - Logging initialized @20814ms to org.eclipse.jetty.util.log.Slf4jLog
2021-08-16 02:18:55.573 INFO  EmbeddedJettyServer - == Spark has ignited ...
2021-08-16 02:18:55.574 INFO  EmbeddedJettyServer - >> Listening on 0.0.0.0:7740
2021-08-16 02:18:55.576 INFO  Server - jetty-9.4.z-SNAPSHOT, build timestamp: 2017-11-21T21:27:37Z, git hash: 82b8fb23f757335bb3329d540ce37a2a2615f0a8
2021-08-16 02:18:55.681 INFO  session - DefaultSessionIdManager workerName=node0
2021-08-16 02:18:55.685 INFO  session - No SessionScavenger set, using defaults
2021-08-16 02:18:55.705 INFO  session - Scavenging every 600000ms
2021-08-16 02:18:55.823 INFO  AbstractConnector - Started ServerConnector@5eb7fac6{HTTP/1.1,[http/1.1]}{0.0.0.0:7740}
2021-08-16 02:18:55.828 INFO  Server - Started @21230ms
2021-08-16 02:18:55.830 INFO  RestApi - Rest API listening on port 7740 and were given 7740
2021-08-16 02:18:55.832 INFO  RestApi - Rest API attached on /
2021-08-16 02:18:57.079 INFO  PostchainApp - Chain 'main' ID = 1 RID = 75ADE7EE7AF02CBFBD78B97EED8ADB350A89A285D769ADA8CB39B60141FF884A
2021-08-16 02:18:57.083 INFO  BaseBlockchainProcessManager - [02ED:8A]: stopBlockchain() - Stopping of Blockchain: chainId: 1
2021-08-16 02:18:57.085 INFO  BaseBlockchainProcessManager - [02ED:8A]: stopBlockchain() - Stopping blockchain, shutdown complete: chainId: 1
2021-08-16 02:18:57.087 INFO  BaseBlockchainProcessManager - [02ED:8A]: startBlockchain() - Starting of blockchain: chainId: 1
2021-08-16 02:18:59.217 INFO  SqlInit - Initializing database (chain_iid = 1)
2021-08-16 02:19:04.284 INFO  DefaultXConnectionManager - [02ED:8A]/[75:4A]: Connecting chain peer: chain = 1, peer = 027B:08
2021-08-16 02:19:04.366 INFO  DefaultXConnectionManager - [02ED:8A]/[75:4A]: New OUTGOING connection: peer = 027B:08, blockchainRID: 75ADE7EE7AF02CBFBD78B97EED8ADB350A89A285D769ADA8CB39B60141FF884A, (size of c4Brid: 1, size of chains: 1)
2021-08-16 02:19:04.367 INFO  NetworkNodes - ------------------------------------
2021-08-16 02:19:04.367 INFO  NetworkNodes - Clearing the read-only node overuse counter. Number of read-only nodes in contact since yesterday: 0. Total calls from read-only nodes: 0
2021-08-16 02:19:04.367 INFO  NetworkNodes - ------------------------------------
2021-08-16 02:19:04.519 INFO  BaseBlockchainProcessManager - [02ED:8A]/[75:4A]: stopBlockchain() - Blockchain has been started: chainId: 1
2021-08-16 02:19:04.528 INFO  PostchainApp -
2021-08-16 02:19:04.529 INFO  PostchainApp - POSTCHAIN APP STARTED
2021-08-16 02:19:04.533 INFO  PostchainApp -     REST API port: 7740
2021-08-16 02:19:04.534 INFO  PostchainApp -
2021-08-16 02:19:04.668 INFO  DefaultXConnectionManager - [02ED:8A]/[75:4A]: New INCOMING connection: peer = 0342:EC, blockchainRID: 75ADE7EE7AF02CBFBD78B97EED8ADB350A89A285D769ADA8CB39B60141FF884A, (size of c4Brid: 1, size of chains: 1)
2021-08-16 02:19:06.045 INFO  DefaultXConnectionManager - [02ED:8A]/[75:4A]: Connecting chain peer: chain = 1, peer = 03D4:80
2021-08-16 02:19:06.054 INFO  DefaultXConnectionManager - [02ED:8A]/[75:4A]: New OUTGOING connection: peer = 03D4:80, blockchainRID: 75ADE7EE7AF02CBFBD78B97EED8ADB350A89A285D769ADA8CB39B60141FF884A, (size of c4Brid: 1, size of chains: 1)
```




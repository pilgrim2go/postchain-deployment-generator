### Steps

#### Create namespace (optional)

`kubectl create ns test1`

#### start postgres instance

 `kubectl -n test1 apply -f postchain-configmap.yaml`
 `kubectl -n test1 apply -f postgres-deployment.yaml`

#### start node0 

`kubectl -n test1 apply -f node0-deployment.yaml`

#### Check log
`kubectl -n test1 logs -f -l apps=node3`


#### Start other deployment

`kubectl -n test1 apply -f .`



helm install  grafana grafana/grafana \
    --namespace grafana \
    --set adminPassword='admin' \
    --values grafana.yml \
    --set persistence.enabled=true \
    --set service.type=LoadBalancer \
    --set image.tag=7.5.0

# kubectl create ns kubegraf
# kubectl apply -f https://raw.githubusercontent.com/devopsprodigy/kubegraf/master/kubernetes/serviceaccount.yaml
# kubectl apply -f https://raw.githubusercontent.com/devopsprodigy/kubegraf/master/kubernetes/clusterrole.yaml
# kubectl apply -f https://raw.githubusercontent.com/devopsprodigy/kubegraf/master/kubernetes/clusterrolebinding.yaml
# kubectl apply -f https://raw.githubusercontent.com/devopsprodigy/kubegraf/master/kubernetes/secret.yaml    
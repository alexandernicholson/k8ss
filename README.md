# k8ss
Listen to pods being created on your cluster. 

k8s*s* - Kubernetes sound.


## Install

```
pipenv install
```

## Run
Uses your current kube context.

```
pipenv shell

# Listen to all namespaces.
python app.py

# Listen to a specific namespace.
python app.py --namespace default
```

## License
[MIT Licence](LICENSE)

# k8ss
Listen to pods being created on your cluster. 

Uses your current kube context.

## Install
```
pipenv install
```

## Run
```
pipenv shell

# Listen to all namespaces.
python app.py

# Listen to a specific namespace.
python app.py --namespace default
```

## License
[MIT Licence](LICENSE)

run the server

```bash
flask --app app run
```

init some data

```bash
flask --app main sample-data
```

### 1. Build the image
```bash
# La commande -t (tag) permet de nommer l'image (ex: 'water-tracker-app')
docker build -t water-tracker-app .

# Build ENV #

virtualenv -p python3.8 venv

source ./venv/source/active

pip install -r pip.txt



# How TO #

## build
```bash
invoke build
```
## test
```bash
invoke test
```

## push
```bash
invoke push
```

## deploy
```bash
invoke deploy
```



**Activate the virtual environment**
```
source blockchain-env/bin/Activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**
```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual enviroment

```
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual enviroment

```
export PEER=True && python3 -m backend.app
```

**Run the frontend**

```
npm run start
```

**Seed the backend with data**
Make sure to activate the virtual enviroment
```
export SEED_DATA=True && python3 -m backend.app
```
# InfluxDB

[InfluxDB](https://www.influxdata.com/) is a time series database, often used to store sensor and meter data from buildings. Version 1 is queried with InfluxQL (SQL-like), version 2 with Flux, and version 3 with SQL or InfluxQL (Flux is not supported in version 3).

To load data from InfluxDB 1 or 2 into pandas, the package [influxdb-toolkit](https://pypi.org/project/influxdb-toolkit/) offers one call for both versions:

```python
from datetime import datetime, timedelta, timezone
from influxdb_toolkit import InfluxDBClientFactory

config = {"url": "http://localhost:8086", "token": "my-token",
          "org": "my-org", "bucket": "my-bucket"}
now = datetime.now(timezone.utc)

with InfluxDBClientFactory.get_client(version=2, config=config) as client:
    df = client.get_timeseries(
        measurement="temperature", fields=["value"],
        start=now - timedelta(days=30), end=now,
        interval="1h", aggregation="mean",   # downsampled on the server
    )
```

The result is a DataFrame that can be used with all recipes of this book. Clients are read-only by default: writing (e.g. `write_dataframe`) needs `allow_write=True` in the config or the environment variable `INFLUXDB_ALLOW_WRITE=true`. See the [influxdb-toolkit documentation](https://pypi.org/project/influxdb-toolkit/) for InfluxDB 1 connections, credentials and further methods.

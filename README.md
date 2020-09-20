# Service Monitoring

The service will check the external urls (https://httpstat.us/503 & https://httpstat.us/200 ) are up (based on http status code 200) and response time in milliseconds.
The service will run a simple http service that produces metrics using appropriate Prometheus libraries and outputs on /metrics


**Base URL:** 
http://0.0.0.0:5000/


# To check the mentioned httpstat service metrics

Exec into the pod:

`kubectl exec -it <POD_NAME> -n prometheus-metrics-vmware bash`

`curl localhost:5000/metrics`


## APIs


**Method:** GET  
 *URL:*
 ```
 /metrics
  
 *Response:*  
 
 ``` 
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 144.0
python_gc_objects_collected_total{generation="1"} 270.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 76.0
python_gc_collections_total{generation="1"} 6.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="7",patchlevel="5",version="3.7.5"} 1.0
# HELP http_request_duration_seconds Flask Request Latency
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{group="test-service-v1",le="0.005",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.01",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.025",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.05",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.075",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.1",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.25",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.5",route="https://httpstat.us/200",up="1"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.75",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="1.0",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="2.5",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="5.0",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="7.5",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="10.0",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="+Inf",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_count{group="test-service-v1",route="https://httpstat.us/200",up="1"} 1.0
http_request_duration_seconds_sum{group="test-service-v1",route="https://httpstat.us/200",up="1"} 0.7072272300720215
http_request_duration_seconds_bucket{group="test-service-v1",le="0.005",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.01",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.025",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.05",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.075",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.1",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.25",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.5",route="https://httpstat.us/503",up="0"} 0.0
http_request_duration_seconds_bucket{group="test-service-v1",le="0.75",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="1.0",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="2.5",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="5.0",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="7.5",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="10.0",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_bucket{group="test-service-v1",le="+Inf",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_count{group="test-service-v1",route="https://httpstat.us/503",up="0"} 1.0
http_request_duration_seconds_sum{group="test-service-v1",route="https://httpstat.us/503",up="0"} 0.6781148910522461
# HELP http_request_duration_seconds_created Flask Request Latency
# TYPE http_request_duration_seconds_created gauge
http_request_duration_seconds_created{group="test-service-v1",route="https://httpstat.us/200",up="1"} 1.600459481043628e+09
http_request_duration_seconds_created{group="test-service-v1",route="https://httpstat.us/503",up="0"} 1.600459481721867e+09

```

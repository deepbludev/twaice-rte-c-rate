## How to run the project:

1. Spin up infra and run the app: `docker-compose up`
2. Visit http://localhost:8000/docs to see the API docs and try it out.
3. Trigger calculation with `GET /api/v1/metrics` . You can use the file `example/data_sample.csv` ads `data` and 94 for `nominal_capacity`.
4. Use the `GET /api/v1/metrics/{task_id}` endpoint to get the results with the `task_id` from the previous response.

## Shortcomings of implementation due to the limited available time and next steps to tackle them:

* API:
  * add proper error handling
  * add proper request and response validation (ensure that the data is correct, metrics are within [0,1], etc)
  * add proper production security settings, CORS, etc
* Celery: 
  * add Flower for monitoring, 
  * use routes for tasks for proper decoupling, 
  * replace sqlite with proper production DB or use redis as a broker.
* Clean architecture:
  *  properly organize the code using infra, domain, app layers
  *  inroducing proper dependency injection
  *  move to a CQRS command/query pattern with command and query bus, handlers, etc. if more endpoints are added
* Testing: 
  * add e2e, integration, unit pytest tests
* Logging: 
  * add proper production-level logging
* Infrastructure: 
  * add k8s and terraform for deployment
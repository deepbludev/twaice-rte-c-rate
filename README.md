## How to run the project:

1. To run the project, execute the command `docker-compose up` to spin up the infrastructure and run the application.
2. Visit http://localhost:8000/docs to see the API documentation and test it out.
3. Trigger a calculation by making a request to the `POST /api/v1/metrics` endpoint, and include the data file from the `example/data_sample.csv` directory. You can use a `nominal_capacity` of 94.
4. To view the results of the calculation, use the `GET /api/v1/metrics/{task_id}` endpoint and provide the `task_id` from the previous response.

## Shortcomings of implementation due to the limited available time and next steps to tackle them:

* API:
  * Implement proper error handling to handle exceptions and provide meaningful error messages to the client.
  * Implement request and response validation to ensure that the data is correct, the metrics are within [0,1], and other such requirements are met.
  *   Implement proper security settings and CORS to protect the application and its resources.

* Celery:
  * Use Flower for monitoring Celery tasks and their performance.
  * Use Celery routes for tasks to enable proper decoupling of tasks.
  * Replace SQLite with a production-level database to ensure better scalability and data integrity.

* Clean architecture:
  * Organize the code using the infra, domain, and app layers, following the clean architecture principles to ensure that each layer has a specific responsibility and is modular and reusable.
  * Implement dependency injection to decouple components and make the application more testable and maintainable.
  * Move to a CQRS command/query pattern with command and query buses, handlers, etc., if more endpoints are added to the application.

* Testing:
  * Add pytest tests for end-to-end, integration, and unit tests to ensure the application works as expected and all the edge cases are handled.

* Logging:
  * Implement production-level logging to ensure that the application logs enough details to troubleshoot issues and monitor the application's performance and security.

* Infrastructure:
  * Implement Kubernetes and Terraform for deployment to make it easier to deploy and scale the application.




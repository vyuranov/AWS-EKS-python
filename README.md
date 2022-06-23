# AWS-EKS-python
In this repo I'll try to do next:
1) Develop simple application with python and flask. It should contain:
  - REST API with 3 endpoints (e.g. login, api, service) which answer with 3 different responses(up to you).
  - One endpoint (login) should get a token from request header and allow client to proceed communication with API. If there is no token provide 403 or 401.
2) Wrap it with container, develop dockerfiles and etc.
3) Develop helm charts for releasing this app in k8s.
4) Develop terraform modules for deploying this application into AWS cloud to EKS following all possible best practices.
5) Develop Terragrunt templates to automate all infrastructure changes process.
6) Implement Drone CI or Jenkins for CI/CD ( your app and infrastructure)

# onsites-phbk

## Documentation for onsites


### Searched
- What is ansible
- how to serve static files using nginx [Nginx documentation]
- can the sendfile directive be used in any level in nginx
- which ysql image to use in docker
-  how to load balance requests between multiple instances of a
- microservice on nginx [nginx documentation]
- how to use multiple instances of a container for load balancing in nginx
- events directive nginx docs
- [used jmeter documentation given in resources]
- what is apache jmeter
- how to configure path environment variables on linux
- how to perform load testing using apache jmeter cli
- how to setup ci cd pipeline on github for jmeter
- how to build ci cd pipeline using jenkins
- upload artifact action
- setup-java action


### ChatGPT
- Assume you have a microservices architecture with user-service, orderservice, and product-service set up with the respective dockerfiles
already. How will you integrate a database to the microservices
- what ports to give in docker compose file
- how to connect the services to the ports?
- how to setup the volume?
- use a common database for the three services
- explain the database url in the microservices
- Documentation for onsites 2
- configure an nginx to load balance the requests using multiple
- instances of the microservices
- what does the events directive do in nginx conf file
- write a script to connect microservices to mysql using nodejs
- Use a tool like Apache JMeter or Locust to perform load testing on the
deployed application.
- include the multiple instances of userservice in testfile
- explain the jmx file
- integrate this into the ci cd pipeline
- what is a connection pool?
- connect to the mysql database from the service using express instead
of sequelize
- how are you connecting it to the services?
- explain the jmeter integrated ci cd pipeline
- explain to me what ansible does
- Use Ansible to automate the provisioning and configuration of the
infrastructure required for the application, including the CI/CD pipeline
using jenkins and push the images to docker hub
### Done
- Created a github repository and cloned it to my machine
- Copied the pre existing architecture from task 2 to the new repo
- Added the root directory and autoindex on to search for static files and
serve them
- Added the try files directive with 404 error code
- Added the single common mysql container with user,order, and product
services databases within it ad connected the microservices by
replacing the mongoose to mysql
- Added multiple instances of a container with different port mappings in
the docker compose and used http upstream directive to balance the
load across the various servers
- Created and written a testplan.jmx file for apache jmeter load testing
- using 100 threads (users) and looping over each user 10 times
- The file may be executed using the cli command
``` jmeter -n -t testplan.jmx -l results.jtl -e -o output-report ```
- Integrated the jmeter load testing into the git workflows ci/cd pipeline
- looked into what jenkins is and its declarative and scripted pipeline
- added the jenkinsfile to manage the ci-cd pipeline instead of github
wokrflow actions
- created ansible directory structure with playbook, inventory and the
roles
- Added the main.yml file for the different roles [namely app_deploy,
ci_cd_setup, common, docker, jenkins]
- Made a python file and did the networking site monitoring task
- Make a flask based architecture from scratch due to node and mysql
connection error
- Connect mysql to it and add init.sql file for initialisation of the databases
- reverse proxy nginx and enable eserving static files with load balancing
using multiple instances of user container
- Added the gitlab ci pipeline file to it
- Added the testplan.jmx file for jmeter load testing
- Added the networking site monitoring task file in networking folder
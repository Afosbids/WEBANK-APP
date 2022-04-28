## WEBANK 

# PROJECT OVERVIEW

WeBank is a Web base Fintech application that allows account holders to perform credit and Debit Transactions through an Agent outlet.

[![Django CI](https://github.com/decadevs/week-9-task-python-pod-b/actions/workflows/ci.yml/badge.svg)](https://github.com/decadevs/week-9-task-python-pod-b/actions/workflows/ci.yml)


## FEATURES

#### User (client) can sign up.
#### User (client) can log in.
#### User (client) can create an account.
#### User (client) can view account transaction history.
#### User (client) can view a specific account transaction.
#### Agent/Staff can debit user (client) account.
#### Agent/Staff can credit user (client) account.
#### Agent/Staff can view all user accounts.
#### Agent/Staff can view a specific user account.
#### Agent/Staff can activate or deactivate an account.
#### Agent/Staff can delete a specific user account.
#### Admin can create and delete agent/staff and admin, user accounts.
#### User can reset password.
#### Integrate real-time email notification upon credit/debit transaction on the user account.


# Runing Docker 

#### Make sure you have docker installed on you local machine or 
download (mac with intel chip) https://www.docker.com/products/docker-desktop/
#### Drag and drop into application folder to installed
#### Run the docker app 
#### to start server in the container, run `docker-compose up` in a terminal window opened in the same directory as docker-compose.yml file
#### to stop server in the container, push `control + c` and run `docker-compose down` in a terminal window opened in the same directory as docker-compose.yml file
#### while docker-compose is down, you can run normal commands like migrate, makemigrations, createsuperuser etc like so
`sudo docker-compose run  web  python manage.py createsuperuser`





## CONTRIBUTORS
#### Akoride Olawale 
#### Olushola Afolayan
#### Nwokocha Maruche
#### Msendoo Chile
#### Sampson Kitigo

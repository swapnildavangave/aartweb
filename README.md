# AartWeb
Web based event management for Animal Adoption 'n' Rescue Team.


#### Requirements

  1. Python=>3.5
  2. Django=1.9.0
  3. django-user-accounts
  4. bootstrapform

### Steps to run the project

##### 1. Clone the repository using git or download zip and extract.
  ```sh
    git clone git@github.com:swapnildavangave/AART.git
  ```
  [download](https://codeload.github.com/swapnildavangave/AART/zip/master)

##### 2. Setup database
  1. [Docker](https://www.docker.com/)
  ```sh
    docker run --name postgresql -itd --restart always \
    --publish 5432:5432 \
    --env 'DB_USER=<user>' --env 'DB_PASS=<password>' \
    --volume /srv/docker/postgresql:/var/lib/postgresql \
    sameersbn/postgresql:9.6-2
  ```
  2. [Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
  3. [Windows](https://www.postgresql.org/download/windows/)
  4. [Mac OS](https://www.postgresql.org/download/macosx/)
##### 3. Edit AART/settings.py and update database setting variables and email setting variable .

##### 4. Run following manage.py commands.
  ```sh
  python3 manage.py migrate
  python3 manage.py collectstatic
  python3 manage.py runserver
  ```



## Tests

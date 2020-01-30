Develop Build [![CircleCI](https://circleci.com/gh/Superskyyy/iQueensu/tree/dev-deploy.svg?style=svg&circle-token=84a2db9e6a8fdb65f43579a20d0667f7d31db266)](https://circleci.com/gh/Superskyyy/iQueensu/tree/dev-deploy)
Master [![CircleCI](https://circleci.com/gh/Superskyyy/iQueensu/tree/master.svg?style=svg&circle-token=84a2db9e6a8fdb65f43579a20d0667f7d31db266)](https://circleci.com/gh/Superskyyy/iQueensu/tree/master)

[![CodeFactor](https://www.codefactor.io/repository/github/superskyyy/iqueensu/badge?s=d89136c4e9d03ccf435d607cd6186a4e16265702)](https://www.codefactor.io/repository/github/superskyyy/iqueensu)
# iQueensu
* [Frontend](https://github.com/Superskyyy/iQueensu-frontend) Portal to iQueensu - frontend repo

## Development Instructions
### Best practices
- Always push to personal branch and open a PR.
- Request review from a peer dev.
- Follow PEP 8 coding style, follow Pylint.
- Always run a test after you modify anything.
### PyLint
- Pycharm - Preference - Plugin - Marketplace 

- Search for Pylint, Install it and reboot Pycharm.
Pylint will appear as an icon in lower left corner, there's one inside VCS - Commit too.

### Testing 

#### Configurations
1. Modify settings.py in iQueensu, make sure docker is set to `True`
2. Duplicate settings_example.py to settings.py in QCumber - scraper - assets.
Fill in corresponding Queen's SSO credentials. This step is crucial to the proper running of SOLUS Scraper.
 
- To run the project in pure local env (Not recommended), set docker to False. Note you may encounter multiple errors as this method is deprecated.
#### Our project is Dockerized

- To build the source code in your local Docker
    - The docker container will automatically reflect latest change of source code.
    So don't build again, run ```> docker-compose up ``` instead.
    
    1. Clone the code, make sure docker is running
    2. Make sure the DOCKER Variable is set to True in settings.py
    3. Run following commands
        ```bash
        docker-compose run web python manage.py migrate
        
        [Windows Git Bash]> winpty docker-compose run web python manage.py createsuperuser
        
        [Unix]> docker-compose run web python manage.py createsuperuser
        
        docker-compose build
        
        docker-compose up


        ```
- To pull from remote image.. Implementing

<a name="Contributors"/><br/>
## Contributors

#### `Usernames are listed in alphabetical order`
<table>
    <tr>
       <td align="center"><a href="https://github.com/Amber201604"><img src="https://avatars0.githubusercontent.com/u/41466956?v=4" width="100px;" alt="Amber201604"/><br /><sub><b>Amber<br/> Backend <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=Amber201604" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
       <td align="center"><a href="https://github.com/EricPyZhou"><img src="https://avatars1.githubusercontent.com/u/26387900?v=4" width="100px;" alt="EricPyZhou"/><br /><sub><b>EricPyZhou <br/>Chief Frontend<br/> Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=EricPyZhou" title="Documentation">📖</a> <a href="#review-iQueensu-frontend" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
       <td align="center"><a href="https://github.com/XinyuFOX"><img src="https://avatars1.githubusercontent.com/u/41837034?v=4" width="100px;" alt="Pipi"/><br /><sub><b>皮皮Fox <br/> Frontend <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=XinyuFOX" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
      <td align="center"><a href="https://github.com/RickyZhangCA"><img src="https://avatars1.githubusercontent.com/u/16908811?v=4" width="100px;" alt="Ricky Zhang"/><br /><sub><b>Ricky Zhang <br/> Chief UI/UX <br/>Designer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=RickyZhangCA" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
      <td align="center"><a href="https://github.com/LeoZzz"><img src="https://avatars1.githubusercontent.com/u/56736269?v=4" width="100px;" alt="LeoZzz"/><br /><sub><b>LeoZzz <br/> Frontend <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=LeoZzz" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
     <td align="center"><a href="https://github.com/Somiona"><img src="https://avatars2.githubusercontent.com/u/20739885?v=4" width="100px;" alt="Somion"/><br /><sub><b>Somion <br/> Full-Stack <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=CalEIFe" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
    </tr>
</table>

## Previous Contributors

<table>
      <td align="center"><a href="https://github.com/estKey"><img src="https://avatars3.githubusercontent.com/u/38852825?v=4" width="100px;" alt="Nalsen"/><br /><sub><b>Nalsen <br/> Special Thanks <br/>Previous Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=estKey" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
</table>

# TO DO LIST: Prioritized 

Qcumber Dev


# Project Title

This is the repo of Project iQueensu, an django-react based website working along with a discourse powered forum. 

We aim to build and provide a better community for Queen's Students and Alumni.

## Getting Started


## Requirements

* [Python 3.7+](https://www.python.org/)
* `python` on the PATH

#### Optional ()

## Installing

## Deployment 

[Bash Script] - Triggered by Git Actions CI
Implementing...

#### Python path can be found by
  
```  
import sys
      
print("Python EXE : " + sys.executable)
```   

## Built With
* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.

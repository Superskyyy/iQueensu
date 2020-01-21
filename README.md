# iQueensu
Project iQueensu-backend

## Development Instructions

### PyLint
- Pycharm - Preference - Plugin - Marketplace 

- Search for Pylint, Install it and reboot Pycharm.
Pylint will appear as an icon in lower left corner, there's one inside VCS - Commit too.

### Testing 

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
              <td align="center"><a href="https://github.com/JiayingHuang"><img src="https://avatars0.githubusercontent.com/u/43382636?v=4" width="100px;" alt="Jiaying"/><br /><sub><b>Jiaying <br/> Backend <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=JiayingHuang" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
      <td align="center"><a href="https://github.com/estKey"><img src="https://avatars3.githubusercontent.com/u/38852825?v=4" width="100px;" alt="Nalsen"/><br /><sub><b>Nalsen <br/> Frontend <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=estKey" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>  
      <td align="center"><a href="https://github.com/RickyZhangCA"><img src="https://avatars1.githubusercontent.com/u/16908811?v=4" width="100px;" alt="Ricky Zhang"/><br /><sub><b>Ricky Zhang <br/> UI/UX <br/>Designer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=RickyZhangCA" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
      <td align="center"><a href="https://github.com/CalElFe"><img src="https://avatars2.githubusercontent.com/u/20739885?v=4" width="100px;" alt="Somion"/><br /><sub><b>Somion <br/> Backend <br/>Developer</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=CalEIFe" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
      <td align="center"><a href="https://github.com/MinamiKotor1"><img src="https://avatars1.githubusercontent.com/u/20905191?v=4" width="100px;" alt="Thomas"/><br /><sub><b>Thomas <br/>Backend Developer<br/>Devops</b></sub></a><br/> <a href="https://github.com/Superskyyy/iQueensu/commits?author=MinamiKotor1" title="Documentation">📖</a> <a href="#review-iQueensu" title="Reviewed Pull Requests">👀</a> <a href="#talk-iQueensu" title="Talks">📢</a></td>
    </tr>
</table>

# TO DO LIST: Prioritized 

Qcumber Dev


# Project Title

This is the repo of Project iQueensu, an django-react based website working along with a discourse powered forum. 

We aim to build and provide a better community for Queen's Students and Alumni.

## Getting Started


## Requirements

* [Python 3.6+](https://www.python.org/)
* `python` on the PATH

#### Optional ()

## Installing

## Deployment 

[Bash Script] - Triggered by Git Actions CI
Not implemented. 

#### Python path can be found by
  
```  
import sys
      
print("Python EXE : " + sys.executable)
```   

## Built With
* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.

# PROmet Website

A simple job portal/community website createad using django

## Getting Started

Make sure that you have python and pip installed. You can either create your own dockerfile to dockerize the application or just test the application by running it on the local server.

### Installing & Running 

Install the dependencies required for the project using

```python
pip install -r requirements.txt
```

To run the project locally 

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Deployment

I have a detailed blog on deploying a django application on an EC2 instance. Follow the link below:

[Hosting a Django Website on EC2](https://dev.to/waji97/hosting-a-django-website-on-ec2-part-1-4758)

Also, I have included a `Dockerfile` and a `nginx.conf` file for deploying the app on a Docker container.

## Built With

* [Django](https://docs.djangoproject.com/en/4.2/) 
* [HTML](https://devdocs.io/html/) 
* [CSS](https://devdocs.io/css/) 
* [JS](https://devdocs.io/javascript/) 
* [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Collaborators

* **Jonguk Lee** - *Project Manager* - [jongouk](https://github.com/jongouk)
* **Yena Lee** - *Front End* - [yena](https://github.com/yena)
* **Geontae Kim** - *Front End* - [kimgeontae1](https://github.com/kimgeontae1)
* **Chanho Song** - *Back End* - [hama0510](https://github.com/hama0510)



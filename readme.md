## Portfolio Blog

### Description

This is a small blog API application that I created using Python, Django, and MySql. I created this for my portfolio website so that I could have a place to post developer updates.

### Requirements

-   Python 3.7
-   Django 3.05

For other requirements, please read the requirements.txt file in the repo.

## Installation

After downloading the repo, you'll need to install any requirements necessary. You will also need to configure your database including the MySql configuration in the settings.py file.

## Usage

Since this is a very simple blog application, there are only a few routes available.

|         Route        |           URL           | METHOD |                Description               |
| :------------------: | :---------------------: | :----: | :--------------------------------------: |
|          "/"         |     <http://DOMAIN/>    |   GET  | This is the full paginated list of posts |
| "/post/&lt;int:pk>/" | <http://DOMAIN/post/ID> |   GET  |    This can be used to get a sing post   |

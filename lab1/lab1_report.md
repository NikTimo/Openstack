Author: Тимоненко Н.А. гр. К4112С, Смирнов Г.А. гр. К4113С
Lab: Lab1
# Лабораторная работа №1 Подготовка к развертыванию OpenStack
## Ход работы
1. Создание ВМ на базе alma linux3.
![img1](img/img1.png)

2. Подключение к ВМ через ssh
![img2](img/img2.png)

3. Установка git
```
sudo dnf install git -y
```
![img3](img/img3.png)

4. Клонирование проекта openstack_lab
```
git clone https://gitlab.com/itmo_samon/openstack_lab.git
```
![img4](img/img4.png)

5. Выполнить prepare.sh
```
[user@localhost openstack_lab]$ sudo ./prepare.sh
```
![img5](img/img5.png)

6. Выполнить config.sh
```
[user@localhost openstack_lab]$ sudo ./config.sh
```
![img6](img/img6.png)

7. Установить OpenStack
```
[user@localhost openstack_lab]$ sudo packstack --answer-file=answer.cfg
```
![img7](img/img7.png)

8. Данные для входа
```
[user@localhost home]$ sudo cat /root/keystonerc_admin
```
![img8](img/img8.png)

9. Загрузка данных для входа в переменные среды
```
[root@localhost ~]# source /root/keystonerc_admin
```
![img9](img/img9.png)

10. openstack endpoint list
```
[root@localhost ~]# openstack endpoint list
```
![img10](img/img10.png)

11. openstack user list
```
[root@localhost ~]# openstack user list
```
![img11](img/img11.png)

12. openstack project list
```
[root@localhost ~]# openstack project list
```
![img12](img/img12.png)

13. openstack project create --domain default --description "Demo Project" demo
```
[root@localhost ~]# openstack project create --domain default --description "Demo Project" demo
```
![img13](img/img13.png)

14. openstack project list
```
[root@localhost ~]# openstack project list
```
![img14](img/img14.png)

15. Авторизация на localhost:8080 с учетными данными admin

![img15](img/img15.png)

16-17. Создание проекта и пользователя в интерфейсе Horizon. Добавить пользователю роль в проекте.

[root@localhost ~]# openstack project list && openstack user list

![img16-1](img/img16-1.png)
![img16-2](img/img16-2.png)
![img16-3](img/img16-3.png)

18. Авторизация под созданными пользователем - виден только проект, к которому относится пользователь.

![img18-1](img/img18-1.png)
![img18-2](img/img18-2.png)

## Выводы
1. Развернута ВМ на базе образа Alma Linux 9.3
2. Настройка среды для установки Openstack
3. Установка OpenStack
4. Изучены возможности OpenStack CLI
5. Вход в Openstack через Horizon
6. Изучены способы создания проектов и пользователей
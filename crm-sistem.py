$ python manage.py startapp leads
leads
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

class Lead(models.Model):
    name = CharField("название", max_length=255)
    title = CharField("название работы", max_length=255)
    contact = CharField("Контакты", max_length=255)
    email = EmailField("Почта")
    description = TextField("описывать")
    attachment = FileField(«Приложение», upload_to="upload")
    create_time = DateTimeField(«Создание времени», auto_now_add=True)
    update_time = DateTimeField(«Последнее обновление времени», auto_now=True)

    def __str__(self):
        return self.name
      

from django.apps import AppConfig

class AppointmentsConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments'

    # # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import appointments.signals
    #
    #
    #     print('started')
    #
    #     appointment_scheduler.add_job(
    #         id='mail send',
    #         func=send_mails,
    #         trigger='interval',
    #         seconds=10,
    #     )
    #     appointment_scheduler.start()
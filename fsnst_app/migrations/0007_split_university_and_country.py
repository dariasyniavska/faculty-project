from django.db import migrations


def split_uni_country(apps, schema_editor):
    ExchangeProgram = apps.get_model('fsnst_app', 'ExchangeProgram')
    for prog in ExchangeProgram.objects.all():
        text = prog.university
        if not text:
            continue

        if '(' in text and ')' in text:
            parts = text.split('(')
            prog.university_name = parts[0].strip()
            prog.country = parts[1].replace(')', '').strip()
        elif ' - ' in text:
            parts = text.split(' - ')
            prog.university_name = parts[0].strip()
            prog.country = parts[1].strip()
        elif ',' in text:
            parts = text.split(',')
            prog.university_name = parts[0].strip()
            prog.country = parts[1].strip()
        else:
            prog.university_name = text.strip()
            prog.country = "Не вказано"

        prog.save()


def reverse_split(apps, schema_editor):
    ExchangeProgram = apps.get_model('fsnst_app', 'ExchangeProgram')
    for prog in ExchangeProgram.objects.all():
        if prog.university_name and prog.country:
            prog.university = f"{prog.university_name}, {prog.country}"
            prog.save()


class Migration(migrations.Migration):
    dependencies = [
        ('fsnst_app', '0006_exchangeprogram_country_and_more'),
    ]

    operations = [
        migrations.RunPython(split_uni_country, reverse_code=reverse_split),
    ]
from django.db import migrations

FORWARD_SQL = """
INSERT INTO fsnst_app_exchangeprogram (university, languages, slots, deadline, description) VALUES
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', 'Один із найбільших університетів Польщі з багатими академічними традиціями.'),
('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', 'Провідний європейський дослідницький центр із високими стандартами викладання.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', 'Найстаріший університет Литви з потужними програмами соціальних наук.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', 'Історичний осередок науки у Кракові з широким вибором курсів англійською.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', 'Провідний класичний університет Естонії, відомий інноваціями.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', 'Сучасний європейський університет у Брно з комфортним середовищем для обміну.');
"""

REVERSE_SQL = """
DELETE FROM fsnst_app_exchangeprogram WHERE university IN (
    'Uniwersytet Warszawski, Польща',
    'KU Leuven (Бельгія)',
    'Vilnius University, Литва',
    'Uniwersytet Jagielloński, Польща',
    'University of Tartu - Естонія',
    'Masaryk University, Чехія'
);
"""

class Migration(migrations.Migration):

    dependencies = [
        ('fsnst_app', '0004_exchangeprogram'),
    ]

    operations = [
        migrations.RunSQL(FORWARD_SQL, reverse_sql=REVERSE_SQL),
    ]
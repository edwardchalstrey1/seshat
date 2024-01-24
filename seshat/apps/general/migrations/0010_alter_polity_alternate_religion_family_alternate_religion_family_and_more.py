# Generated by Django 4.0.3 on 2023-11-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_alter_polity_alternate_religion_family_alternate_religion_family_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polity_alternate_religion_family',
            name='alternate_religion_family',
            field=models.CharField(choices=[('Saivist Traditions', 'Saivist Traditions'), ('Assyrian Religions', 'Assyrian Religions'), ('Republican Religions', 'Republican Religions'), ('Imperial Confucian Traditions', 'Imperial Confucian Traditions'), ('Shii', 'Shii'), ('Bhagavatist Traditions', 'Bhagavatist Traditions'), ('Sunni', 'Sunni'), ('Vedist Traditions', 'Vedist Traditions'), ('Saivist', 'Saivist'), ('Islam', 'Islam'), ('Chinese Folk Religion', 'Chinese Folk Religion'), ('Semitic', 'Semitic'), ('Vaisnava Traditions', 'Vaisnava Traditions'), ('Ptolemaic Religion', 'Ptolemaic Religion'), ('Vedic Traditions', 'Vedic Traditions'), ('Japanese Buddhism', 'Japanese Buddhism'), ('Orthodox', 'Orthodox'), ('Vaishnava Traditions', 'Vaishnava Traditions'), ('Shang Religion', 'Shang Religion'), ('Atenism', 'Atenism'), ('Mahayana', 'Mahayana'), ('suspected unknown', 'suspected unknown'), ('Japanese State Shinto', 'Japanese State Shinto'), ('Saiva Traditions', 'Saiva Traditions'), ('Sufi', 'Sufi'), ('Chinese Buddhist Traditions', 'Chinese Buddhist Traditions'), ('Arian', 'Arian'), ('Shia', 'Shia'), ('Catholic', 'Catholic'), ('Western Zhou Religion', 'Western Zhou Religion'), ('Imperial Cult', 'Imperial Cult'), ('Theravada', 'Theravada'), ('Seleucid Religion', 'Seleucid Religion'), ('Saivite Hinduism', 'Saivite Hinduism'), ('Theravada Buddhism', 'Theravada Buddhism'), ('Theravāda Buddhism', 'Theravāda Buddhism'), ('Protestant Christianity', 'Protestant Christianity'), ('Saivist Hinduism', 'Saivist Hinduism'), ('Sunni Islam', 'Sunni Islam'), ('Shia Islam', 'Shia Islam'), ('Vodun', 'Vodun'), ('Dahomey royal ancestor cult', 'Dahomey royal ancestor cult'), ('Shaivist', 'Shaivist'), ('Shaivism', 'Shaivism'), ('Sufi Islam', 'Sufi Islam'), ('Shaivite Hinduism', 'Shaivite Hinduism'), ('Vaishnavist Hinduism', 'Vaishnavist Hinduism'), ('Catholicism', 'Catholicism'), ('Protestant', 'Protestant'), ('Christianity', 'Christianity'), ('Vedic', 'Vedic'), ('Church of England', 'Church of England'), ('Protestantism', 'Protestantism'), ('Zoroastrianism', 'Zoroastrianism'), ('Central Asian Shamanism', 'Central Asian Shamanism'), ('Hawaiian Religion', 'Hawaiian Religion'), ('Paganism', 'Paganism')], max_length=500),
        ),
        migrations.AlterField(
            model_name='polity_language',
            name='language',
            field=models.CharField(choices=[('Pashto', 'Pashto'), ('Persian', 'Persian'), ('Greek', 'Greek'), ('Bactrian', 'Bactrian'), ('Sogdian', 'Sogdian'), ('Pahlavi', 'Pahlavi'), ('Brahmi', 'Brahmi'), ('Kharoshthi', 'Kharoshthi'), ('Tocharian', 'Tocharian'), ('Chinese', 'Chinese'), ('archaic Chinese', 'archaic Chinese'), ('Xiangxi', 'Xiangxi'), ('Qiandong', 'Qiandong'), ('Chuanqiandian', 'Chuanqiandian'), ('Hmong-Mien', 'Hmong-Mien'), ('Hmongic', 'Hmongic'), ('Middle Chinese', 'Middle Chinese'), ('Jurchen', 'Jurchen'), ('Khitan', 'Khitan'), ('Xianbei', 'Xianbei'), ('Manchu language', 'Manchu language'), ('Mongolian language', 'Mongolian language'), ('Atanque', 'Atanque'), ('Shuar', 'Shuar'), ('Arabic', 'Arabic'), ('suspected unknown', 'suspected unknown'), ('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'), ('Demotic', 'Demotic'), ('Ancient Egyptian', 'Ancient Egyptian'), ('Late Egyptian', 'Late Egyptian'), ('demotic Egyptian', 'demotic Egyptian'), ('Castilian Spanish', 'Castilian Spanish'), ('Chuukese', 'Chuukese'), ('French', 'French'), ('Langues dOil', 'Langues dOil'), ('Occitan', 'Occitan'), ('Latin', 'Latin'), ('Old Frankish', 'Old Frankish'), ('Germanic', 'Germanic'), ('Gallic', 'Gallic'), ('Gaulish', 'Gaulish'), ('English', 'English'), ('Akan', 'Akan'), ('Twi', 'Twi'), ('Doric Greek', 'Doric Greek'), ('Minoan', 'Minoan'), ('Early Greek', 'Early Greek'), ('Eteocretan', 'Eteocretan'), ('Old Hawaiian', 'Old Hawaiian'), ('Hawaiian', 'Hawaiian'), ('Iban', 'Iban'), ('Sanskrit', 'Sanskrit'), ('Old Javanese', 'Old Javanese'), ('Middle Javanese', 'Middle Javanese'), ('Javanese', 'Javanese'), ('Canaanite', 'Canaanite'), ('Aramaic', 'Aramaic'), ('Hebrew', 'Hebrew'), ('Kannada', 'Kannada'), ('Urdu', 'Urdu'), ('A’chik', 'A’chik'), ('Prakrit', 'Prakrit'), ('Telugu', 'Telugu'), ('Tamil', 'Tamil'), ('Akkadian', 'Akkadian'), ('Sumerian', 'Sumerian'), ('Amorite', 'Amorite'), ('Old Babylonian', 'Old Babylonian'), ('Mesopotamian Religions', 'Mesopotamian Religions'), ('Old Persian', 'Old Persian'), ('Elamite', 'Elamite'), ('Egyptian', 'Egyptian'), ('Old Elamite', 'Old Elamite'), ('Mongolian', 'Mongolian'), ('native Iranian languages', 'native Iranian languages'), ('Turkic', 'Turkic'), ('Turkish', 'Turkish'), ('Babylonian', 'Babylonian'), ('Hurrian', 'Hurrian'), ('Proto-Elamite', 'Proto-Elamite'), ('Old Norse', 'Old Norse'), ('Italian', 'Italian'), ('Middle Japanese', 'Middle Japanese'), ('Old Japanese', 'Old Japanese'), ('Late Old Japanese', 'Late Old Japanese'), ('Japanese', 'Japanese'), ('Early Modern Japanese', 'Early Modern Japanese'), ('Old Turkic', 'Old Turkic'), ('Iranian', 'Iranian'), ('Old Khmer', 'Old Khmer'), ('Mon', 'Mon'), ('Tai', 'Tai'), ('Khmer', 'Khmer'), ('Pali', 'Pali'), ('Phoenician', 'Phoenician'), ('Berber', 'Berber'), ('Spanish', 'Spanish'), ('Portuguese', 'Portuguese'), ('Bambara', 'Bambara'), ('Mande', 'Mande'), ('Songhay', 'Songhay'), ('Russian', 'Russian'), ('Georgian', 'Georgian'), ('Armenian', 'Armenian'), ('Kereid', 'Kereid'), ('Tatar', 'Tatar'), ('Naimans', 'Naimans'), ('Khalkha', 'Khalkha'), ('Rouran', 'Rouran'), ('Xiongnu', 'Xiongnu'), ('Oirat', 'Oirat'), ('Zapotec', 'Zapotec'), ('Icelandic', 'Icelandic'), ('Aymara', 'Aymara'), ('Puquina', 'Puquina'), ('Quechua', 'Quechua'), ('Orokaiva', 'Orokaiva'), ('unknown', 'unknown'), ('Sindhi', 'Sindhi'), ('Punjabi', 'Punjabi'), ('Sakha (Yakut)', 'Sakha (Yakut)'), ('Merotic', 'Merotic'), ('Coptic', 'Coptic'), ('Thai', 'Thai'), ('Proto-Indo-European language', 'Proto-Indo-European language'), ('Nesite', 'Nesite'), ('Luwian', 'Luwian'), ('Hattic', 'Hattic'), ('Hittite', 'Hittite'), ('Old Assyrian dialect of Akkadian', 'Old Assyrian dialect of Akkadian'), ('Indo-European language', 'Indo-European language'), ('Lydian', 'Lydian'), ('Ottoman Turkish', 'Ottoman Turkish'), ('Phrygian', 'Phrygian'), ('Miami Illinois', 'Miami Illinois'), ('Cayuga', 'Cayuga'), ('Mohawk', 'Mohawk'), ('Oneida', 'Oneida'), ('Onondaga', 'Onondaga'), ('Seneca', 'Seneca'), ('Tuscarora', 'Tuscarora'), ('Middle Mongolian', 'Middle Mongolian'), ('Ancient Iranian', 'Ancient Iranian'), ('Chagatai Turkish', 'Chagatai Turkish'), ('Sabaic', 'Sabaic'), ('Mainic', 'Mainic'), ('Qatabanic', 'Qatabanic'), ('Hadramawtic', 'Hadramawtic'), ('Old Arabic', 'Old Arabic'), ('Susu', 'Susu'), ('Koranko', 'Koranko'), ('Limba', 'Limba'), ('Temne', 'Temne'), ('Bullom', 'Bullom'), ('Loko', 'Loko'), ('Manding', 'Manding'), ('Krio', 'Krio'), ('Pulaar', 'Pulaar'), ('Kissi', 'Kissi'), ('Krim', 'Krim'), ('Vai', 'Vai'), ('Mossi', 'Mossi'), ('Shona', 'Shona'), ('Sinhala', 'Sinhala'), ('Dutch', 'Dutch'), ('Sinhalese', 'Sinhalese'), ('Oromo', 'Oromo'), ('Harari', 'Harari'), ('Argobba', 'Argobba'), ('Maay', 'Maay'), ('Somali', 'Somali'), ('Harla', 'Harla'), ('Hadiyya', 'Hadiyya'), ('Tigrinya', 'Tigrinya'), ('Funj', 'Funj'), ('Kafa', 'Kafa'), ('Yemsa', 'Yemsa'), ('Qafar', 'Qafar'), ('Proto-Yoruba', 'Proto-Yoruba'), ('Yoruba', 'Yoruba'), ('Bini', 'Bini'), ('Jukun', 'Jukun'), ('Ajagbe', 'Ajagbe'), ('Proto-Yoruboid', 'Proto-Yoruboid'), ('Sokoto', 'Sokoto'), ('Hausa', 'Hausa'), ('Idoma', 'Idoma'), ('Igbo', 'Igbo'), ('Nri', 'Nri'), ('Kanuri', 'Kanuri'), ('Kanembu', 'Kanembu'), ('Fongbe', 'Fongbe'), ('Wolof', 'Wolof'), ('Sereer', 'Sereer'), ('Fula', 'Fula'), ('Luganda', 'Luganda'), ('Kinyambo', 'Kinyambo'), ('Kinyarwanda', 'Kinyarwanda'), ('Runyankore', 'Runyankore'), ('Kirundi', 'Kirundi'), ('Fipa', 'Fipa'), ('Haya', 'Haya'), ('Old Tamil', 'Old Tamil'), ('Efik-Ibibio', 'Efik-Ibibio'), ('Hungarian', 'Hungarian'), ('Native languages', 'Native languages'), ('German', 'German'), ('Czech', 'Czech'), ('Lombardic', 'Lombardic'), ('Pukina / Puquina', 'Pukina / Puquina'), ('Old English', 'Old English'), ('Middle-Modern Persian', 'Middle-Modern Persian'), ('Anglo-Norman', 'Anglo-Norman'), ('Pictish', 'Pictish')], max_length=500),
        ),
        migrations.AlterField(
            model_name='polity_linguistic_family',
            name='linguistic_family',
            field=models.CharField(choices=[('Indo-European', 'Indo-European'), ('Sino-Tibetan', 'Sino-Tibetan'), ('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'), ('Tungusic', 'Tungusic'), ('Altaic', 'Altaic'), ('Mongolic', 'Mongolic'), ('Chibcha', 'Chibcha'), ('Chicham', 'Chicham'), ('Afro-Asiatic', 'Afro-Asiatic'), ('Oceanic-Austronesian', 'Oceanic-Austronesian'), ('Celtic', 'Celtic'), ('Niger-Congo', 'Niger-Congo'), ('Kwa', 'Kwa'), ('Hamito-Semitic', 'Hamito-Semitic'), ('Austronesian', 'Austronesian'), ('Malayo-Polynesian', 'Malayo-Polynesian'), ('Semitic', 'Semitic'), ('Indo-Iranian', 'Indo-Iranian'), ('Dravidian', 'Dravidian'), ('isolate language', 'isolate language'), ('West Semetic', 'West Semetic'), ('isolate', 'isolate'), ('suspected unknown', 'suspected unknown'), ('language isolate', 'language isolate'), ('none', 'none'), ('Germanic', 'Germanic'), ('Japonic', 'Japonic'), ('Turkic', 'Turkic'), ('Austro-Asiatic, Mon-Khmer', 'Austro-Asiatic, Mon-Khmer'), ('Austro-Asiatic', 'Austro-Asiatic'), ('unknown', 'unknown'), ('Mande', 'Mande'), ('Songhay', 'Songhay'), ('Oghuz', 'Oghuz'), ('Kartvelian', 'Kartvelian'), ('Manchu-Tungusic', 'Manchu-Tungusic'), ('Proto-Mongolic', 'Proto-Mongolic'), ('Otomanguean', 'Otomanguean'), ('Proto-Otomanguean', 'Proto-Otomanguean'), ('Mixe-Zoquean', 'Mixe-Zoquean'), ('Aymaran', 'Aymaran'), ('Quechuan', 'Quechuan'), ('Papuan Languages', 'Papuan Languages'), ('Tai-Kadai', 'Tai-Kadai'), ('Algonquian', 'Algonquian'), ('Iroquois', 'Iroquois'), ('Iranian', 'Iranian'), ('Creoles and Pidgins', 'Creoles and Pidgins'), ('Indo-Aryan', 'Indo-Aryan'), ('Yoruboid', 'Yoruboid'), ('Edoid', 'Edoid'), ('Proto-Bene-Kwa', 'Proto-Bene-Kwa'), ('Chadic', 'Chadic'), ('Saharan', 'Saharan'), ('Southern Dravidian', 'Southern Dravidian'), ('Uralic', 'Uralic'), ('Romance', 'Romance'), ('West Germanic', 'West Germanic')], max_length=500),
        ),
        migrations.AlterField(
            model_name='polity_religion_family',
            name='religion_family',
            field=models.CharField(choices=[('Saivist Traditions', 'Saivist Traditions'), ('Assyrian Religions', 'Assyrian Religions'), ('Republican Religions', 'Republican Religions'), ('Imperial Confucian Traditions', 'Imperial Confucian Traditions'), ('Shii', 'Shii'), ('Bhagavatist Traditions', 'Bhagavatist Traditions'), ('Sunni', 'Sunni'), ('Vedist Traditions', 'Vedist Traditions'), ('Saivist', 'Saivist'), ('Islam', 'Islam'), ('Chinese Folk Religion', 'Chinese Folk Religion'), ('Semitic', 'Semitic'), ('Vaisnava Traditions', 'Vaisnava Traditions'), ('Ptolemaic Religion', 'Ptolemaic Religion'), ('Vedic Traditions', 'Vedic Traditions'), ('Japanese Buddhism', 'Japanese Buddhism'), ('Orthodox', 'Orthodox'), ('Vaishnava Traditions', 'Vaishnava Traditions'), ('Shang Religion', 'Shang Religion'), ('Atenism', 'Atenism'), ('Mahayana', 'Mahayana'), ('suspected unknown', 'suspected unknown'), ('Japanese State Shinto', 'Japanese State Shinto'), ('Saiva Traditions', 'Saiva Traditions'), ('Sufi', 'Sufi'), ('Chinese Buddhist Traditions', 'Chinese Buddhist Traditions'), ('Arian', 'Arian'), ('Shia', 'Shia'), ('Catholic', 'Catholic'), ('Western Zhou Religion', 'Western Zhou Religion'), ('Imperial Cult', 'Imperial Cult'), ('Theravada', 'Theravada'), ('Seleucid Religion', 'Seleucid Religion'), ('Saivite Hinduism', 'Saivite Hinduism'), ('Theravada Buddhism', 'Theravada Buddhism'), ('Theravāda Buddhism', 'Theravāda Buddhism'), ('Protestant Christianity', 'Protestant Christianity'), ('Saivist Hinduism', 'Saivist Hinduism'), ('Sunni Islam', 'Sunni Islam'), ('Shia Islam', 'Shia Islam'), ('Vodun', 'Vodun'), ('Dahomey royal ancestor cult', 'Dahomey royal ancestor cult'), ('Shaivist', 'Shaivist'), ('Shaivism', 'Shaivism'), ('Sufi Islam', 'Sufi Islam'), ('Shaivite Hinduism', 'Shaivite Hinduism'), ('Vaishnavist Hinduism', 'Vaishnavist Hinduism'), ('Catholicism', 'Catholicism'), ('Protestant', 'Protestant'), ('Christianity', 'Christianity'), ('Vedic', 'Vedic'), ('Church of England', 'Church of England'), ('Protestantism', 'Protestantism'), ('Zoroastrianism', 'Zoroastrianism'), ('Central Asian Shamanism', 'Central Asian Shamanism'), ('Hawaiian Religion', 'Hawaiian Religion'), ('Paganism', 'Paganism')], max_length=500),
        ),
    ]

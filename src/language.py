__all__ = [ 'resolve' ]

def resolve(code):
    """
    Transform the given (2- or 3-letter) language code to a human readable
    language name.  The return value is a 2-tuple containing the given
    language code and the language name.  If the language code cannot be
    resolved, name will be 'Unknown (<code>)'.
    """
    if not code:
        return None, None
    code = code[:3]

    for spec in codes:
        if code in spec[:-1]:
            return code, spec[-1]

    return code, u'Unknown (%s)' % code


# Parsed from http://www.loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt
codes = (
   ('aar', 'aa', u'Afar'),
   ('abk', 'ab', u'Abkhazian'),
   ('ace', u'Achinese'),
   ('ach', u'Acoli'),
   ('ada', u'Adangme'),
   ('ady', u'Adyghe'),
   ('afa', u'Afro-Asiatic '),
   ('afh', u'Afrihili'),
   ('afr', 'af', u'Afrikaans'),
   ('ain', u'Ainu'),
   ('aka', 'ak', u'Akan'),
   ('akk', u'Akkadian'),
   ('alb', 'sq', u'Albanian'),
   ('ale', u'Aleut'),
   ('alg', u'Algonquian languages'),
   ('alt', u'Southern Altai'),
   ('amh', 'am', u'Amharic'),
   ('ang', u'English, Old '),
   ('anp', u'Angika'),
   ('apa', u'Apache languages'),
   ('ara', 'ar', u'Arabic'),
   ('arc', u'Official Aramaic '),
   ('arg', 'an', u'Aragonese'),
   ('arm', 'hy', u'Armenian'),
   ('arn', u'Mapudungun'),
   ('arp', u'Arapaho'),
   ('art', u'Artificial '),
   ('arw', u'Arawak'),
   ('asm', 'as', u'Assamese'),
   ('ast', u'Asturian'),
   ('ath', u'Athapascan languages'),
   ('aus', u'Australian languages'),
   ('ava', 'av', u'Avaric'),
   ('ave', 'ae', u'Avestan'),
   ('awa', u'Awadhi'),
   ('aym', 'ay', u'Aymara'),
   ('aze', 'az', u'Azerbaijani'),
   ('bad', u'Banda languages'),
   ('bai', u'Bamileke languages'),
   ('bak', 'ba', u'Bashkir'),
   ('bal', u'Baluchi'),
   ('bam', 'bm', u'Bambara'),
   ('ban', u'Balinese'),
   ('baq', 'eu', u'Basque'),
   ('bas', u'Basa'),
   ('bat', u'Baltic '),
   ('bej', u'Beja'),
   ('bel', 'be', u'Belarusian'),
   ('bem', u'Bemba'),
   ('ben', 'bn', u'Bengali'),
   ('ber', u'Berber '),
   ('bho', u'Bhojpuri'),
   ('bih', 'bh', u'Bihari'),
   ('bik', u'Bikol'),
   ('bin', u'Bini'),
   ('bis', 'bi', u'Bislama'),
   ('bla', u'Siksika'),
   ('bnt', u'Bantu '),
   ('bos', 'bs', u'Bosnian'),
   ('bra', u'Braj'),
   ('bre', 'br', u'Breton'),
   ('btk', u'Batak languages'),
   ('bua', u'Buriat'),
   ('bug', u'Buginese'),
   ('bul', 'bg', u'Bulgarian'),
   ('bur', 'my', u'Burmese'),
   ('byn', u'Blin'),
   ('cad', u'Caddo'),
   ('cai', u'Central American Indian '),
   ('car', u'Galibi Carib'),
   ('cat', 'ca', u'Catalan'),
   ('cau', u'Caucasian '),
   ('ceb', u'Cebuano'),
   ('cel', u'Celtic '),
   ('cha', 'ch', u'Chamorro'),
   ('chb', u'Chibcha'),
   ('che', 'ce', u'Chechen'),
   ('chg', u'Chagatai'),
   ('chi', 'zh', u'Chinese'),
   ('chk', u'Chuukese'),
   ('chm', u'Mari'),
   ('chn', u'Chinook jargon'),
   ('cho', u'Choctaw'),
   ('chp', u'Chipewyan'),
   ('chr', u'Cherokee'),
   ('chu', 'cu', u'Church Slavic'),
   ('chv', 'cv', u'Chuvash'),
   ('chy', u'Cheyenne'),
   ('cmc', u'Chamic languages'),
   ('cop', u'Coptic'),
   ('cor', 'kw', u'Cornish'),
   ('cos', 'co', u'Corsican'),
   ('cpe', u'Creoles and pidgins, English based '),
   ('cpf', u'Creoles and pidgins, French-based '),
   ('cpp', u'Creoles and pidgins, Portuguese-based '),
   ('cre', 'cr', u'Cree'),
   ('crh', u'Crimean Tatar'),
   ('crp', u'Creoles and pidgins '),
   ('csb', u'Kashubian'),
   ('cus', u'Cushitic '),
   ('cze', 'cs', u'Czech'),
   ('dak', u'Dakota'),
   ('dan', 'da', u'Danish'),
   ('dar', u'Dargwa'),
   ('day', u'Land Dayak languages'),
   ('del', u'Delaware'),
   ('den', u'Slave '),
   ('dgr', u'Dogrib'),
   ('din', u'Dinka'),
   ('div', 'dv', u'Divehi'),
   ('doi', u'Dogri'),
   ('dra', u'Dravidian '),
   ('dsb', u'Lower Sorbian'),
   ('dua', u'Duala'),
   ('dum', u'Dutch, Middle '),
   ('dut', 'nl', u'Dutch'),
   ('dyu', u'Dyula'),
   ('dzo', 'dz', u'Dzongkha'),
   ('efi', u'Efik'),
   ('egy', u'Egyptian '),
   ('eka', u'Ekajuk'),
   ('elx', u'Elamite'),
   ('eng', 'en', u'English'),
   ('enm', u'English, Middle '),
   ('epo', 'eo', u'Esperanto'),
   ('est', 'et', u'Estonian'),
   ('ewe', 'ee', u'Ewe'),
   ('ewo', u'Ewondo'),
   ('fan', u'Fang'),
   ('fao', 'fo', u'Faroese'),
   ('fat', u'Fanti'),
   ('fij', 'fj', u'Fijian'),
   ('fil', u'Filipino'),
   ('fin', 'fi', u'Finnish'),
   ('fiu', u'Finno-Ugrian '),
   ('fon', u'Fon'),
   ('fre', 'fr', u'French'),
   ('frm', u'French, Middle '),
   ('fro', u'French, Old '),
   ('frr', u'Northern Frisian'),
   ('frs', u'Eastern Frisian'),
   ('fry', 'fy', u'Western Frisian'),
   ('ful', 'ff', u'Fulah'),
   ('fur', u'Friulian'),
   ('gaa', u'Ga'),
   ('gay', u'Gayo'),
   ('gba', u'Gbaya'),
   ('gem', u'Germanic '),
   ('geo', 'ka', u'Georgian'),
   ('ger', 'de', u'German'),
   ('gez', u'Geez'),
   ('gil', u'Gilbertese'),
   ('gla', 'gd', u'Gaelic'),
   ('gle', 'ga', u'Irish'),
   ('glg', 'gl', u'Galician'),
   ('glv', 'gv', u'Manx'),
   ('gmh', u'German, Middle High '),
   ('goh', u'German, Old High '),
   ('gon', u'Gondi'),
   ('gor', u'Gorontalo'),
   ('got', u'Gothic'),
   ('grb', u'Grebo'),
   ('grc', u'Greek, Ancient '),
   ('gre', 'el', u'Greek, Modern '),
   ('grn', 'gn', u'Guarani'),
   ('gsw', u'Swiss German'),
   ('guj', 'gu', u'Gujarati'),
   ('gwi', u"Gwich'in"),
   ('hai', u'Haida'),
   ('hat', 'ht', u'Haitian'),
   ('hau', 'ha', u'Hausa'),
   ('haw', u'Hawaiian'),
   ('heb', 'he', u'Hebrew'),
   ('her', 'hz', u'Herero'),
   ('hil', u'Hiligaynon'),
   ('him', u'Himachali'),
   ('hin', 'hi', u'Hindi'),
   ('hit', u'Hittite'),
   ('hmn', u'Hmong'),
   ('hmo', 'ho', u'Hiri Motu'),
   ('hsb', u'Upper Sorbian'),
   ('hun', 'hu', u'Hungarian'),
   ('hup', u'Hupa'),
   ('iba', u'Iban'),
   ('ibo', 'ig', u'Igbo'),
   ('ice', 'is', u'Icelandic'),
   ('ido', 'io', u'Ido'),
   ('iii', 'ii', u'Sichuan Yi'),
   ('ijo', u'Ijo languages'),
   ('iku', 'iu', u'Inuktitut'),
   ('ile', 'ie', u'Interlingue'),
   ('ilo', u'Iloko'),
   ('ina', 'ia', u'Interlingua '),
   ('inc', u'Indic '),
   ('ind', 'id', u'Indonesian'),
   ('ine', u'Indo-European '),
   ('inh', u'Ingush'),
   ('ipk', 'ik', u'Inupiaq'),
   ('ira', u'Iranian '),
   ('iro', u'Iroquoian languages'),
   ('ita', 'it', u'Italian'),
   ('jav', 'jv', u'Javanese'),
   ('jbo', u'Lojban'),
   ('jpn', 'ja', u'Japanese'),
   ('jpr', u'Judeo-Persian'),
   ('jrb', u'Judeo-Arabic'),
   ('kaa', u'Kara-Kalpak'),
   ('kab', u'Kabyle'),
   ('kac', u'Kachin'),
   ('kal', 'kl', u'Kalaallisut'),
   ('kam', u'Kamba'),
   ('kan', 'kn', u'Kannada'),
   ('kar', u'Karen languages'),
   ('kas', 'ks', u'Kashmiri'),
   ('kau', 'kr', u'Kanuri'),
   ('kaw', u'Kawi'),
   ('kaz', 'kk', u'Kazakh'),
   ('kbd', u'Kabardian'),
   ('kha', u'Khasi'),
   ('khi', u'Khoisan '),
   ('khm', 'km', u'Central Khmer'),
   ('kho', u'Khotanese'),
   ('kik', 'ki', u'Kikuyu'),
   ('kin', 'rw', u'Kinyarwanda'),
   ('kir', 'ky', u'Kirghiz'),
   ('kmb', u'Kimbundu'),
   ('kok', u'Konkani'),
   ('kom', 'kv', u'Komi'),
   ('kon', 'kg', u'Kongo'),
   ('kor', 'ko', u'Korean'),
   ('kos', u'Kosraean'),
   ('kpe', u'Kpelle'),
   ('krc', u'Karachay-Balkar'),
   ('krl', u'Karelian'),
   ('kro', u'Kru languages'),
   ('kru', u'Kurukh'),
   ('kua', 'kj', u'Kuanyama'),
   ('kum', u'Kumyk'),
   ('kur', 'ku', u'Kurdish'),
   ('kut', u'Kutenai'),
   ('lad', u'Ladino'),
   ('lah', u'Lahnda'),
   ('lam', u'Lamba'),
   ('lao', 'lo', u'Lao'),
   ('lat', 'la', u'Latin'),
   ('lav', 'lv', u'Latvian'),
   ('lez', u'Lezghian'),
   ('lim', 'li', u'Limburgan'),
   ('lin', 'ln', u'Lingala'),
   ('lit', 'lt', u'Lithuanian'),
   ('lol', u'Mongo'),
   ('loz', u'Lozi'),
   ('ltz', 'lb', u'Luxembourgish'),
   ('lua', u'Luba-Lulua'),
   ('lub', 'lu', u'Luba-Katanga'),
   ('lug', 'lg', u'Ganda'),
   ('lui', u'Luiseno'),
   ('lun', u'Lunda'),
   ('luo', u'Luo '),
   ('lus', u'Lushai'),
   ('mac', 'mk', u'Macedonian'),
   ('mad', u'Madurese'),
   ('mag', u'Magahi'),
   ('mah', 'mh', u'Marshallese'),
   ('mai', u'Maithili'),
   ('mak', u'Makasar'),
   ('mal', 'ml', u'Malayalam'),
   ('man', u'Mandingo'),
   ('mao', 'mi', u'Maori'),
   ('map', u'Austronesian '),
   ('mar', 'mr', u'Marathi'),
   ('mas', u'Masai'),
   ('may', 'ms', u'Malay'),
   ('mdf', u'Moksha'),
   ('mdr', u'Mandar'),
   ('men', u'Mende'),
   ('mga', u'Irish, Middle '),
   ('mic', u"Mi'kmaq"),
   ('min', u'Minangkabau'),
   ('mis', u'Uncoded languages'),
   ('mkh', u'Mon-Khmer '),
   ('mlg', 'mg', u'Malagasy'),
   ('mlt', 'mt', u'Maltese'),
   ('mnc', u'Manchu'),
   ('mni', u'Manipuri'),
   ('mno', u'Manobo languages'),
   ('moh', u'Mohawk'),
   ('mol', 'mo', u'Moldavian'),
   ('mon', 'mn', u'Mongolian'),
   ('mos', u'Mossi'),
   ('mul', u'Multiple languages'),
   ('mun', u'Munda languages'),
   ('mus', u'Creek'),
   ('mwl', u'Mirandese'),
   ('mwr', u'Marwari'),
   ('myn', u'Mayan languages'),
   ('myv', u'Erzya'),
   ('nah', u'Nahuatl languages'),
   ('nai', u'North American Indian'),
   ('nap', u'Neapolitan'),
   ('nau', 'na', u'Nauru'),
   ('nav', 'nv', u'Navajo'),
   ('nbl', 'nr', u'Ndebele, South'),
   ('nde', 'nd', u'Ndebele, North'),
   ('ndo', 'ng', u'Ndonga'),
   ('nds', u'Low German'),
   ('nep', 'ne', u'Nepali'),
   ('new', u'Nepal Bhasa'),
   ('nia', u'Nias'),
   ('nic', u'Niger-Kordofanian '),
   ('niu', u'Niuean'),
   ('nno', 'nn', u'Norwegian Nynorsk'),
   ('nob', 'nb', u'Bokm\xe5l, Norwegian'),
   ('nog', u'Nogai'),
   ('non', u'Norse, Old'),
   ('nor', 'no', u'Norwegian'),
   ('nqo', u"N'Ko"),
   ('nso', u'Pedi'),
   ('nub', u'Nubian languages'),
   ('nwc', u'Classical Newari'),
   ('nya', 'ny', u'Chichewa'),
   ('nym', u'Nyamwezi'),
   ('nyn', u'Nyankole'),
   ('nyo', u'Nyoro'),
   ('nzi', u'Nzima'),
   ('oci', 'oc', u'Occitan '),
   ('oji', 'oj', u'Ojibwa'),
   ('ori', 'or', u'Oriya'),
   ('orm', 'om', u'Oromo'),
   ('osa', u'Osage'),
   ('oss', 'os', u'Ossetian'),
   ('ota', u'Turkish, Ottoman '),
   ('oto', u'Otomian languages'),
   ('paa', u'Papuan '),
   ('pag', u'Pangasinan'),
   ('pal', u'Pahlavi'),
   ('pam', u'Pampanga'),
   ('pan', 'pa', u'Panjabi'),
   ('pap', u'Papiamento'),
   ('pau', u'Palauan'),
   ('peo', u'Persian, Old '),
   ('per', 'fa', u'Persian'),
   ('phi', u'Philippine '),
   ('phn', u'Phoenician'),
   ('pli', 'pi', u'Pali'),
   ('pol', 'pl', u'Polish'),
   ('pon', u'Pohnpeian'),
   ('por', 'pt', u'Portuguese'),
   ('pra', u'Prakrit languages'),
   ('pro', u'Proven\xe7al, Old '),
   ('pus', 'ps', u'Pushto'),
   ('qaa-qtz', u'Reserved for local use'),
   ('que', 'qu', u'Quechua'),
   ('raj', u'Rajasthani'),
   ('rap', u'Rapanui'),
   ('rar', u'Rarotongan'),
   ('roa', u'Romance '),
   ('roh', 'rm', u'Romansh'),
   ('rom', u'Romany'),
   ('rum', 'ro', u'Romanian'),
   ('run', 'rn', u'Rundi'),
   ('rup', u'Aromanian'),
   ('rus', 'ru', u'Russian'),
   ('sad', u'Sandawe'),
   ('sag', 'sg', u'Sango'),
   ('sah', u'Yakut'),
   ('sai', u'South American Indian '),
   ('sal', u'Salishan languages'),
   ('sam', u'Samaritan Aramaic'),
   ('san', 'sa', u'Sanskrit'),
   ('sas', u'Sasak'),
   ('sat', u'Santali'),
   ('scc', 'sr', u'Serbian'),
   ('scn', u'Sicilian'),
   ('sco', u'Scots'),
   ('scr', 'hr', u'Croatian'),
   ('sel', u'Selkup'),
   ('sem', u'Semitic '),
   ('sga', u'Irish, Old '),
   ('sgn', u'Sign Languages'),
   ('shn', u'Shan'),
   ('sid', u'Sidamo'),
   ('sin', 'si', u'Sinhala'),
   ('sio', u'Siouan languages'),
   ('sit', u'Sino-Tibetan '),
   ('sla', u'Slavic '),
   ('slo', 'sk', u'Slovak'),
   ('slv', 'sl', u'Slovenian'),
   ('sma', u'Southern Sami'),
   ('sme', 'se', u'Northern Sami'),
   ('smi', u'Sami languages '),
   ('smj', u'Lule Sami'),
   ('smn', u'Inari Sami'),
   ('smo', 'sm', u'Samoan'),
   ('sms', u'Skolt Sami'),
   ('sna', 'sn', u'Shona'),
   ('snd', 'sd', u'Sindhi'),
   ('snk', u'Soninke'),
   ('sog', u'Sogdian'),
   ('som', 'so', u'Somali'),
   ('son', u'Songhai languages'),
   ('sot', 'st', u'Sotho, Southern'),
   ('spa', 'es', u'Spanish'),
   ('srd', 'sc', u'Sardinian'),
   ('srn', u'Sranan Tongo'),
   ('srr', u'Serer'),
   ('ssa', u'Nilo-Saharan '),
   ('ssw', 'ss', u'Swati'),
   ('suk', u'Sukuma'),
   ('sun', 'su', u'Sundanese'),
   ('sus', u'Susu'),
   ('sux', u'Sumerian'),
   ('swa', 'sw', u'Swahili'),
   ('swe', 'sv', u'Swedish'),
   ('syc', u'Classical Syriac'),
   ('syr', u'Syriac'),
   ('tah', 'ty', u'Tahitian'),
   ('tai', u'Tai '),
   ('tam', 'ta', u'Tamil'),
   ('tat', 'tt', u'Tatar'),
   ('tel', 'te', u'Telugu'),
   ('tem', u'Timne'),
   ('ter', u'Tereno'),
   ('tet', u'Tetum'),
   ('tgk', 'tg', u'Tajik'),
   ('tgl', 'tl', u'Tagalog'),
   ('tha', 'th', u'Thai'),
   ('tib', 'bo', u'Tibetan'),
   ('tig', u'Tigre'),
   ('tir', 'ti', u'Tigrinya'),
   ('tiv', u'Tiv'),
   ('tkl', u'Tokelau'),
   ('tlh', u'Klingon'),
   ('tli', u'Tlingit'),
   ('tmh', u'Tamashek'),
   ('tog', u'Tonga '),
   ('ton', 'to', u'Tonga '),
   ('tpi', u'Tok Pisin'),
   ('tsi', u'Tsimshian'),
   ('tsn', 'tn', u'Tswana'),
   ('tso', 'ts', u'Tsonga'),
   ('tuk', 'tk', u'Turkmen'),
   ('tum', u'Tumbuka'),
   ('tup', u'Tupi languages'),
   ('tur', 'tr', u'Turkish'),
   ('tut', u'Altaic '),
   ('tvl', u'Tuvalu'),
   ('twi', 'tw', u'Twi'),
   ('tyv', u'Tuvinian'),
   ('udm', u'Udmurt'),
   ('uga', u'Ugaritic'),
   ('uig', 'ug', u'Uighur'),
   ('ukr', 'uk', u'Ukrainian'),
   ('umb', u'Umbundu'),
   ('und', u'Undetermined'),
   ('urd', 'ur', u'Urdu'),
   ('uzb', 'uz', u'Uzbek'),
   ('vai', u'Vai'),
   ('ven', 've', u'Venda'),
   ('vie', 'vi', u'Vietnamese'),
   ('vol', 'vo', u'Volap\xfck'),
   ('vot', u'Votic'),
   ('wak', u'Wakashan languages'),
   ('wal', u'Walamo'),
   ('war', u'Waray'),
   ('was', u'Washo'),
   ('wel', 'cy', u'Welsh'),
   ('wen', u'Sorbian languages'),
   ('wln', 'wa', u'Walloon'),
   ('wol', 'wo', u'Wolof'),
   ('xal', u'Kalmyk'),
   ('xho', 'xh', u'Xhosa'),
   ('yao', u'Yao'),
   ('yap', u'Yapese'),
   ('yid', 'yi', u'Yiddish'),
   ('yor', 'yo', u'Yoruba'),
   ('ypk', u'Yupik languages'),
   ('zap', u'Zapotec'),
   ('zbl', u'Blissymbols'),
   ('zen', u'Zenaga'),
   ('zha', 'za', u'Zhuang'),
   ('znd', u'Zande languages'),
   ('zul', 'zu', u'Zulu'),
   ('zun', u'Zuni'),
   ('zxx', u'No linguistic content'),
   ('zza', u'Zaza'),
)

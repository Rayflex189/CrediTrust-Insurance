from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
import random
import string

def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_account_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(11))

def generate_otp():
    return ''.join(str(random.randint(0, 4)) for _ in range(6))

def generate_imf():
    return ''.join(str(random.randint(0, 4)) for _ in range(6))

def generate_aml():
    return ''.join(str(random.randint(0, 4)) for _ in range(6))

def generate_vat():
    return ''.join(str(random.randint(0, 4)) for _ in range(6))

def generate_tac():
    return ''.join(str(random.randint(0, 4)) for _ in range(6))

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    balance_after = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.user.username} - {self.timestamp}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    next_of_kin = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
        # Additional Information
    social_security_number = models.CharField(max_length=11, blank=True, null=True)
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Next of Kin Information
    next_of_kin_name = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin_phone = models.CharField(max_length=20, blank=True, null=True)
    next_of_kin_email = models.EmailField(blank=True, null=True)
    next_of_kin_relationship = models.CharField(max_length=50, blank=True, null=True)
    next_of_kin_address = models.TextField(blank=True, null=True)
    COUNTRY_CHOICES = [
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('British Virgin Islands', 'British Virgin Islands'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Cook Islands', 'Cook Islands'),
        ('Costa Rica', 'Costa Rica'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('East Timor', 'East Timor'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('French Guiana', 'French Guiana'),
        ('French Polynesia', 'French Polynesia'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Ivory Coast', 'Ivory Coast'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macau', 'Macau'),
        ('Macedonia', 'Macedonia'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Island', 'Norfolk Island'),
        ('North Korea', 'North Korea'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestinian Territory', 'Palestinian Territory'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Barthelemy', 'Saint Barthelemy'),
        ('Saint Helena', 'Saint Helena'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Martin', 'Saint Martin'),
        ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Korea', 'South Korea'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Western Sahara', 'Western Sahara'),
        ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Martin', 'Saint Martin'),
        ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Korea', 'South Korea'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    ]
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, blank=True)
    currency_choices = currency_choices = [
        ('$', 'US Dollar'),
        ('€', 'Euro'),
        ('£', 'British Pound'),
        ('¥', 'Japanese Yen'),
        ('A$', 'Australian Dollar'),
        ('C$', 'Canadian Dollar'),
        ('CHF', 'Swiss Franc'),
        ('¥', 'Chinese Yuan'),
        ('kr', 'Swedish Krona'),
        ('$', 'New Zealand Dollar'),
        ('₩', 'South Korean Won'),
        ('$', 'Singapore Dollar'),
        ('kr', 'Norwegian Krone'),
        ('$', 'Mexican Peso'),
        ('₹', 'Indian Rupee'),
        ('₽', 'Russian Ruble'),
        ('R', 'South African Rand'),
        ('R$', 'Brazilian Real'),
        ('₺', 'Turkish Lira'),
        ('$', 'Hong Kong Dollar'),
        ('Rp', 'Indonesian Rupiah'),
        ('RM', 'Malaysian Ringgit'),
        ('₱', 'Philippine Peso'),
        ('฿', 'Thai Baht'),
        ('kr', 'Danish Krone'),
        ('zł', 'Polish Zloty'),
        ('Ft', 'Hungarian Forint'),
        ('Kč', 'Czech Koruna'),
        ('₪', 'Israeli Shekel'),
        ('$', 'Chilean Peso'),
        ('E£', 'Egyptian Pound'),
        ('₴', 'Ukrainian Hryvnia'),
        ('د.إ', 'United Arab Emirates Dirham'),
        ('$', 'Argentine Peso'),
        ('ر.س', 'Saudi Riyal'),
        ('ر.ق', 'Qatari Riyal'),
        ('د.ك', 'Kuwaiti Dinar'),
        ('₦', 'Nigerian Naira'),
        ('৳', 'Bangladeshi Taka'),
        ('₫', 'Vietnamese Dong'),
        ('$', 'Colombian Peso'),
        ('lei', 'Romanian Leu'),
        ('S/', 'Peruvian Sol'),
        ('₨', 'Pakistani Rupee'),
        ('₨', 'Sri Lankan Rupee'),
        ('kn', 'Croatian Kuna'),
        ('лв', 'Bulgarian Lev'),
        ('د.ج', 'Algerian Dinar'),
        ('﷼', 'Iranian Rial'),
        ('$', 'Taiwan Dollar'),
        ('₾', 'Georgian Lari'),
        ('BYN', 'Belarusian Ruble'),
        ('₸', 'Kazakhstani Tenge'),
        ('د.م.', 'Moroccan Dirham'),
        ('Bs', 'Venezuelan Bolívar'),
        ('ብር', 'Ethiopian Birr'),
        ('Sh', 'Ugandan Shilling'),
        ('ج.س.', 'Sudanese Pound'),
        ('₨', 'Nepalese Rupee'),
        ('FCFA', 'Central African CFA Franc'),
        ('CFA', 'West African CFA Franc'),
        ('$', 'East Caribbean Dollar'),
        ('Sh', 'Tanzanian Shilling'),
        ('₵', 'Ghanaian Cedi'),
        ('Sh', 'Kenyan Shilling'),
        ('MT', 'Mozambican Metical'),
        ('Kz', 'Angolan Kwanza'),
        ('Sh', 'Ugandan Shilling'),
        ('د.ت', 'Tunisian Dinar'),
        ('ل.ل', 'Lebanese Pound'),
        ('د.أ', 'Jordanian Dinar'),
        ('Q', 'Guatemalan Quetzal'),
        ('₲', 'Paraguayan Guarani'),
        ('Bs', 'Bolivian Boliviano'),
        ('₣', 'CFP Franc'),
        ('$', 'Bahamian Dollar'),
        ('$', 'Barbadian Dollar'),
        ('$', 'Bermudian Dollar'),
        ('$', 'Fijian Dollar'),
        ('$', 'Guyanese Dollar'),
        ('$', 'Guyanese Dollar'),
        ('L', 'Honduran Lempira'),
        ('J$', 'Jamaican Dollar'),
        ('៛', 'Cambodian Riel'),
        ('с', 'Kyrgyzstani Som'),
        ('₭', 'Lao Kip'),
        ('₨', 'Sri Lankan Rupee'),
        ('Ar', 'Malagasy Ariary'),
        ('lei', 'Moldovan Leu'),
        ('ден', 'Macedonian Denar'),
        ('Ks', 'Myanmar Kyat'),
        ('MOP$', 'Macau Pataca'),
        ('₨', 'Mauritian Rupee'),
        ('Rf', 'Maldivian Rufiyaa'),
        ('MK', 'Malawian Kwacha'),
        ('$', 'Namibian Dollar'),
        ('C$', 'Nicaraguan Córdoba'),
        ('K', 'Papua New Guinean Kina'),
        ('din', 'Serbian Dinar'),
        ('₨', 'Seychellois Rupee'),
        ('£', 'Syrian Pound'),
        ('SM', 'Tajikistani Somoni'),
        ('T$', 'Tongan Paʻanga'),
        ('$', 'Trinidad and Tobago Dollar'),
        ('T', 'Turkmenistan Manat'),
        ('Sh', 'Tanzanian Shilling'),
        ('Sh', 'Ugandan Shilling'),
        ('$', 'Uruguayan Peso'),
        ('лв', 'Uzbekistani Som'),
        ('Vt', 'Vanuatu Vatu'),
        ('T', 'Samoan Tala'),
        ('FCFA', 'Central African CFA Franc'),
        ('SDR', 'Special Drawing Rights'),
        ('CFA', 'West African CFA Franc'),
        ('﷼', 'Yemeni Rial'),
        ('ZK', 'Zambian Kwacha'),
    ]

    currency = models.CharField(max_length=4, choices=currency_choices, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    working_choices = [
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Retired', 'Retired'),
        ('Student', 'Student'),
        ('Others', 'Others'),
    ]
    status = models.CharField(max_length=50, choices=working_choices, blank=True)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    Gender = models.CharField(max_length=50, choices=gender_choices, blank=True)
    account_choices = [
        ('Online Account', 'Online Account'),
        ('Checking Account', 'Checking Account'),
        ('Current Account', 'Current Account'),
        ('Corporate Account', 'Corporate Account'),
        ('Offshore Account', 'Offshore Account'),
        ('Joint Account', 'Joint Account'),
    ]
    account_type = models.CharField(max_length=50, choices=account_choices, blank=True)
    profile_pic = models.ImageField(default='d_profile.jfif', null=True, blank=True)
    account_number = models.CharField(max_length=11, default=generate_account_number)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    linking_code = models.CharField(max_length=11, default=generate_code)
    otp_code = models.CharField(max_length=11, default=generate_otp)
    imf_code = models.CharField(max_length=11, default=generate_imf)
    aml_code = models.CharField(max_length=11, default=generate_aml)
    tac_code = models.CharField(max_length=11, default=generate_tac)
    vat_code = models.CharField(max_length=11, default=generate_vat)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_linked = models.BooleanField(default=False)
    is_upgraded = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Ensure profile_picture and document are not mistakenly set to a boolean
        if isinstance(self.profile_picture, bool):
            self.profile_picture = None
        if isinstance(self.document, bool):
            self.document = None
        
        if not self.account_number:
            self.account_number = generate_account_number()
        super().save(*args, **kwargs)
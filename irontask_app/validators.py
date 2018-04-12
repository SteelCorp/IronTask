from django.core.validators import RegexValidator

phoneValidator = RegexValidator('^((\+)33|0)[1-9](\d{2}){4}', message ='Le format du téléphone est incorrect')
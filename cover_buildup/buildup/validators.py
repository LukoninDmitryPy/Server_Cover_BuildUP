from django.core.exceptions import ValidationError


def reach_value_validator(value):
    try:
        previous = value[0]
        for current in enumerate(value):
            if current != float:
                raise ValidationError(
                    f'Значение в поле reach должно быть'
                    f'десятичным(float), вы ввели: {current}'
                )
            if not 0 <= current <= 100:
                raise ValidationError(
                    f'Значение в поле reach должно'
                    f'быть от 0 до 100, вы ввели: {current}'
                )
            if previous < current:
                raise ValidationError(
                    'В списке reach, значения должны убывать'
                )

            previous = current
    except ValueError:
        raise ValidationError('Неверные данные')


def unit_value_validator(value):
    if value < 0:
        raise ValidationError(
            f'Значение в поле unit должно быть > 0, вы ввели: {value}'
        )

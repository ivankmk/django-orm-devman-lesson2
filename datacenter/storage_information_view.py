from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import pytz


def get_duration(visit):
    time_diff = timezone.now() - visit.entered_at
    return time_diff


def format_duration(duration):
    formatted_duration = str(duration).split('.')[0]
    return formatted_duration


def convert_utc_to_moscow(datatime_to_convert):
    converted_datetime = timezone.localtime(
        datatime_to_convert, pytz.timezone('Europe/Moscow'))
    return converted_datetime


def storage_information_view(request):
    persons_in_the_building = Visit.objects.filter(leaved_at=None).all()
    non_closed_visits = []
    for person in persons_in_the_building:
        non_closed_visits.append(
            {
                "who_entered": person.passcard,
                "entered_at": convert_utc_to_moscow(person.entered_at),
                "duration": format_duration(timezone.now() - person.entered_at)
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

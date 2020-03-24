from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def get_duration(visit):
    leaved_at = visit.leaved_at if visit.leaved_at else timezone.now()
    time_diff = leaved_at - visit.entered_at
    return time_diff


def is_visit_long(visit, minutes=60):
    leaved_at = visit.leaved_at if visit.leaved_at else timezone.now()
    time_in_building = leaved_at - visit.entered_at
    is_long = time_in_building.total_seconds() / 60 > minutes
    return is_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode).all()[0]
    passcard_visits = Visit.objects.filter(passcard=passcard).all()
    this_passcard_visits = []

    for visit in passcard_visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': get_duration(visit),
                'is_strange': is_visit_long(visit)
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

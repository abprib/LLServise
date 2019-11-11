from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, FormView
from django.utils.translation import gettext_lazy as _
from options.models import TimeInterval, RepeatAmount, Status
from registrations.views import UserAuthActionMixin


class UserGetMixin(object):
    model = None

    def get(self, *args, **kwargs):
        options_id = kwargs['pk']
        for option in self.model.objects.filter(pk=options_id):
            user_id = option.user.id
            if user_id != self.request.user.id:
                messages.success(self.request, _(f'Страница не найдена'))
                return HttpResponseRedirect('/')
        return super().get(self.request, *args, **kwargs)


class IntervalUpdate(SuccessMessageMixin, UserAuthActionMixin, UserGetMixin, UpdateView):
    model = TimeInterval
    template_name_suffix = '_update_form'
    fields = ['time_start', 'time_end']
    success_message = _('Интервал изменен')
    success_url = '/'


class StatusUpdate(SuccessMessageMixin, UserAuthActionMixin, UserGetMixin, UpdateView):
    model = Status
    template_name = 'options/timeinterval_update_form.html'
    fields = ['status1', 'status2', 'status3', 'status4', 'status5', 'status6', 'status7', 'status8']
    success_message = _('Статус изменен')
    success_url = '/'


class RepeatUpdate(SuccessMessageMixin, UserAuthActionMixin, UserGetMixin, UpdateView):
    model = RepeatAmount
    template_name = 'options/timeinterval_update_form.html'
    fields = ['words_per_day']
    success_message = _('Колличество повторений изменено')
    success_url = '/'




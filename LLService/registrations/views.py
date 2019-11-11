from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, FormView
from django.views.generic.base import View, TemplateView

from options.models import TimeInterval, Status, RepeatAmount
from registrations.models import User
from registrations.forms import UserRegisterForm, UserActivationRegisterForm, UserActivationForm

from django.contrib.auth import login as auth_login


class UserNotAuthMixin(UserPassesTestMixin):
    url_redirect = '/'

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return HttpResponseRedirect(self.url_redirect)


class UserAuthMixin(UserNotAuthMixin):
    warning_message = _('Для перехода по этой ссылке пожалуйста залогиньтесь.')

    def test_func(self):
        return self.request.user.is_authenticated


class UserAuthActionMixin(LoginRequiredMixin, UserPassesTestMixin):
    warning_message = _('Для перехода по этой ссылке пожалуйста подтвердите аккаунт.')
    url_redirect = reverse_lazy('auth:active')

    def test_func(self):
        return self.request.user.reg_ok

    def handle_no_permission(self):
        return HttpResponseRedirect(self.url_redirect)


class Login(SuccessMessageMixin, UserNotAuthMixin, LoginView):
    success_message = _('Вход в систему выполнен')



class Logout(UserAuthMixin, LogoutView):
    success_message = _('Вы вышли из системы')

    def get_next_page(self):
        next_page = super().get_next_page()
        if next_page:
            messages.success(self.request, self.success_message)
        return next_page


class AccountCreate(UserNotAuthMixin, SuccessMessageMixin, CreateView, PasswordResetView,):
    model = User
    extra_context = {'page_title': _('Форма регистрации')}
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')
    # url_redirect = reverse_lazy('auth:profile')
    template_name = 'registration/user_signup_form.html'
    email_template_name = 'registration/signup_email.html'
    success_message = _('Для активации аккаунта выслано письмо')


class AccountConfirm(PasswordResetConfirmView):
    """
    Activation registration
    """
    extra_context = {'page_title': _('Подтверждение регистрации')}

    success_url = reverse_lazy('auth:login')
    template_name = 'registration/signup_confirm.html'
    form_class = UserActivationRegisterForm
    post_reset_login = True
    post_reset_login_backend = 'django.contrib.auth.backends.ModelBackend'
    INTERNAL_RESET_URL_TOKEN = 'set-active'


class AccountActive(FormView):
    template_name = 'registration/activate_form.html'
    # success_url = None
    model_tag = User
    form_class_tag = UserActivationForm

    def get(self, *args, **kwargs):
        if not self.request.user.id:
            messages.success(self.request, _(f'Вам необходимо залогиниться'))
            return HttpResponseRedirect(reverse_lazy('auth:login'))
        if self.request.user.reg_ok == True:
            return HttpResponseRedirect('/')
        return super().get(self.request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.id:
            if self.request.user.reg_ok == False:
                if User.objects.get(pk=self.request.user.id).reg_key == form.cleaned_data['reg_key']:
                    User.objects.filter(pk=self.request.user.id).update(reg_ok=True)
                    TimeInterval.objects.filter(pk=self.request.user.id).create(user_id=self.request.user.id)
                    Status.objects.filter(pk=self.request.user.id).create(user_id=self.request.user.id)
                    RepeatAmount.objects.filter(pk=self.request.user.id).create(user_id=self.request.user.id)
                    messages.success(self.request, _(f'Аккаунт активирован'))

                else:
                    messages.success(self.request, _(f'Неверный пароль'))
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['form'] = self.form_class_tag()
        return kwargs


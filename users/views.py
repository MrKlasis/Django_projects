from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

import users
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.utils import restore_password


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_verify')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Подтвердите почту',
            message=f'Пройдите по ссылке http://127.0.0.1:8000/users/activate/{new_user.token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate(request, token):
    user = User.objects.get(token=token)
    user.email_verify = True
    user.save()
    return render(request, 'users/activate.html')


class RestoreView(TemplateView):
    template_name = 'users/restore.html'

    def post(self, request,  *args, **kwargs):
        context = self.get_context_data(**kwargs)
        email = self.request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except users.models.User.DoesNotExist:
            context['description'] = 'Неверный email. Попробуйте еще раз'
        else:
            new_pas = restore_password()
            user.set_password(new_pas)
            user.save()

            send_mail(
                    subject='Восстановление пароля',
                    message=f'Ваш новый пароль {new_pas}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )
            return redirect(reverse('users:login'))
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

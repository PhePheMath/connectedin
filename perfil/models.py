from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    phone = models.CharField(max_length=20, null=False)
    works_to = models.CharField(max_length=255, null=False)
    contacts = models.ManyToManyField('Profile', related_name='contacted')
    about = models.TextField(default='Hello, i\'m new to ConnectedIn')
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username

    def remove_contact(self, perfil):
        self.contacts.remove(perfil)
        perfil.contacts.remove(self)

    def allow_invitation(self, invited):
        if (self == invited):
            return False

        if (self in invited.contacts.all()):
            return False

        if Invitation.objects.intersection(invited.who_invites.all(),
                                           self.invited.all()):
            Invitation.objects.get(inviter=invited, invited=self).accept()
            return False

        if Invitation.objects.intersection(self.who_invites.all(),
                                           invited.invited.all()):
            return False

        return True

    def add_contact(self, perfil_convidado):
        perfil_convidado = Profile.objects.get(username=perfil_convidado)
        if self.allow_invitation(perfil_convidado):
            convite = Invitation(inviter=self, invited=perfil_convidado)
            convite.save()


class Invitation(models.Model):
    inviter = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                related_name='who_invites')
    invited = models.ForeignKey('Profile', on_delete=models.CASCADE,
                                related_name='invited')

    def accept(self):
        self.inviter.contacts.add(self.invited)
        self.delete()

    def deny(self):
        self.delete()

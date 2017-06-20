from django.db import models
from django.contrib.auth.models import *

class Utente(models.Model):
    user=models.OneToOneField(User)
#    usid=models.IntegerField() # per contenere l'ID di auth_user (alternativo alla riga sopra)
    livello=models.CharField(max_length=1)
    note=models.CharField(max_length=256)
    def __str__(self):
        return u"%s " %(self.user.get_username())
    class Meta:
        verbose_name_plural="Utenti"

class Menu(models.Model):
    utente=models.ForeignKey(Utente, blank=True, null=True)
#    usid=models.IntegerField() # per contenere l'ID di auth_user (alternativo alla riga sopra)
    nome=models.CharField(max_length=40, blank=True, null=True)
    data=models.DateField(blank=True, null=True)
#    giorno=models.SmallIntegerField(choices=((1,'lunedì'), (2, 'martedì'),(3, 'mercoledì'), (4, 'giovedì'), (5, 'venerdì'), (6, 'sabato'), (7, 'domenica')), blank=True, null=True)
    giorno=models.CharField(max_length=10, choices=(('Lunedì', 'lunedì'), ('Martedì', 'martedì'),('Mercoledì', 'mercoledì'), ('Giovedì', 'giovedì'), ('Venerdì', 'venerdì'), ('Sabato', 'sabato'), ('Domenica', 'domenica')), blank=True, null=True)
    righe=models.ManyToManyField('Voce',through="Riga", related_name="voci_di")
    def __str__(self):
        return u"%s %s %s %s" %(self.utente, self.nome, self.giorno, self.data)
    class Meta:
        verbose_name_plural="Menù"

class Riga(models.Model):
    menu=models.ForeignKey(Menu)
    voce=models.ForeignKey("Voce")
    quantità=models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return u"%s %s" %(self.menu, self.voce)
    class Meta:
        verbose_name_plural="Righe di menù"

class Voce(models.Model):
    nome=models.CharField(max_length=40)
    descrizione=models.CharField(max_length=256)
    tipo=models.CharField(max_length=40, blank=True, null=True, choices=(('P', 'Prodotto'), ('S', 'Semilavorato'), ('I', 'Ingrediente')))
    genere=models.CharField(max_length=40, blank=True, null=True)
    scheda=models.TextField(blank=True, null=True)
    UM=models.ForeignKey("UM")
    proprietario=models.ForeignKey(Utente, blank=True, null=True)
    ingredienti=models.ManyToManyField('self',through="Composizione", symmetrical=False, related_name="ingrediente_di")
    def __str__(self):
        return u"%s %s (%s) %s"%(self.nome, self.tipo, self.UM, self.proprietario)
    class Meta:
        verbose_name_plural="Voci"
        ordering=['nome']


class Composizione(models.Model):
    prodotto=models.ForeignKey(Voce, related_name="componenti")
    ingrediente=models.ForeignKey(Voce, related_name="parte_di")
    UnMisIngr=models.ForeignKey("UM", related_name="usata_in")
    quantitaI=models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return u"%s %s"%(self.prodotto, self.ingrediente)
    class Meta:
        verbose_name_plural="Ingredienti"


class UM(models.Model):
    nome=models.CharField(max_length=20)
    tipo=models.CharField(max_length=20, blank=True, null=True)
    corrisponde=models.ManyToManyField('self', through="Trasformatore", symmetrical=False, related_name="viene_da")
    def __str__(self):
        return u"%s"%(self.nome)
    class Meta:
        verbose_name_plural="Unità di misura"

class Trasformatore(models.Model):
    UMEntrata=models.ForeignKey(UM, related_name="a")
    UMUscita=models.ForeignKey(UM, related_name="da")
    coefficente=models.FloatField()
    def __str__(self):
        return u"%s %s"%(self.UMEntrata, self.UMUscita)
    class Meta:
        verbose_name_plural="Trasformazioni"

class Lista (models.Model):
    utente=models.ForeignKey(Utente)
    data=models.DateField(blank=True, null=True)
    stato=models.CharField(max_length=20)
    fornitore=models.CharField(max_length=100)
    def __str__(self):
        return u"%s %s"%(self.utente, self.data)
    class Meta:
        verbose_name_plural="Liste"

class Dettaglio (models.Model):
    lista=models.ForeignKey(Lista, related_name="r_dettaglio")
    articolo=models.ForeignKey(Voce)
    prezzo=models.FloatField()
    stato=models.CharField(max_length=100)
    quantità=models.FloatField()
    UMisura=models.CharField(max_length=20)
    Tot_riga=models.FloatField()
    def __str__(self):
        return u"%s %s"%(self.articolo, self.quantità)
    class Meta:
        verbose_name_plural="Righe Lista"



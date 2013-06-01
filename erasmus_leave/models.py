# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class DecyzjaOKwalifikacji(models.Model):
    
    decyzja = models.CharField(max_length=20, blank=True)
    def __unicode__(self):
        return self.decyzja
    class Meta:
        db_table = 'decyzja_o_kwalifikacji'

class DoswiadczenieZawodowe(models.Model):
    
    rodzaj = models.CharField(max_length=20, blank=True)
    firma_organizacja = models.CharField(max_length=255, blank=True)
    data = models.CharField(max_length=10, blank=True)
    kraj = models.CharField(max_length=255, blank=True)
    rodzaj2 = models.CharField(max_length=20, blank=True)
    firma_organizacja2 = models.CharField(max_length=20, blank=True)
    data2 = models.CharField(max_length=20, blank=True)
    kraj2 = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'doswiadczenie_zawodowe'

class ErazmusWyjazdPraktyka(models.Model):
    data_rozpoczecia_praktyk = models.DateField(null=True, blank=True)
    data_zakonczenia_praktyk = models.DateField(null=True, blank=True)
    kraj = models.CharField(max_length=255, blank=True)
    udostepnienie_email_i_tel = models.NullBooleanField()
    obecny_rok_studiow = models.DateField(null=True, blank=True)
    obecny_semestr_studiow = models.SmallIntegerField(null=True, blank=True)
    srednia_ocen_dwa_ost_sem = models.FloatField(null=True, blank=True)
    instutucja_przyjmujaca = models.CharField(max_length=255, blank=True)
    komisja_kwalifikuje = models.NullBooleanField(null=True, blank=True)
    szczegoly_praktyk = models.OneToOneField('SzczegolyPraktyk', null=True, blank=True)
    def __unicode__(self):
        return self.kraj +" "+ self.instutucja_przyjmujaca +" decyzja komisji:"+ self.komisja_kwalifikuje
    class Meta:
        db_table = 'erazmus_wyjazd_praktyka'

class ErazmusWyjazdStudia(models.Model):
    student = models.ForeignKey('Student', null = False, blank = True)
    wynik_egzaminu_jezykowego = models.IntegerField(null=True, blank=True)
    kraj = models.CharField(max_length=255, blank=True)
    uczelnia = models.CharField(max_length=255, blank=True)
    okres_studiow_za_granica = models.CharField(max_length=255, blank=True)
    udost_emailu_i_tel = models.NullBooleanField()
    srednia_ocen = models.FloatField()
    obecny_rok_studiow = models.DateField(null=True, blank=True)
    obecny_semestr_studiow = models.SmallIntegerField(null=True, blank=True)
    decyzja_o_kwalifikacji = models.OneToOneField(DecyzjaOKwalifikacji, null=True,blank=True)
    planowany_okres_studiow_semestr = models.CharField(max_length=20, blank=True)
    instytucja_przyjmujaca = models.ForeignKey('InstytucjaPrzyjmujaca', null=True, blank=True)
    dlaczego_chcesz_studiowac_za_granica = models.CharField(max_length=500, blank=True)
    liczba_oczekiwanych_pkt_ects = models.SmallIntegerField(null=True, blank=True)
    czas_pobytu_w_miesiacach = models.SmallIntegerField(null=True, blank=True)
    dyplom_stopen_dla_ktorego_studiuje = models.CharField(max_length=20, blank=True)
    liczba_lat_studiow_przed_wyjazdem = models.SmallIntegerField(null=True, blank=True)
    czy_studiowales_za_granica = models.NullBooleanField(null=True, blank=True)
    w_jakiej_instytucji = models.CharField(max_length=20, blank=True)
    kiedy = models.DateField(null=True, blank=True)
    czy_chcesz_ubiegac_sie_o_dotacje = models.NullBooleanField(null=True, blank=True)
    zmiany_w_programie_studiowania_za_granica = models.ForeignKey('ZmianyWProgramieStudiowaniaZaGranica', null=True, blank=True)
    class Meta:
        db_table = 'erazmus_wyjazd_studia'
    def __unicode__(self):
        return self.kraj +" "+ unicode(self.instytucja_przyjmujaca) +" decyzja komisji:"+ unicode(self.decyzja_o_kwalifikacji)



class InstytucjaPrzyjmujaca(models.Model):
    
    kraj = models.CharField(max_length=20, blank=True)
    uczelnia = models.CharField(max_length=20, blank=True)
    wstepnie_przyjety = models.NullBooleanField(null=True, blank=True)
    nie_przyjety = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = 'instytucja_przyjmujaca'
    def __unicode__(self):
        return unicode(self.uczelnia +" " +self.kraj)
    #+" wstepnie przyjety: "+self.wstepnie_przyjety + " nie przyjety " +self.nie_przyjety)


class JezykObcy(models.Model):
    
    kompetencje_jezykowe= models.ForeignKey('KompetencjeJezykowe', null=True, blank=True)
    jezyk = models.CharField(max_length=20, blank=True)
    poziom_znajomosci_jezyka = models.ForeignKey('PoziomZnajomosciJezyka', null=True, blank=True)
    studiuje_ten_jezyk = models.NullBooleanField(null=True, blank=True)
    mam_wystarczajaca_wiedze_zeby_sledzic_wyklady = models.NullBooleanField(null=True, blank=True)
    mialbym_wystarczajaca_wiedze_gdybym_mial_wiecej_przygotowania = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = 'jezyk_obcy'
    def __unicode__(self):
        return self.jezyk


class KierunekSpecjalnosc(models.Model):
    
    nazwa = models.CharField(max_length=255)
    wydzial = models.ForeignKey('Wydzial')
    class Meta:
        db_table = 'kierunek_specjalnosc'
    def __unicode__(self):
        return self.nazwa + " "+unicode(self.wydzial)


class KompetencjeJezykowe(models.Model):
    
    jezyk_ojczysty = models.CharField(max_length=255, blank=True)
    jezyk_wykladowy_na_uczelni = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'kompetencje_jezykowe'
    def __unicode__(self):
        return "jezyk ojczysty: "+self.jezyk_ojczysty + "jezyk wykladany: "+self.jezyk_wykladowy_na_uczelni


class Koordynator(models.Model):
    
    imie = models.CharField(max_length=255, blank=True)
    nazwisko = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    class Meta:
        db_table = 'koordynator'
    def __unicode__(self):
        return self.imie + " " + self.nazwisko + " "+self.email
        

class Kurs(models.Model):
    
    kod_kursu = models.CharField(max_length=10, blank=True)
    nazwa_kursu = models.CharField(max_length=20, blank=True)
    usuniecie_kursu = models.NullBooleanField(null=True, blank=True)
    dodanie_kursu = models.NullBooleanField(null=True, blank=True)
    punkty_ects = models.SmallIntegerField(null=True, blank=True)
    zmiany = models.ForeignKey('ZmianyWProgramieStudiowaniaZaGranica', null=True, blank=True)
    class Meta:
        db_table = 'kurs'
    def __unicode__(self):
        return unicode(self.kod_kursu) + " " + unicode(self.nazwa_kursu) + " "+unicode(self.punkty_ects)

class Osoba(models.Model):
    
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    pesel = models.CharField(max_length=11)
    data_urodzenia = models.DateField()
    miejsce_urodzenia = models.CharField(max_length=255)
    adres_zameldowania = models.CharField(max_length=255)
    adres_zamieszkania = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20, blank=True)
    telefon_komorkowy = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255)
    nr_dowodu_osobistego = models.CharField(max_length=20)
    zdjecie = models.ImageField(upload_to='photos', max_length=255, blank=True)
    plec = models.CharField(max_length=10)
    narodowosc = models.CharField(max_length=255, blank=True)
    termin_waznosci_adresu_zamieszkania = models.CharField(max_length=20, blank=True)
    def __unicode__(self):
        return self.imie +" "+ self.nazwisko +" "+ self.pesel
    class Meta:
        db_table = 'osoba'
        
class OsobaForm(ModelForm):
    class Meta:
        model = Osoba
#    def save(self, *args, **kwargs):
#        data = self.cleaned_data
#        return article

class PlanowaneStudiaZagraniczne(models.Model):
    
    kraj = models.CharField(max_length=20, blank=True)
    uczelnia = models.CharField(max_length=20, blank=True)
    erazmus_wyjazd = models.ForeignKey(ErazmusWyjazdStudia, null=True, blank=True)
    class Meta:
        db_table = 'planowane_studia_zagraniczne'
    def __unicode__(self):
        return self.kraj + " " + self.uczelnia + " "+unicode(self.erazmus_wyjazd)

class PoziomZnajomosciJezyka(models.Model):
    
    poziom = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'poziom_znajomosci_jezyka'
    def __unicode__(self):
        return self.poziom

class Przedmiot(models.Model):
    
    nazwa = models.CharField(max_length=20, blank=True)
    kod_przedmiotu = models.CharField(max_length=20, blank=True)
    punkty_ects = models.IntegerField(null=True, blank=True)
    semestr = models.ForeignKey('Semestr', null=True, blank=True)
    class Meta:
        db_table = 'przedmiot'
    def __unicode__(self):
        return unicode(self.nazwa) + " " + unicode(self.kod_przedmiotu) + " "+unicode(self.punkty_ects)+ " " + unicode(self.semestr)

class RokAkademicki(models.Model):
    
    rok = models.DateField(null=True, blank=True)
    wykaz_zaliczen_przedmiotow = models.ForeignKey('WykazZaliczenPrzedmiotow', null=True, blank=True)
    class Meta:
        db_table = 'rok_akademicki'
    def __unicode__(self):
        return unicode(self.wykaz_zaliczen_przedmiotow)

class Semestr(models.Model):
    
    nr_semestru = models.SmallIntegerField(null=True, blank=True)
    rok_akademicki = models.ForeignKey(RokAkademicki, null=True,  blank=True)
    class Meta:
        db_table = 'semestr'
    def __unicode__(self):
        return unicode(self.nr_semestru) + " " + unicode(self.rok_akademicki)

class Student(models.Model):
    
    osoba = models.ForeignKey(Osoba, null=True, blank=True)
    nr_indeksu = models.CharField(max_length=7)
    stopien_naukowy = models.CharField(max_length=10, blank=True)
    wydzial = models.ForeignKey('Wydzial')
    uczelnia= models.ForeignKey('Uczelnia', null=True, blank=True)
    kierunek_specjalnosc = models.ForeignKey(KierunekSpecjalnosc, null=True, blank=True)
    kompetencje_jezykowe = models.OneToOneField(KompetencjeJezykowe, null=True, blank=True)
    doswiadczenie_zawodowe = models.OneToOneField(DoswiadczenieZawodowe, null=True, blank=True)
    wykaz_zaliczen_przedmiotow = models.OneToOneField('WykazZaliczenPrzedmiotow', null=True, blank=True, related_name="wykaz_zaliczen_przedmiotow_student")
    erazmus_wyjazd_studia = models.OneToOneField(ErazmusWyjazdStudia, null=True,  blank=True, related_name="erazmus_wyjazd_studia_student")
    erazmus_wyjazd_praktyka = models.OneToOneField(ErazmusWyjazdPraktyka, null=True, blank=True,related_name="erazmus_wyjazd_praktyka_student")
    class Meta:
        db_table = 'student'
    def __unicode__(self):
        return unicode(self.osoba) + " " + self.nr_indeksu + " "+unicode(self.uczelnia) + " " + unicode(self.wydzial) + " " + unicode(self.kierunek_specjalnosc) + " " +unicode(self.kompetencje_jezykowe) + " " + unicode(self.doswiadczenie_zawodowe) + " " + unicode(self.erazmus_wyjazd_praktyka) + " " + unicode(self.erazmus_wyjazd_studia)   

class SzczegolyPraktyk(models.Model):
    
    co_chesz_osiagnoc = models.CharField(max_length=500, blank=True)
    program_praktyk = models.CharField(max_length=500, blank=True)
    zadania_praktykanta = models.CharField(max_length=500, blank=True)
    oczekiwany_minimalny_poziom_znajomosci_jezyka = models.CharField(max_length=20, blank=True)
    znajomosc_j_obcego_wystarczajaca = models.NullBooleanField(null=True, blank=True)
    korzysci_ze_studiowania_za_granica = models.CharField(max_length=500, blank=True)
    monitorowanie_i_ocena_planu = models.CharField(max_length=500, blank=True)
    erazmus_wyjazd_praktyka = models.ForeignKey(ErazmusWyjazdPraktyka, null=True, blank=True)
    class Meta:
        db_table = 'szczegoly_praktyk'

class Uczelnia(models.Model):
    
    nazwa = models.CharField(max_length=255)
    class Meta:
        db_table = 'uczelnia'
    def __unicode__(self):
        return self.nazwa
    
class Wydzial(models.Model):
    
    nazwa = models.CharField(max_length=255)
    adres = models.CharField(max_length=255, blank=True)
    uczelnia = models.ForeignKey(Uczelnia)
    telefon = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    koordynator = models.ForeignKey(Koordynator, null=True, blank=True)
    class Meta:
        db_table = 'wydzial'
    def __unicode__(self):
        return self.nazwa + " " + self.adres +  " " + unicode(self.uczelnia) +" "+ self.telefon + " "+unicode(self.koordynator)

class WykazZaliczenPrzedmiotow(models.Model):
    
    student = models.ForeignKey(Student,null = True, blank = True)
    class Meta:
        db_table = 'wykaz_zaliczen_przedmiotow'
    def __unicode__(self):
        return unicode(self.student)

class ZmianyWProgramieStudiowaniaZaGranica(models.Model):

    zatwierdzenie_przez_koordynatora = models.NullBooleanField(null=True, blank=True)
    zatwierdzenie_przez_studenta = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = 'zmiany_w_programie_studiowania_za_granica'
    def __unicode__(self):
        return unicode(self.zatwierdzenie_przez_koordynatora) + " " + unicode(self.zatwierdzenie_przez_studenta)



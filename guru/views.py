from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login as login_guru, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from user.models import User, Guru, Murid
from guru.models import Berita, Kegiatan, Video, Modul,Pengetesan, Pengajuan


# Create your views here.


def upload_berita(request):
    berita = Berita.objects.all()
    return render(request, 'uploadberita.html', {'berita':berita})


def tambah_berita(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        foto_berita = request.FILES.get('berita')

        berita = Berita(judul=judul, deskripsi=deskripsi,foto_berita=foto_berita)
        if foto_berita:
            berita.foto_berita.save(foto_berita.name, foto_berita, save=True)
        berita.save()
        return redirect('upload_berita')

    return render(request, 'berita/tambahberita.html')

def edit_berita(request, id):
    berita = Berita.objects.get(id=id)
    return render(request, 'berita/editberita.html', {'berita':berita})

def update_berita(request, id):
    berita = get_object_or_404(Berita, id=id)
    if request.method == 'POST':
        berita.judul = request.POST['judul']
        berita.deskripsi = request.POST['deskripsi']
        berita.foto_berita = request.FILES['berita']
        berita.save()
        messages.success(request,"Data Berhasil Diubah")
        return redirect('upload_berita')
    
    return render(request, 'berita/editberita.html', {'berita': berita})


def hapus_berita(request,id):
    if request.method=='POST':  
        berita = Berita.objects.get(id=id) 
        berita.delete()
    return redirect ('upload_berita')

def upload_kegiatan(request):
    kegiatan = Kegiatan.objects.all()
    return render(request, 'uploadkegiatan.html', {'kegiatan':kegiatan})

def tambah_kegiatan(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        foto_kegiatan = request.FILES.get('kegiatan')

        kegiatan = Kegiatan(judul=judul, deskripsi=deskripsi,foto_kegiatan=foto_kegiatan)
        if foto_kegiatan:
            kegiatan.foto_kegiatan.save(foto_kegiatan.name, foto_kegiatan, save=True)
        kegiatan.save()
        return redirect('upload_kegiatan')

    return render(request, 'kegiatan/tambahkegiatan.html')

def edit_kegiatan(request, id):
    kegiatan = Kegiatan.objects.get(id=id)
    return render(request, 'kegiatan/editkegiatan.html', {'kegiatan':kegiatan})

def update_kegiatan(request, id):
    kegiatan = get_object_or_404(Kegiatan, id=id)
    if request.method == 'POST':
        kegiatan.judul = request.POST['judul']
        kegiatan.deskripsi = request.POST['deskripsi']
        kegiatan.foto_kegiatan = request.FILES['kegiatan']
        kegiatan.save()
        messages.success(request,"Data Berhasil Diubah")
        return redirect('upload_kegiatan')
    
    return render(request, 'kegiatan/editkegiatan.html', {'kegiatan': kegiatan})

def hapus_kegiatan(request,id):
    if request.method=='POST':  
        kegiatan = Kegiatan.objects.get(id=id) 
        kegiatan.delete()
    return redirect ('upload_kegiatan')





def guru_dashboard(request):
    video = Video.objects.all()
    return render(request, 'materi/video.html', {'video':video})

def tambahvideomateri(request):
    if request.method == 'POST':
        materi = request.POST['materi']
        judul = request.POST['judul']
        deskripsi = request.POST['deskripsi']
        file_video = request.FILES['video']
        video = Video(judul=judul, materi=materi, deskripsi=deskripsi, file_video=file_video)
        video.save()
        return redirect('materi_video')
    return render(request, 'materi/tambahvideo.html')

def delete_video(request, id):
    if request.method=='POST':  
        video = Video.objects.get(id=id) 
        video.delete()
    return redirect("materi_video")



def modulmateri(request):
    modul = Modul.objects.all()
    return render(request, 'materi/modul.html', {'modul':modul})

def tambahvideoma(request):
    return render(request, 'soal/tambahsoal.html')


# def tingkat_murid(request):
#     tingkat = Tingkat.objects.all()
#     return render(request, 'tingkat.html', {'tingkat':tingkat})

# def tambah_tingkat(request):
#     murid = Murid.objects.all()
#     if request.method == 'POST':
#         murid_id = request.POST['nama']
#         tingkat = request.POST['tingkat']
#         try:
#             murid = Murid.objects.get(id=murid_id)
#         except (Murid.DoesNotExist, ValueError):
#             messages.warning(request, 'Murid tidak ditemukan.')
#             return redirect('tambah_tingkat')
#         muridtingkat = Tingkat(
#             murid=murid,
#             tingkat=tingkat
#         )
#         muridtingkat.save()
#         return redirect('tingkat_murid')
    
#     return render(request, 'tambahtingkat.html',{'murid':murid})

def pengetesan(request):
    pengetesan = Pengetesan.objects.all()
    return render(request, 'pengetesan.html', {'pengetesan':pengetesan})

def tambah_pengetesan(request):
    if request.method == 'POST':
        judul = request.POST['judul']
        tingkat = request.POST['tingkat']
        materi = request.POST['materi']
        url = request.POST['url']
        test = Pengetesan(judul=judul, url=url, tingkat=tingkat, materi=materi)
        test.save()
        return redirect('pengetesan')
    return render(request, 'test/tambahpengetesan.html')

def pengajuan_menghitung(request):
    pengajuan = Pengajuan.objects.all()
    return render(request, 'pengajuan_menghitung.html', {'pengajuan':pengajuan})

def setuju_pengajuan_menghitung(request, id):
    pengajuan = get_object_or_404(Pengajuan, id=id)

    if pengajuan.status == 'Menunggu Penilaian':
        pengajuan.status = 'Disetujui'
        pengajuan.save()

        if pengajuan.murid.menghitung == 'Menghitung Tingkat 1':
            pengajuan.murid.menghitung = 'Menghitung Tingkat 2'
            pengajuan.murid.save()

        elif pengajuan.murid.menghitung == 'Menghitung Tingkat 2':
            pengajuan.murid.menghitung = 'Menghitung Tingkat 3'
            pengajuan.murid.save()

    elif pengajuan.status == 'Ditolak':
        pengajuan.status = 'Disetujui'
        pengajuan.save()
        if pengajuan.murid.menghitung == 'Menghitung Tingkat 1':
            pengajuan.murid.menghitung = 'Menghitung Tingkat 2'
            pengajuan.murid.save()

        elif pengajuan.murid.menghitung == 'Menghitung Tingkat 2':
            pengajuan.murid.menghitung = 'Menghitung Tingkat 3'
            pengajuan.murid.save()

    return redirect('pengajuan_menghitung')


def tolak_pengajuan_menghitung(request, id):
    pengajuan = get_object_or_404(Pengajuan, id=id)

    if pengajuan.status == 'Menunggu Penilaian':
        pengajuan.status = 'Ditolak'
        pengajuan.save()

    elif pengajuan.status == 'Disetujui':
        pengajuan.status = 'Ditolak'
        pengajuan.save()
    return redirect('pengajuan_menghitung')


def pengajuan_membaca(request):
    pengajuan = Pengajuan.objects.all()
    return render(request, 'pengajuan_membaca.html', {'pengajuan':pengajuan})

def setuju_pengajuan_membaca(request, id):
    pengajuan = get_object_or_404(Pengajuan, id=id)

    if pengajuan.status == 'Menunggu Penilaian':
        pengajuan.status = 'Disetujui'
        pengajuan.save()

        if pengajuan.murid.membaca == 'Membaca Tingkat 1':
            pengajuan.murid.membaca = 'Membaca Tingkat 2'
            pengajuan.murid.save()

        elif pengajuan.murid.membaca == 'Membaca Tingkat 2':
            pengajuan.murid.membaca = 'Membaca Tingkat 3'
            pengajuan.murid.save()

    elif pengajuan.status == 'Ditolak':
        pengajuan.status = 'Disetujui'
        pengajuan.save()
        if pengajuan.murid.membaca == 'Membaca Tingkat 1':
            pengajuan.murid.membaca = 'Membaca Tingkat 2'
            pengajuan.murid.save()

        elif pengajuan.murid.membaca == 'Membaca Tingkat 2':
            pengajuan.murid.membaca = 'Membaca Tingkat 3'
            pengajuan.murid.save()

    return redirect('pengajuan_membaca')

def tolak_pengajuan_membaca(request, id):
    pengajuan = get_object_or_404(Pengajuan, id=id)

    if pengajuan.status == 'Menunggu Penilaian':
        pengajuan.status = 'Ditolak'
        pengajuan.save()

    elif pengajuan.status == 'Disetujui':
        pengajuan.status = 'Ditolak'
        pengajuan.save()
    return redirect('pengajuan_membaca')



def pengajuan_menulis(request):
    pengajuan = Pengajuan.objects.all()
    return render(request, 'pengajuan_menulis.html', {'pengajuan':pengajuan})

def setuju_pengajuan_menulis(request, id):
    pengajuan = get_object_or_404(Pengajuan, id=id)

    if pengajuan.status == 'Menunggu Penilaian':
        pengajuan.status = 'Disetujui'
        pengajuan.save()

        if pengajuan.murid.menulis == 'Menulis Tingkat 1':
            pengajuan.murid.menulis = 'Menulis Tingkat 2'
            pengajuan.murid.save()

        elif pengajuan.murid.menulis == 'Menulis Tingkat 2':
            pengajuan.murid.menulis = 'Menulis Tingkat 3'
            pengajuan.murid.save()

    elif pengajuan.status == 'Ditolak':
        pengajuan.status = 'Disetujui'
        pengajuan.save()
        if pengajuan.murid.menulis == 'Menulis Tingkat 1':
            pengajuan.murid.menulis = 'Menulis Tingkat 2'
            pengajuan.murid.save()

        elif pengajuan.murid.menulis == 'Menulis Tingkat 2':
            pengajuan.murid.menulis = 'Menulis Tingkat 3'
            pengajuan.murid.save()

    return redirect('pengajuan_menulis')


def tolak_pengajuan_menulis(request, id):
    pengajuan = get_object_or_404(Pengajuan, id=id)

    if pengajuan.status == 'Menunggu Penilaian':
        pengajuan.status = 'Ditolak'
        pengajuan.save()

    elif pengajuan.status == 'Disetujui':
        pengajuan.status = 'Ditolak'
        pengajuan.save()
    return redirect('pengajuan_menulis')
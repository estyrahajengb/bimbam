from django.urls import path
from menu_admin.views import *
from user.views import *
from guru.views import *
from murid.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout/',logoutuser, name='logout'),
    # user
    path('', index),
    path('index/', index),
    path('daftar/', daftar, name='daftar'),
    path('caradaftar/', caradaftar, name='caradaftar'),
    path('biodata', biodata, name='biodata'),
    path('pembayaran/', pembayaran, name='pembayaran'),
    path('pembayaran/status/', status, name='status'),
    path('tentang/', tentang, name='tentang'),
    path('pembelajaran/', pembelajaran),
    path('berita', berita, name='berita'),
    path('detailberita/<int:id>/', detailberita, name='detailberita'),
    path('kegiatan/', kegiatan, name='kegiatan'),
    path('detailkegiatan/<int:id>/', detailkegiatan, name='detailkegiatan'),
    path('kontak/', kontak, name='kontak'),

    # murid
    path('beranda/', beranda, name='beranda'),
    path('pembelajaran/materi', materi, name='materimurid'),
    path('status_tingkat_menghitung', status_tingkat_menghitung, name='status_tingkat_menghitung'),
    path('status_tingkat_membaca', status_tingkat_membaca, name='status_tingkat_membaca'),
    path('status_tingkat_menulis', status_tingkat_menulis, name='status_tingkat_menulis'),
    path('pembelajaran/level', level, name='levelmurid'),
    path('.berita', beritamurid, name='beritamurid'),
    path('.kontak', kontakmurid, name='kontakmurid'),
    path('.kegiatan', kegiatanmurid , name='kegiatanmurid'),
    path('.tentang', tentangmurid, name='tentangmurid'),
    path('pengetesan_murid', pengetesan_murid, name='pengetesan_murid'),
    path('detail_berita_murid/<int:id>/', detailberitamurid, name='detailberitamurid'),
    path('detail_kegiatan_murid/<int:id>/', detailkegiatanmurid, name='detailkegiatanmurid'),

    # guru
    path('guruku', guru_dashboard, name="guruku"),
    path('uploadberita', upload_berita, name="upload_berita"),
    path('uploadkegiatan', upload_kegiatan, name="upload_kegiatan"),
    path('tambah_berita', tambah_berita, name="tambah_berita"),
    path('tambah_kegiatan', tambah_kegiatan, name="tambah_kegiatan"),
    path('pengetesan', pengetesan, name="pengetesan"),

    path('pengajuan_menghitung', pengajuan_menghitung, name="pengajuan_menghitung"),
    path('setuju_pengajuan_menghitung/<int:id>/', setuju_pengajuan_menghitung, name='setuju_pengajuan_menghitung'),
    path('tolak_pengajuan_menghitung/<int:id>/', tolak_pengajuan_menghitung, name='tolak_pengajuan_menghitung'),
    
    path('pengajuan_membaca', pengajuan_membaca, name="pengajuan_membaca"),
    path('setuju_pengajuan_membaca/<int:id>/', setuju_pengajuan_membaca, name='setuju_pengajuan_membaca'),
    path('tolak_pengajuan_membaca/<int:id>/', tolak_pengajuan_membaca, name='tolak_pengajuan_membaca'),

    path('pengajuan_menulis', pengajuan_menulis, name="pengajuan_menulis"),
    path('setuju_pengajuan_menulis/<int:id>/', setuju_pengajuan_menulis, name='setuju_pengajuan_menulis'),
    path('tolak_pengajuan_menulis/<int:id>/', tolak_pengajuan_menulis, name='tolak_pengajuan_menulis'),

    path('tambah_pengetesan', tambah_pengetesan, name="tambah_pengetesan"),
    path('edit/kegiatan/<int:id>', edit_kegiatan, name='edit_kegiatan'),  
    path('edit/berita/<int:id>', edit_berita, name='edit_berita'),  
    path('update/kegiatan/<int:id>/', update_kegiatan, name='update_kegiatan'), 
    path('update/berita/<int:id>/', update_berita, name='update_berita'), 
    path('delete/berita/<int:id>/', hapus_berita, name="hapus_berita"),
    path('delete/kegiatan/<int:id>/', hapus_kegiatan, name="hapus_kegiatan"),

    path('tambah_video1', tambahvideomateri, name="tambah_video1"),
    path('delete/video/<int:id>/', delete_video, name='delete_video'),

    path('materi_modul', modulmateri, name="materi_modul"),
    # path('tingkat_murid', tingkat_murid, name="tingkat_murid"),
    # path('tambah_tingkat', tambah_tingkat, name="tambah_tingkat"),

    # admin
    path('admin/', admin, name='admin'),

    # kelolamurid
    path('murid', murid, name='murid'),
    path('tambah/murid/', tambahmurid, name='tambahmurid'),
    path('delete/murid/<int:id>/', destroymurid, name='destroy'),
    path('edit/murid/<int:id>', edit, name='edit'),  
    path('update/murid/<int:id>/', update_murid, name='update'), 

    # kelolaguru
    path('guru', guruku, name='guru'),
    path('tambah/guru/', tambahguru, name='tambahguru'),
    path('delete/guru/<int:id>/', hapusguru, name='hapusguru'),
    path('edit/guru/<int:id>/', editguru, name='editguru'),
    path('update/guru/<int:id>/', updateguru, name='updatesguru'),

    # kelolauser
    path('user', user, name='user'),
    path('tambah/user/', tambahuser, name='tambahuser'),
    path('delete/user/<int:id>/', hapususer, name='hapususer'),
    path('edit/user/<int:id>/', edituser, name='edituser'), 
    path('update/user/<int:id>/', updateuser, name='updatesuser'),

    # kelolatransaksi
    path('transaksi', transaksi, name='transaksi'),
    path('setuju/<str:id_pembayaran>/', setuju, name='setuju'),
    path('tolak/<str:id_pembayaran>/', tolak, name='tolak'),
    path('delete/user/<int:id>/', hapususer, name='hapususer'),
    path('edit/user/<int:id>/', edituser, name='edituser'),
    path('update/user/<int:id>/', updateuser, name='updatesuser'),

    path('laporan/', laporan, name='laporan'),
    path('laporan-transaksi/', generate_laporan, name='laporan_transaksi'),

    path('pengetesan/menghitung/<str:tingkat>/', pengetesan_murid_menghitung, name='pengetesan_murid_menghitung'),
    path('pengetesan/membaca/<str:tingkat>/', pengetesan_murid_membaca, name='pengetesan_murid_membaca'),
    path('pengetesan/menulis/<str:tingkat>/', pengetesan_murid_menulis, name='pengetesan_murid_menulis'),

    path('membaca/<str:tingkat>/', membaca, name='membaca'),
    path('menghitung/<str:tingkat>/', menghitung, name='menghitung'),
    path('menulis/<str:tingkat>/', menulis, name='menulis'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

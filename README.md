# hdu_school_library_auto
30 00 * * *root reboot  </br>
00 20 * * */usr/bin/python3 -u /root/library.py > /root/library.out 2>&1 &  </br>  </br>
31 08 * * */usr/bin/python3 -u /root/cheakin.py >/root/cheakin.out 2>&1 &  </br>  </br>  </br>



Ctrl+x  </br>
crontab -l  </br>
crontab -e </br>

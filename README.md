# Project linksys wrt54g v7

## Analizing the hardware

Lets analize the hardeware for the 'linksys wrt54g v7'

When we take look at the pcb, we can see some chips.


Manufactor | Type | purspose
--- | --- | ---
Atheros | AR2317-AC14 | SOC, system on chip
Infineon | ADM6996I | Network Controler
Hynix | HY57V641620ETP-H | DRAM chip
MX | 25L1605AMC | Flash chip


## Hooking up some wires


On the PCB there are some holes, where you can solder some pins into.

![alt text][PCB]

[PCB]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/pcb-jp1.jpg "PCB"

Connect the device with some jumperwires and a serial2uart (for example a ftdi232) adapter to a computer. 

Below is the output of the captured bootlog from the device.


```
ar531xPlus rev 0x00000090 firmware startup...
SDRAM NOT TEST


WRT54G version 4.1.2.56SP4


 1
 0

auto-booting...

Attaching to TFFS... done.
Loading /fl/ap61.sys...956368
Starting at 0x80480684...


                                                            

/fl/  - Volume is OK 
Attaching interface lo0...done

Ready unit=0


 ********** Disable sysWatchdog ***************



 ++++++++++++ IP attach interface ++++++++++  

 Start Initial MEM Drv size:0x1fe00
Copy OK: 28261 bytes copied
FlshFormatFileSystem: Invalid Filesys ID -1
 vxBitsInit 
!!!!!!!!!!!!!!Find Interface mirror0 
!!!!!!!!!!!!!!Find Interface ae1 


WAN Initialisation                                 [SUCCESS]

PPPoE Initialised

 PPTP Initialised

 L2TP Initialization success FW initalized


 ** before calling dhcpc http register function ** 

TFTPDstandard_tftp_server launched on port :Initializatinion ok ..........69.....

.
IGWIpRsmInit():  ....End


 Initialising UPnP Stack DEBUG: IGWHttpServStart: server is now running 


  UPnP Stack InitialisedIGWUPNLdSvInit 54



  IGWIGDLoadAndSaveInit: success 

../../ldsvcbk/firewall/kukildsv.c(76): FWCookieLdsvInit: SUCCESS


Loading the databases......

 ======================= Set IP Address state 0 
 ======================= Set Boardcast Address state 0 
Loading RIP configuration records - success.

Loaded RIP database

DNSRDLoad Done
DNSRDLoadSysDName Done

Firewall load database completed Loaded Security database

 IGWIGD: Loading data 

lTotalRecs is 1

IGWIGDSetIface: IGWUpnpGetIfaceInfo failure

 IGWIGDLoadEnable :lTotalRecs is 1

  UPnPPeriodicAdver0xtiseRestart: Start805f8190ing Advts. 
 (
strt

  IGWIGDLoad:  ): IGWIGDLoad() succarp_rtrequest: bad gateway valueess 

 IGWUPN: Loading data 

IGWUPNLoadData 74

IGWUPNLoadHostRec 270

IGWUPNLoadServRec 356


IGWUPNLoadServRec: DbGetRecordInfo Failed 

 Already login from internal n/w is enabled 

Httpd_Register_TagArray

Httpd_Register_TagArray

Httpd_Register_TagArray

**********Registration of local tags succesful for DMZHostConfig



 ********** Ensable sysWatchdog ***************

IGWIGDSetIface: IGWUpnpGetIfaceInfo failure


ROUTE NET TABLE
destination      gateway              flags  Refcnt  Use           Interface
----------------------------------------------------------------------------
0.0.0.0          0.0.0.0              101    0       0             ae1
192.168.1.0      192.168.1.1          101    0       0             mirror0
----------------------------------------------------------------------------

ROUTE HOST TABLE
destination      gateway              flags  Refcnt  Use           Interface
----------------------------------------------------------------------------
127.0.0.1        127.0.0.1            5      1       3             lo0
239.255.255.250  192.168.1.1          5      0       0             mirror0
----------------------------------------------------------------------------

Listing Directory /fl:
-rwxrwxrwx  1 0       0           956756 Jan  1 02:13 ap61.sys 
-rwxrwxrwx  1 0       0           224664 Jan  1 02:13 igwhtm.dat 
-rwxrwxrwx  1 0       0            28528 Jan  1 02:13 langpak_en 
-rwxrwxrwx  1 0       0            28261 Jan  1 01:00 igwpricf.dat 
-rwxrwxrwx  1 0       0             3600 Jan  1 01:00 nvram.cfg 
-rwxrwxrwx  1 0       0             2046 Dec 24  2001 calibra.dat 

/fl/  - disk check in progress ...

/fl/ap61.sys
/fl/igwhtm.dat
/fl/langpak_en 
/fl/igwpricf.dat
/fl/nvram.cfg    
/fl/calibra.dat
                                                            

/fl/  - Volume is OK 

	  total # of clusters:	2,819
	   # of free clusters:	385
	    # of bad clusters:	0
	     total free space:	197,120
     max contiguous free space:  197,120 bytes
		   # of files:	6
		 # of folders:	0
	 total bytes in files:	1,214 Kb
	     # of lost chains:	0
   total bytes in lost chains:  0

FREE LIST:
  num     addr      size
  --- ---------- ----------
    1 0x805f4d40      13872
    2 0x805f4aa0         32
    3 0x805e8180      50736
    4 0x80510520        192
    5 0x803dd2a0     242896


SUMMARY:
 status   bytes    blocks   avg block  max block
 ------ --------- -------- ---------- ----------
current
   free    307728        5      61545    242896
  alloc   4009248     2345       1709        -
cumulative
  alloc   4475216    11055        404        -

```



## Dumping the firmware

Before we can dump the firm, we must remove the flashchip. This can be done with a SMD Reworkstation

![alt text][flashchip1]
![alt text][flashchip3]
![alt text][flashchip2]

Now, lets dump the firmware from the flashchip

![alt text][flashchip4]

We can dump the firmware with a programmer. 
In this example i use a RT809h.

![alt text][flashchip5]

[flashchip1]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/flashchip1.jpg "Flashchip"
[flashchip2]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/flashchip2.jpg "Flashchip"
[flashchip3]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/flashchip3.jpg "Flashchip"
[flashchip4]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/flashchip4.jpg "Flashchip"
[flashchip5]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/screen.png "Flashchip"


## Analizing the firmware

Before taking a look at the fireware, lets use binwalker to see what we've got.


```
$ binwalk MX25L1605A_SOIC16_20200124_185531.BIN 


DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1280          0x500           Copyright string: "Copyright 2003-2004 Atheros Communications, Inc."
25118         0x621E          Unix path: /depot/sw/releases/4.0/src/ap/os/vxworks/target/config/ar531xPlus/ar531xPlus.h#1 $
25216         0x6280          VxWorks operating system version "5.4.2" , compiled: "Apr 26 2006, 17:10:39"
25920         0x6540          Copyright string: "Copyright 1984-1996 Wind River Systems, Inc."
26769         0x6891          Zlib compressed data, default compression
396320        0x60C20         gzip compressed data, has original file name: "lastpassword.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:01
396516        0x60CE4         gzip compressed data, has original file name: "Log.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
407350        0x63736         gzip compressed data, has original file name: "md5.js", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:01
409222        0x63E86         gzip compressed data, has original file name: "OutLog.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
410060        0x641CC         gzip compressed data, has original file name: "ping.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:01
411657        0x64809         GIF image data, version "87a", 82 x 44
412973        0x64D2D         GIF image data, version "89a", 82 x 44
414264        0x65238         gzip compressed data, has original file name: "ptrigger.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
418596        0x66324         gzip compressed data, has original file name: "qos.htm", from NTFS filesystem (NT), last modified: 2006-04-12 06:01:16
424626        0x67AB2         HTML document header
666385        0xA2B11         HTML document footer
666398        0xA2B1E         gzip compressed data, has original file name: "reset.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:01
667731        0xA3053         gzip compressed data, has original file name: "Routing.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
672961        0xA44C1         gzip compressed data, has original file name: "RTable.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
673859        0xA4843         gzip compressed data, has original file name: "Service.htm", from NTFS filesystem (NT), last modified: 2006-04-26 03:11:33
676374        0xA5216         GIF image data, version "89a", 50 x 50
677361        0xA55F1         gzip compressed data, has original file name: "StaLan.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:13
682871        0xA6B77         gzip compressed data, has original file name: "StaRouter.htm", from NTFS filesystem (NT), last modified: 2006-04-25 06:39:04
687832        0xA7ED8         gzip compressed data, has original file name: "StaWlan.htm", from NTFS filesystem (NT), last modified: 2006-04-04 06:45:18
694279        0xA9807         gzip compressed data, has original file name: "summary.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:13
695913        0xA9E69         gzip compressed data, has original file name: "sysinfo.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:03
696126        0xA9F3E         gzip compressed data, has original file name: "Traceroute.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:03
697558        0xAA4D6         GIF image data, version "89a", 165 x 57
702087        0xAB687         GIF image data, version "89a", 613 x 33
703042        0xABA42         GIF image data, version "89a", 160 x 33
703523        0xABC23         GIF image data, version "89a", 8 x 13
703608        0xABC78         GIF image data, version "87a", 15 x 19
703768        0xABD18         GIF image data, version "89a", 41 x 8
703881        0xABD89         GIF image data, version "89a", 67 x 8
703963        0xABDDB         GIF image data, version "89a", 773 x 11
704749        0xAC0ED         GIF image data, version "89a", 176 x 64
707313        0xACAF1         gzip compressed data, has original file name: "Unauthorized.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:03
707457        0xACB81         gzip compressed data, has original file name: "Upgrade.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:13
713322        0xAE26A         gzip compressed data, has original file name: "UpgStat.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:03
713876        0xAE494         gzip compressed data, has original file name: "UpLangPak.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:13
715273        0xAEA09         gzip compressed data, has original file name: "VPN.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:13
720710        0xAFF46         gzip compressed data, has original file name: "WAdv.htm", from NTFS filesystem (NT), last modified: 2006-05-04 12:03:22
738304        0xB4400         TROC filesystem, 16777216 file entries
738358        0xB4436         Copyright string: "Copyright Intoto, Inc"
748032        0xB6A00         TROC filesystem, 1509949440 file entries
750717        0xB747D         gzip compressed data, has original file name: "apply.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
751463        0xB7767         gzip compressed data, has original file name: "apply1.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
752447        0xB7B3F         gzip compressed data, has original file name: "apply2.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
753080        0xB7DB8         gzip compressed data, has original file name: "apply2sec.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
754064        0xB8190         gzip compressed data, has original file name: "apply3.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
754969        0xB8519         gzip compressed data, has original file name: "applyW.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
755714        0xB8802         gzip compressed data, has original file name: "bad.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
756236        0xB8A0C         gzip compressed data, has original file name: "basic.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
770564        0xBC204         Microsoft executable, MS-DOS
777728        0xBDE00         ELF, 32-bit MSB MIPS-II executable, MIPS, version 1 (SYSV)
1212804       0x128184        Microsoft executable, MS-DOS
1235456       0x12DA00        TROC filesystem, 16777216 file entries
1235510       0x12DA36        Copyright string: "Copyright Intoto, Inc"
1443096       0x160518        gzip compressed data, has original file name: "bkconfig.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:54
1446084       0x1610C4        gzip compressed data, has original file name: "ChgLan.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:56
1446784       0x161380        gzip compressed data, has original file name: "common.js", from NTFS filesystem (NT), last modified: 2006-04-25 06:38:55
1449139       0x161CB3        gzip compressed data, has original file name: "Cysaja.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:56
1449351       0x161D87        gzip compressed data, has original file name: "DDNS.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:10
1453432       0x162D78        gzip compressed data, has original file name: "DEVICE.HTM", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:57
1454488       0x163198        gzip compressed data, has original file name: "DHCPTable.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:10
1455718       0x163666        gzip compressed data, has original file name: "Diag.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:11
1458668       0x1641EC        gzip compressed data, has original file name: "DMZ.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:11
1464191       0x16577F        gzip compressed data, has original file name: "ERRSCRN.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:57
1464760       0x1659B8        gzip compressed data, has original file name: "FacDef.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:11
1467784       0x166588        gzip compressed data, has original file name: "FilterMac.htm", from NTFS filesystem (NT), last modified: 2006-04-18 14:57:51
1469843       0x166D93        gzip compressed data, has original file name: "Filters.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:11
1475591       0x168407        gzip compressed data, has original file name: "Firewall.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:11
1478835       0x1690B3        gzip compressed data, has original file name: "Forward.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
1483289       0x16A219        gzip compressed data, has original file name: "HDDNS.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:58
1484447       0x16A69F        gzip compressed data, has original file name: "HDefault.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:58
1485350       0x16AA26        gzip compressed data, has original file name: "HDMZ.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:58
1486347       0x16AE0B        gzip compressed data, has original file name: "HFilters.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:59
1489763       0x16BB63        gzip compressed data, has original file name: "HFirewall.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:59
1490726       0x16BF26        gzip compressed data, has original file name: "HForward.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:59
1491759       0x16C32F        gzip compressed data, has original file name: "HLog.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:04:59
1492625       0x16C691        gzip compressed data, has original file name: "HMAC.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1493659       0x16CA9B        gzip compressed data, has original file name: "HManage.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1494664       0x16CE88        gzip compressed data, has original file name: "HRouting.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1495964       0x16D39C        gzip compressed data, has original file name: "HSetup.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1497500       0x16D99C        gzip compressed data, has original file name: "HStatus.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1498875       0x16DEFB        gzip compressed data, has original file name: "HUpgrade.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1499947       0x16E32B        gzip compressed data, has original file name: "HVPN.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:00
1500900       0x16E6E4        gzip compressed data, has original file name: "HWEP.htm", from NTFS filesystem (NT), last modified: 2006-03-29 07:02:26
1502713       0x16EDF9        gzip compressed data, has original file name: "HWireless.htm", from NTFS filesystem (NT), last modified: 2006-03-29 07:02:27
1504189       0x16F3BD        gzip compressed data, has original file name: "HWPA.htm", from NTFS filesystem (NT), last modified: 2006-03-29 07:02:27
1505321       0x16F829        gzip compressed data, has original file name: "InLog.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
1506151       0x16FB67        gzip compressed data, has original file name: "language.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:12
1705020       0x1A043C        gzip compressed data, has original file name: "share.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:57
1775289       0x1B16B9        gzip compressed data, has original file name: "WanMAC.htm", from NTFS filesystem (NT), last modified: 2006-05-04 10:21:13
1778616       0x1B23B8        gzip compressed data, has original file name: "WClient.htm", from NTFS filesystem (NT), last modified: 2006-03-04 02:21:25
1780397       0x1B2AAD        gzip compressed data, has original file name: "WFilter.htm", from NTFS filesystem (NT), last modified: 2006-03-04 02:21:25
1783934       0x1B387E        gzip compressed data, has original file name: "Wireless.htm", from NTFS filesystem (NT), last modified: 2006-04-04 13:41:57
1791356       0x1B557C        gzip compressed data, has original file name: "wlaninfo.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:03
1791533       0x1B562D        gzip compressed data, has original file name: "WMList.htm", from NTFS filesystem (NT), last modified: 2006-03-17 16:39:09
1793873       0x1B5F51        gzip compressed data, has original file name: "WRT54G_qos.htm", from NTFS filesystem (NT), last modified: 2006-04-04 06:44:57
1800246       0x1B7836        gzip compressed data, has original file name: "WSecurity.htm", from NTFS filesystem (NT), last modified: 2006-04-06 10:55:41
1806753       0x1B91A1        gzip compressed data, has original file name: "WState.htm", from NTFS filesystem (NT), last modified: 2006-03-30 09:05:03
1807360       0x1B9400        TROC filesystem, 184549376 file entries
1807637       0x1B9515        gzip compressed data, has original file name: "capadmin.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:53
1808899       0x1B9A03        gzip compressed data, has original file name: "capapp.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:53
1810111       0x1B9EBF        gzip compressed data, has original file name: "capasg.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:59
1818751       0x1BC07F        gzip compressed data, has original file name: "capsec.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:53
1820636       0x1BC7DC        gzip compressed data, has original file name: "capsetup.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:54
1822263       0x1BCE37        gzip compressed data, has original file name: "capstatus.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:54
1822766       0x1BD02E        gzip compressed data, has original file name: "ddnsmsg.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:54
1823333       0x1BD265        gzip compressed data, has original file name: "errmsg.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:55
1824046       0x1BD52E        gzip compressed data, has original file name: "help.js", from NTFS filesystem (NT), last modified: 2006-05-15 08:59:56
```

It's seems we have succesvol dumped the firmware.
A quick look at the output tells us we have a VxWorks Operating system, and a TROC filesystem.

Both i have never heard of before.
But we can also see a lot of htm files.

Shall we try to extract some files?

I have seen some interesting filenames in the output of binwalker.
Lastpassword.htm and unauthorized.htm

Lets extract those files from the firmware dump.


## Extracting files from the firmware dump

To extract the 2 files, we can use the utility dd. 

dd \[inputfile\] \[outputfile\] \[skip\] \[count\] \[blocksize\]

inputfile = MX25L1605A_SOIC16_20200124_185449.bin

outputfile = lastpassword.htm.gz (becouse the source is also compressed)

skip = 396320 (the offset of the file in the firmware dump, use the output of binwalker as reference)

count = 196 (calculate from the next file's offset from the output of binwalker. subtract both values.)

blocksize = 1 (this is the size of the blocks.) 


> **Note:** We can also use count=1 and bs=196, this tells dd that we count 1 blocksize of 196 bytes.

```
$ dd if=MX25L1605A_SOIC16_20200124_185449.BIN of=lastpassword.htm.gz skip=396320 count=196 bs=1

$ dd if=MX25L1605A_SOIC16_20200124_185449.BIN of=Unauthorized.htm.gz skip=707313 count=144 bs=1
```

Listing of the files collected so far.

```
$ ls -la

drwxrwxr-x  5 w w    4096 feb  4 20:43 .
drwxrwxr-x 13 w w    4096 jan 25 19:39 ..
-rw-rw-r--  1 w w   14982 jan 24 20:33 binwalk_output.log
-rw-r--r--  1 w w    4466 dec 27 12:52 bootlog.log
drwxrwxr-x  2 w w    4096 feb  4 20:49 modified_firmware
-rw-rw-r--  1 w w     196 feb  4 20:29 lastpassword.htm.gz
-rwxrwxrwx  1 w w  989685 jan 24 18:48 MX25L1605A.pdf
-rwxrwxrwx  1 w w 2097152 jan 24 18:55 MX25L1605A_SOIC16_20200124_185449.BIN
-rwxrwxrwx  1 w w 2097152 jan 24 18:55 MX25L1605A_SOIC16_20200124_185531.BIN
-rw-rw-r--  1 w w     144 feb  4 20:42 Unauthorized.htm.gz
```

Lets see the content of the file lastpassword.htm.gz

```
$ zcat lastpassword.htm.gz

<HTML><HEAD>
<META http-equiv=Content-Type content="text/html; charset=iso-8859-1">
</HEAD>
<BODY><PRE>Last Password : <TRI_START_LASTPSW>[TRI_LAST_PASSWORD]<TRI_END_LASTPSW>
</PRE></BODY></HTML>
```

## Modifing the firmware


```
$ cp Unauthorized.htm.gz Unauthorized.htm_org.gz
$ mkdir modified_firmware
$ mv Unauthorized.htm* modified_firmware/
$ mv lastpassword.htm* modified_firmware/
$ cp MX25L1605A_SOIC16_20200124_185449.BIN modified_firmware/
```

```
$ cd modified_firmware/
```
```
$ ls -la

drwxrwxr-x 2 w w    4096 feb  4 20:49 .
drwxrwxr-x 5 w w    4096 feb  4 20:43 ..
-rw-rw-r-- 1 w w  707313 feb  4 20:48 block1
-rw-rw-r-- 1 w w 1389695 feb  4 20:48 block2
-rw-rw-r-- 1 w w     196 feb  4 20:29 lastpassword.htm.gz
-rwxrwxr-x 1 w w 2097152 feb  4 20:44 MX25L1605A_SOIC16_20200124_185449.BIN
-rw-rw-r-- 1 w w 2097152 feb  4 20:49 MX25L1605A_SOIC16_20200124_185449.BIN_modified_firmware
-rw-rw-r-- 1 w w     144 feb  4 20:40 Unauthorized.htm.gz
-rw-rw-r-- 1 w w     144 feb  4 20:40 Unauthorized.htm_org.gz
```

```
$ zcat Unauthorized.htm_org.gz 

<HTML><HEAD><TITLE>401 Unauthorized</TITLE></HEAD>
<BODY BGCOLOR="#cc9999"><H4>401 Unauthorized</H4>
Authorization required.
</BODY></HTML>
```

Now make changes in the file with the name Unauthorized.htm.
> **Note:** Becouse we have extracted the files from the firmware with dd and we are writing the file back into the firmware with dd, the file size of the file must be exact the same. so play around with some characters te make sure the bytes are the same.

```
$ zcat Unauthorized.htm.gz 

<HTML><BODY BGCOLOR="#cc9999"><H4>401 Unauthorized</H4><TRI_START_LASTPSW>[TRI_LAST_PASSWORD]
<TRI_END_LASTPSW></BODY></HTML>
```

```
-rw-rw-r-- 1 w w     144 feb  4 20:42 Unauthorized.htm.gz
-rw-rw-r-- 1 w w     144 feb  4 20:40 Unauthorized.htm_org.gz
```

## Rebuilding the firmware

Now we know how we can get the administrator password from the device, we can begin te reconstruct the firmware.
I dont know how the VXWorks OS works in detail, so i want to make sure that the filesize of the modified file is the same size of the original.
  
```
$ dd if=MX25L1605A_SOIC16_20200124_185449.BIN bs=1 count=707313 of=block1
$ dd if=MX25L1605A_SOIC16_20200124_185449.BIN bs=1 skip=707457 of=block2
$ cat block1 Unauthorized.htm.gz block2 > MX25L1605A_SOIC16_20200124_185449.BIN_modified_firmware 
```

## Flashing the firmware

![alt text][rt809h]

[rt809h]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/rt809h.jpg "rt809h"


## Testing the modified firmware

![alt text][logon_page]

Hit the cancel button.

![alt text][unauthorized]

[logon_page]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/login_page.png "Logon page"
[unauthorized]: https://github.com/w2k8/linksys_wrt54g_v7/raw/master/images/unauthorized_croped.jpg "Unauthorized"

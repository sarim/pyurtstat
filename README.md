Usage:

./pyurtstat.py SERVER PORT [options]

SERVER:		Required, ip or hostname of urbanterror server.
PORT:		Required, port of urbanterror server.
options:	Optional, comma separated list of server options you want to retrive, by default, pyurtstat will show sv_hostname and mapname


Example:

```$ ./pyurtstat.py 209.190.50.170 27960

sv_hostname:		^2WWW.FALLIN-ANGELS.ORG
mapname:		ut4_roma_beta2B

Online Players : 7

Ping			Kill			Name
----------------------  ----------------------  ----------------------
146			32			COS
123			40			|FA|Sh4doWs
132			3			NoobBert
130			32			NiAkE2002
104			36			Badvegan
145			22			KnelII
158			36			pITYU```


```$ ./pyurtstat.py 209.190.50.170 27960 Admin

Admin:		DragonHeart

Online Players : 7

Ping			Kill			Name
----------------------  ----------------------  ----------------------
145			32			COS
110			40			|FA|Sh4doWs
140			4			NoobBert
126			32			NiAkE2002
103			37			Badvegan
150			22			KnelII
155			36			pITYU```

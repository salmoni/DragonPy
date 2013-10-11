10 PRINT:PRINT "TEST CC SUBA V0.1"
20 PRINT "(GPL V3 OR ABOVE)"
30 PRINT:PRINT "COPYLEFT (C) 2013 JENS DIEMER":PRINT
40 LA=&H4000			' LOAD / EXECUTE ADDRESS
50 PRINT "POKE MACHINE CODE TO: $";HEX$(LA)
60 PA = LA			' START ADDRESS FOR POKE
70 READ HB$			' HEX CONSTANTS
80 IF HB$="END" THEN 140
90 V=VAL("&H"+HB$)
100 POKE PA,V	                ' POKE VALUE INTO MEMORY
110 'PRINT "POKE $";HEX$(V);" AT $";HEX$(PA)
120 PA = PA + 1			        ' INCREMENT POKE ADDRESS
130 GOTO 70
140 PRINT "LOADED, END ADDRESS IS: $"; HEX$(PA-1)
150 INIT=3:PRINT
160 PRINT "INIT ACCU A WITH";INIT
170 POKE &H4500,INIT ' SET START VALUE
180 PRINT "START MACHINE CODE PROGRAMM"
190 EXEC LA
200 PRINT "RESULTS:"
210 EA=&H4500
220 FOR I = 1 TO 8
230 PRINT I;INIT;"A:";PEEK(EA);" CC:";HEX$(PEEK(EA+1))
235 INIT=INIT-1
240 EA=EA+2
250 NEXT I
270 ' MACHINE CODE IN HEX
280 ' LDA $4500
290 DATA B6,45,00
300 ' SUBA 1
310 DATA 80,01
320 ' TFR CC,B + STD $4502
330 DATA 1F,A9,FD,45,02
340 ' LDA $4500
350 DATA B6,45,00
360 ' SUBA 2
370 DATA 80,02
380 ' TFR CC,B + STD $4504
390 DATA 1F,A9,FD,45,04
400 ' LDA $4500
410 DATA B6,45,00
420 ' SUBA 3
430 DATA 80,03
440 ' TFR CC,B + STD $4506
450 DATA 1F,A9,FD,45,06
460 ' LDA $4500
470 DATA B6,45,00
480 ' SUBA 4
490 DATA 80,04
500 ' TFR CC,B + STD $4508
510 DATA 1F,A9,FD,45,08
520 ' LDA $4500
530 DATA B6,45,00
540 ' SUBA 5
550 DATA 80,05
560 ' TFR CC,B + STD $450A
570 DATA 1F,A9,FD,45,0A
580 ' LDA $4500
590 DATA B6,45,00
600 ' SUBA 6
610 DATA 80,06
620 ' TFR CC,B + STD $450C
630 DATA 1F,A9,FD,45,0C
640 ' LDA $4500
650 DATA B6,45,00
660 ' SUBA 7
670 DATA 80,07
680 ' TFR CC,B + STD $450E
690 DATA 1F,A9,FD,45,0E
700 ' LDA $4500
710 DATA B6,45,00
720 ' SUBA 8
730 DATA 80,08
740 ' TFR CC,B + STD $4510
750 DATA 1F,A9,FD,45,10
760 ' RTS
770 DATA 39
780 DATA END

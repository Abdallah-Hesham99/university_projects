; -------------------------------------------------------------
; 
$INCLUDE "Common\8052.mc"

; -------------------------------------------------------------
; Program start
; -------------------------------------------------------------

    ORG 00h
;-------Define Inputs and outputs------
MOV P2,#00h
MOV P3,#0FFh
MOV P1,#0FFh
;-------Monitor Buttons-------
buttons:

JNB P1.0, do1
JNB P1.1, re1
JNB P1.2, me1
JNB P1.3, fa1
JNB P1.4, sol1
JNB P1.5, la1
JNB P1.6, si1
JNB P1.7, g1

JNB P3.0, c1
JNB P3.1, c2
JNB P3.2, b1
JNB P3.3, b2
JNB P3.4, b3
JNB P3.5, b4
JNB P3.6, b5
SJMP buttons

g1:
LJMP do2

c1:
LJMP  re2
c2:
LJMP  me2



b1:
LJMP  fa2
b2:
LJMP  sol2
b3:
LJMP  la2
b4:
LJMP  si2
b5:
LJMP  do3





    
; ------do1------ 
do1:
CPL p2.7
MOV R3,#20
h1: MOV R4,#255
h2: 
DJNZ R4,h2
DJNZ R3,h1

;JNB P1.0, do1
RET
; ------re1------ 
re1:
CPL p2.7
MOV R3,#16
h3: MOV R4,#255
h4: 
DJNZ R4,h4
DJNZ R3,h3
;JNB P1.0, re1
RET
; ------me1------ 
me1:
CPL p2.7
MOV R3,#12
h5: MOV R4,#255
h6: 
DJNZ R4,h6
DJNZ R3,h5
;JNB P1.0, me1
RET
; ------fa1------ 
fa1:
CPL p2.7
MOV R3,#8
h7: MOV R4,#245
h8: 
DJNZ R4,h8
DJNZ R3,h7
;JNB P1.0, fa1
RET
; ------sol1------ 
sol1:
CPL p2.7
MOV R3,#4
h9: MOV R4,#220
h10: 
DJNZ R4,h10
DJNZ R3,h9
;JNB P1.0, sol1
RET
; ------la1------ 
la1:
CPL p2.7
MOV R3,#14
h11: MOV R4,#150
h12: 
DJNZ R4,h12
DJNZ R3,h11
;JNB P1.0, la1
RET
; ------si1------ 
si1:
CPL p2.7
MOV R3,#10
h13: MOV R4,#150
h14: 
DJNZ R4,h14
DJNZ R3,h13
;JNB P1.0, si1
RET


; ------do2------ 
do2:
CPL p2.7
MOV R3,#10
h15: MOV R4,#140
h16: 
DJNZ R4,h16
DJNZ R3,h15
;JNB P1.0, do2
RET

; ------re2------ 
re2:
CPL p2.7
MOV R3,#6
h17: MOV R4,#150
h18: 
DJNZ R4,h18
DJNZ R3,h17
;JNB P1.0, re2
RET

; ------me2------ 
me2:
CPL p2.7
MOV R3,#2
h19: MOV R4,#150
h20: 
DJNZ R4,h20
DJNZ R3,h19
;JNB P1.0, me2
RET

; ------fa2------ 
fa2:
CPL p2.7
MOV R3,#10
h21: MOV R4,#50
h22: 
DJNZ R4,h22
DJNZ R3,h21
;JNB P1.0, fa2
RET

; ------sol2------ 
sol2:
CPL p2.7
MOV R3,#6
h23: MOV R4,#50
h24: 
DJNZ R4,h24
DJNZ R3,h23
;JNB P1.0, sol2
RET

; ------la2------ 
la2:
CPL p2.7
MOV R3,#4
h25: MOV R4,#40
h26: 
DJNZ R4,h26
DJNZ R3,h25
;JNB P1.0, la2
RET

; ------si2------ 
si2:
CPL p2.7
MOV R3,#2
h27: MOV R4,#50
h28: 
DJNZ R4,h28
DJNZ R3,h27
;JNB P1.0, si2
RET

; ------do3------ 
do3:
CPL p2.7
MOV R3,#2
h29: MOV R4,#60
h30: 
DJNZ R4,h30
DJNZ R3,h29
;JNB P1.0, do3
RET
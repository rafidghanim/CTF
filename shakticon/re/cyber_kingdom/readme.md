> cyber_k main.c
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+Ch] [rbp-164h]
  int j; // [rsp+10h] [rbp-160h]
  int v6; // [rsp+14h] [rbp-15Ch]
  int k; // [rsp+18h] [rbp-158h]
  int v8[36]; // [rsp+20h] [rbp-150h]
  int v9[36]; // [rsp+B0h] [rbp-C0h]
  char s[40]; // [rsp+140h] [rbp-30h] BYREF
  unsigned __int64 v11; // [rsp+168h] [rbp-8h]

  v11 = __readfsqword(0x28u);
  srand(0x7Bu);
  for ( i = 0; i <= 34; ++i )
    v8[i] = rand() & 0xF;
  puts("\n\t||| Welcome to my Cyber Kingdom |||");
  puts("||| I have a quick task for you if you don't mind |||");
  puts("|| Find the correct flag for me and prove yourself! ||\n");
  printf("Please enter the flag: ");
  fgets(s, 36, _bss_start);
  for ( j = 0; j <= 34; ++j )
    s[j] ^= LOBYTE(v8[j]);
  v9[0] = 114;
  v9[1] = 109;
  v9[2] = 96;
  v9[3] = 101;
  v9[4] = 115;
  v9[5] = 98;
  v9[6] = 104;
  v9[7] = 122;
  v9[8] = 108;
  v9[9] = 122;
  v9[10] = 119;
  v9[11] = 100;
  v9[12] = 49;
  v9[13] = 84;
  v9[14] = 119;
  v9[15] = 49;
  v9[16] = 108;
  v9[17] = 99;
  v9[18] = 89;
  v9[19] = 103;
  v9[20] = 98;
  v9[21] = 49;
  v9[22] = 108;
  v9[23] = 88;
  v9[24] = 49;
  v9[25] = 125;
  v9[26] = 83;
  v9[27] = 126;
  v9[28] = 59;
  v9[29] = 98;
  v9[30] = 105;
  v9[31] = 48;
  v9[32] = 108;
  v9[33] = 49;
  v9[34] = 114;
  v6 = 0;
  for ( k = 0; k <= 34; ++k )
  {
    if ( v9[k] == s[k] )
      ++v6;
  }
  if ( v6 == 35 )
    puts("\nYou got it!!");
  else
    puts("\nNope, that's not the right path");
  return 0;
}
```
based on code i notice that:
* there is a scheme before the user input comparing with v6
* the user input xored with srand() value
* the length of flag is 35
so, to retrieve the flag value:
gdb -> set break point into cmp -> input 0*35 -> xor the output with v9 -> flag
> leet@lzi~# gdb cyber_k
```
GNU gdb (Debian 13.2-1) 13.2
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from cyber_k...
(No debugging symbols found in cyber_k)
gdb-peda$ r
Starting program:cyber_k 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

        ||| Welcome to my Cyber Kingdom |||
||| I have a quick task for you if you don't mind |||
|| Find the correct flag for me and prove yourself! ||

Please enter the flag: 00000000000000000000000000000000000 

Nope, that's not the right path
[Inferior 1 (process 96768) exited normally]
Warning: 'set logging off', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled off'.

Warning: 'set logging on', an alias for the command 'set logging enabled', is deprecated.
Use 'set logging enabled on'.

Warning: not running
gdb-peda$ disas main
Dump of assembler code for function main:
   0x0000555555555189 <+0>:     push   rbp
   0x000055555555518a <+1>:     mov    rbp,rsp
   0x000055555555518d <+4>:     sub    rsp,0x170
   0x0000555555555194 <+11>:    mov    rax,QWORD PTR fs:0x28
   0x000055555555519d <+20>:    mov    QWORD PTR [rbp-0x8],rax
   0x00005555555551a1 <+24>:    xor    eax,eax
   0x00005555555551a3 <+26>:    mov    DWORD PTR [rbp-0x154],0x7b
   0x00005555555551ad <+36>:    mov    eax,DWORD PTR [rbp-0x154]
   0x00005555555551b3 <+42>:    mov    edi,eax
   0x00005555555551b5 <+44>:    call   0x555555555060 <srand@plt>
   0x00005555555551ba <+49>:    mov    DWORD PTR [rbp-0x164],0x0
   0x00005555555551c4 <+59>:    jmp    0x5555555551e6 <main+93>
   0x00005555555551c6 <+61>:    call   0x555555555080 <rand@plt>
   0x00005555555551cb <+66>:    and    eax,0xf
   0x00005555555551ce <+69>:    mov    edx,eax
   0x00005555555551d0 <+71>:    mov    eax,DWORD PTR [rbp-0x164]
   0x00005555555551d6 <+77>:    cdqe
   0x00005555555551d8 <+79>:    mov    DWORD PTR [rbp+rax*4-0x150],edx
   0x00005555555551df <+86>:    add    DWORD PTR [rbp-0x164],0x1
   0x00005555555551e6 <+93>:    cmp    DWORD PTR [rbp-0x164],0x22
   0x00005555555551ed <+100>:   jle    0x5555555551c6 <main+61>
   0x00005555555551ef <+102>:   lea    rax,[rip+0xe12]        # 0x555555556008
   0x00005555555551f6 <+109>:   mov    rdi,rax
   0x00005555555551f9 <+112>:   call   0x555555555030 <puts@plt>
   0x00005555555551fe <+117>:   lea    rax,[rip+0xe2b]        # 0x555555556030
   0x0000555555555205 <+124>:   mov    rdi,rax
   0x0000555555555208 <+127>:   call   0x555555555030 <puts@plt>
   0x000055555555520d <+132>:   lea    rax,[rip+0xe54]        # 0x555555556068
   0x0000555555555214 <+139>:   mov    rdi,rax
   0x0000555555555217 <+142>:   call   0x555555555030 <puts@plt>
   0x000055555555521c <+147>:   lea    rax,[rip+0xe7d]        # 0x5555555560a0
   0x0000555555555223 <+154>:   mov    rdi,rax
   0x0000555555555226 <+157>:   mov    eax,0x0
   0x000055555555522b <+162>:   call   0x555555555050 <printf@plt>
   0x0000555555555230 <+167>:   mov    rdx,QWORD PTR [rip+0x2e09]        # 0x555555558040 <stdin@GLIBC_2.2.5>
   0x0000555555555237 <+174>:   lea    rax,[rbp-0x30]
   0x000055555555523b <+178>:   mov    esi,0x24
   0x0000555555555240 <+183>:   mov    rdi,rax
   0x0000555555555243 <+186>:   call   0x555555555070 <fgets@plt>
   0x0000555555555248 <+191>:   mov    DWORD PTR [rbp-0x160],0x0
   0x0000555555555252 <+201>:   jmp    0x555555555285 <main+252>
   0x0000555555555254 <+203>:   mov    eax,DWORD PTR [rbp-0x160]
   0x000055555555525a <+209>:   cdqe
   0x000055555555525c <+211>:   movzx  edx,BYTE PTR [rbp+rax*1-0x30]
   0x0000555555555261 <+216>:   mov    eax,DWORD PTR [rbp-0x160]
   0x0000555555555267 <+222>:   cdqe
   0x0000555555555269 <+224>:   mov    eax,DWORD PTR [rbp+rax*4-0x150]
   0x0000555555555270 <+231>:   xor    edx,eax
   0x0000555555555272 <+233>:   mov    eax,DWORD PTR [rbp-0x160]
   0x0000555555555278 <+239>:   cdqe
   0x000055555555527a <+241>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x000055555555527e <+245>:   add    DWORD PTR [rbp-0x160],0x1
   0x0000555555555285 <+252>:   cmp    DWORD PTR [rbp-0x160],0x22
   0x000055555555528c <+259>:   jle    0x555555555254 <main+203>
   0x000055555555528e <+261>:   mov    DWORD PTR [rbp-0xc0],0x72
   0x0000555555555298 <+271>:   mov    DWORD PTR [rbp-0xbc],0x6d
   0x00005555555552a2 <+281>:   mov    DWORD PTR [rbp-0xb8],0x60
   0x00005555555552ac <+291>:   mov    DWORD PTR [rbp-0xb4],0x65
   0x00005555555552b6 <+301>:   mov    DWORD PTR [rbp-0xb0],0x73
   0x00005555555552c0 <+311>:   mov    DWORD PTR [rbp-0xac],0x62
   0x00005555555552ca <+321>:   mov    DWORD PTR [rbp-0xa8],0x68
   0x00005555555552d4 <+331>:   mov    DWORD PTR [rbp-0xa4],0x7a
   0x00005555555552de <+341>:   mov    DWORD PTR [rbp-0xa0],0x6c
   0x00005555555552e8 <+351>:   mov    DWORD PTR [rbp-0x9c],0x7a
   0x00005555555552f2 <+361>:   mov    DWORD PTR [rbp-0x98],0x77
   0x00005555555552fc <+371>:   mov    DWORD PTR [rbp-0x94],0x64
   0x0000555555555306 <+381>:   mov    DWORD PTR [rbp-0x90],0x31
   0x0000555555555310 <+391>:   mov    DWORD PTR [rbp-0x8c],0x54
   0x000055555555531a <+401>:   mov    DWORD PTR [rbp-0x88],0x77
   0x0000555555555324 <+411>:   mov    DWORD PTR [rbp-0x84],0x31
   0x000055555555532e <+421>:   mov    DWORD PTR [rbp-0x80],0x6c
   0x0000555555555335 <+428>:   mov    DWORD PTR [rbp-0x7c],0x63
   0x000055555555533c <+435>:   mov    DWORD PTR [rbp-0x78],0x59
   0x0000555555555343 <+442>:   mov    DWORD PTR [rbp-0x74],0x67
   0x000055555555534a <+449>:   mov    DWORD PTR [rbp-0x70],0x62
   0x0000555555555351 <+456>:   mov    DWORD PTR [rbp-0x6c],0x31
   0x0000555555555358 <+463>:   mov    DWORD PTR [rbp-0x68],0x6c
   0x000055555555535f <+470>:   mov    DWORD PTR [rbp-0x64],0x58
   0x0000555555555366 <+477>:   mov    DWORD PTR [rbp-0x60],0x31
   0x000055555555536d <+484>:   mov    DWORD PTR [rbp-0x5c],0x7d
   0x0000555555555374 <+491>:   mov    DWORD PTR [rbp-0x58],0x53
   0x000055555555537b <+498>:   mov    DWORD PTR [rbp-0x54],0x7e
   0x0000555555555382 <+505>:   mov    DWORD PTR [rbp-0x50],0x3b
   0x0000555555555389 <+512>:   mov    DWORD PTR [rbp-0x4c],0x62
   0x0000555555555390 <+519>:   mov    DWORD PTR [rbp-0x48],0x69
   0x0000555555555397 <+526>:   mov    DWORD PTR [rbp-0x44],0x30
   0x000055555555539e <+533>:   mov    DWORD PTR [rbp-0x40],0x6c
   0x00005555555553a5 <+540>:   mov    DWORD PTR [rbp-0x3c],0x31
   0x00005555555553ac <+547>:   mov    DWORD PTR [rbp-0x38],0x72
   0x00005555555553b3 <+554>:   mov    DWORD PTR [rbp-0x15c],0x0
   0x00005555555553bd <+564>:   mov    DWORD PTR [rbp-0x158],0x0
   0x00005555555553c7 <+574>:   jmp    0x5555555553fa <main+625>
   0x00005555555553c9 <+576>:   mov    eax,DWORD PTR [rbp-0x158]
   0x00005555555553cf <+582>:   cdqe
   0x00005555555553d1 <+584>:   mov    edx,DWORD PTR [rbp+rax*4-0xc0]
   0x00005555555553d8 <+591>:   mov    eax,DWORD PTR [rbp-0x158]
   0x00005555555553de <+597>:   cdqe
   0x00005555555553e0 <+599>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00005555555553e5 <+604>:   movsx  eax,al
   0x00005555555553e8 <+607>:   cmp    edx,eax
   0x00005555555553ea <+609>:   jne    0x5555555553f3 <main+618>
   0x00005555555553ec <+611>:   add    DWORD PTR [rbp-0x15c],0x1
   0x00005555555553f3 <+618>:   add    DWORD PTR [rbp-0x158],0x1
   0x00005555555553fa <+625>:   cmp    DWORD PTR [rbp-0x158],0x22
   0x0000555555555401 <+632>:   jle    0x5555555553c9 <main+576>
   0x0000555555555403 <+634>:   cmp    DWORD PTR [rbp-0x15c],0x23
   0x000055555555540a <+641>:   jne    0x55555555541d <main+660>
   0x000055555555540c <+643>:   lea    rax,[rip+0xca5]        # 0x5555555560b8
   0x0000555555555413 <+650>:   mov    rdi,rax
   0x0000555555555416 <+653>:   call   0x555555555030 <puts@plt>
   0x000055555555541b <+658>:   jmp    0x55555555542c <main+675>
   0x000055555555541d <+660>:   lea    rax,[rip+0xca4]        # 0x5555555560c8
   0x0000555555555424 <+667>:   mov    rdi,rax
   0x0000555555555427 <+670>:   call   0x555555555030 <puts@plt>
   0x000055555555542c <+675>:   mov    eax,0x0
   0x0000555555555431 <+680>:   mov    rdx,QWORD PTR [rbp-0x8]
   0x0000555555555435 <+684>:   sub    rdx,QWORD PTR fs:0x28
   0x000055555555543e <+693>:   je     0x555555555445 <main+700>
   0x0000555555555440 <+695>:   call   0x555555555040 <__stack_chk_fail@plt>
   0x0000555555555445 <+700>:   leave
   0x0000555555555446 <+701>:   ret
End of assembler dump.
gdb-peda$ b*0x00005555555553e8
Breakpoint 1 at 0x5555555553e8
gdb-peda$ r
Starting program:cyber_k 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

        ||| Welcome to my Cyber Kingdom |||
||| I have a quick task for you if you don't mind |||
|| Find the correct flag for me and prove yourself! ||

Please enter the flag: 00000000000000000000000000000000000
[----------------------------------registers-----------------------------------]
RAX: 0x31 ('1')
RBX: 0x7fffffffdd68 --> 0x7fffffffe0da ("/home/kecoakterbang/CTF/shakticon/cyber_kingdom/cyber_k")
RCX: 0x7fffffffdc20 ("151>7;;>:10<1;455761>5;70><<?<=01>?")
RDX: 0x72 ('r')
RSI: 0x5555555596b1 ('0' <repeats 34 times>, "\n")
RDI: 0x7ffff7f8da40 --> 0x0 
RBP: 0x7fffffffdc50 --> 0x1 
RSP: 0x7fffffffdae0 --> 0x0 
RIP: 0x5555555553e8 (<main+607>:        cmp    edx,eax)
R8 : 0x0 
R9 : 0x410 
R10: 0x1000 
R11: 0x246 
R12: 0x0 
R13: 0x7fffffffdd78 --> 0x7fffffffe112 ("CLUTTER_IM_MODULE=ibus")
R14: 0x555555557dd8 --> 0x555555555130 (endbr64)
R15: 0x7ffff7ffd000 --> 0x7ffff7ffe2d0 --> 0x555555554000 --> 0x10102464c457f
EFLAGS: 0x297 (CARRY PARITY ADJUST zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5555555553de <main+597>:   cdqe
   0x5555555553e0 <main+599>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x5555555553e5 <main+604>:   movsx  eax,al
=> 0x5555555553e8 <main+607>:   cmp    edx,eax
   0x5555555553ea <main+609>:   jne    0x5555555553f3 <main+618>
   0x5555555553ec <main+611>:   add    DWORD PTR [rbp-0x15c],0x1
   0x5555555553f3 <main+618>:   add    DWORD PTR [rbp-0x158],0x1
   0x5555555553fa <main+625>:   cmp    DWORD PTR [rbp-0x158],0x22
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdae0 --> 0x0 
0008| 0x7fffffffdae8 --> 0x2300000000 ('')
0016| 0x7fffffffdaf0 --> 0x23 ('#')
0024| 0x7fffffffdaf8 --> 0x7b00000000 ('')
0032| 0x7fffffffdb00 --> 0x500000001 
0040| 0x7fffffffdb08 --> 0xe00000001 
0048| 0x7fffffffdb10 --> 0xb00000007 
0056| 0x7fffffffdb18 --> 0xe0000000b 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x00005555555553e8 in main ()
gdb-peda$ 

```
we get RCX: 0x7fffffffdc20 ("151>7;;>:10<1;455761>5;70><<?<=01>?")
since we know that the mechanism of the binary is using xor to compare with real value
then, just guest the uknown int symbol like >;<?=
we know that the flag is started with shaktictf{
xor(1,114) = s
xor(5,109) = h
and soon untii the last xor = }

after long comparing each other i get
#before_s = "151>7;;>:10<1;455761>5;70><<?<=01>?"
s =[1, 5, 1, 14, 7, 11, 11, 14, 10, 1, 0, 12, 1, 11, 4, 5, 5, 7, 6, 1, 14, 5, 11, 7, 0, 14, 12, 12, 15, 12, 13, 0, 1, 14, 15]

then xor them with v9 array
```
from pwn import xor
#before_s = "151>7;;>:10<1;455761>5;70><<?<=01>?"
s =[1, 5, 1, 14, 7, 11, 11, 14, 10, 1, 0, 12, 1, 11, 4, 5, 5, 7, 6, 1, 14, 5, 11, 7, 0, 14, 12, 12, 15, 12, 13, 0, 1, 14, 15]
v9 = [114, 109, 96, 101, 115, 98, 104, 122, 108, 122, 119, 100, 49, 84, 119, 49, 108, 99, 89, 103, 98, 49, 108, 88, 49, 125, 83, 126, 59, 98, 105, 48, 108, 49, 114]
print(''.join([xor(s[i],v9[i]).decode() for i in range(len(s))]))
#shaktictf{wh0_s4id_fl4g_1s_r4nd0m?}
```

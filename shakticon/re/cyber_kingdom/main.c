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

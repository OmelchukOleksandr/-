Const m=[',',' ','.','?','!'];
Var s,s1,smin:string;
    i,min:byte;
Begin
    write('Введіть речення: ');readln(s);
    s:=s+' ';s1:='';
    For i:=1 to Length(s) do
     if s[i] in m then break;
    smin:=Copy(s, 1, i-1);min:=Length(smin);
    For i:=1 to Length(s) do
     if not (s[i] in m) then s1:=s1+s[i]
     else
     Begin
       if (s1<>'')and(Length(s1)<min) then
       Begin
         min:=Length(s1);
         smin:=s1;
       End;
       s1:='';
     End;
    writeln('Найкоротше слово "',smin,'"');
End.
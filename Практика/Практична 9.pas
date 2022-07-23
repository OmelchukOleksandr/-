type rs = record
     name, t1, t2, t3:string;
     c: real;
     end;
var i, n: integer;
    a:array[1..100] of rs;
const line = '--------------------------------------------------------------------------------------';
begin
  write('Введіть к-сть рейсів: '); readln(n);
  for i:= 1 to n do
    begin
      write('Пункт посадки: '); readln(a[i].name);
      write('Час відправлення: '); readln(a[i].t1);
      write('Час прибуття: '); readln(a[i].t2);
      write('Час польоту: '); readln(a[i].t3);
      write('Вартість квитка: '); readln(a[i].c);         
    end;
  writeln(line);
  writeln('Пункт посадки|Час відправлення|Час прибуття|Час польоту|Вартість квитка');
  writeln(line);
  for i:= 1 to n do
    writeln(a[i].name:13,'|', a[i].t1:16, '|', a[i].t2:12, '|', a[i].t3:11, '|', a[i].c);  
end.
    
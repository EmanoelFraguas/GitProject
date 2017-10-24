program teste;

var
cont: integer;
n, num: longint;

begin
	read(n);
	num := n;
	cont := 0;
	while num > 0 do
	begin
		num := num div 10;
		cont := cont +1;
	end;
	writeln(cont);
end.
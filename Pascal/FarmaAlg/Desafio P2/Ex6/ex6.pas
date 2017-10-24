program ex6;

var
v1: array[1..10] of integer;
v2: array[1..10] of integer;
i, n, dif, cont: integer;

procedure leitura();
begin
	for i := 1 to 10 do
	begin
		read(n);
		v1[i] := n;
	end;
	for i := 1 to 10 do
	begin
		read(n);
		v2[i] := n;
	end;
	read(dif);
end;

begin
	leitura();
	cont := 0;
	for i := 1 to 10 do
		if abs(v1[i] - v2[i]) > dif then
			cont := cont +1;
	if cont = 0 then 
		writeln('PARECIDOS')
	else
		writeln('DIFERENTES com ', cont, ' discrepante(s)');
end.
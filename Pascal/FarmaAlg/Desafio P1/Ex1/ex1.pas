program ex1;
uses Math;

var
cont, i: integer;
v1: array[1..100] of integer;
expo, numero, maior: real;
num, n, mult, result1, result2: longint;
bin: boolean;

procedure contador(n: longint);

begin
	num := n;
	cont := 0;
	while num > 0 do
	begin
		num := num div 10;
		cont := cont +1;
	end;
end;

procedure insertArray(n: longint);

begin
	mult := 1;
	for i := cont downto 1 do
	begin
		result1 := n mod (mult * 10);
		result2 := result1 div mult;
		mult := mult * 10;
		v1[i] := result2;
	end;
end;

procedure printArray();

begin
	write('Array: ');
	for i := 1 to cont do
		write(v1[i], ' ');
	writeln('');
end;

begin
	read(n);
	maior := 0;
	while n <> -1 do
	begin
		contador(n);
		insertArray(n);
		//printArray();
		bin := true;
		for i := 1 to cont do
		begin
			if (v1[i] <> 0) and (v1[i] <> 1) then
			begin
				bin := false;
				break;
			end;
		end;
		if bin = false then
			writeln('Número não binário')
		else
		begin
			expo := power(2, cont-1);
			numero := 0;
			for i := 1 to cont do
			begin
				if v1[i] = 1 then
				begin
					numero := numero + expo;
				end;
				expo := expo / 2;
			end;
			writeln(numero:0:0);
		end;
		if numero > maior then
			maior := numero;
		readln(n);
	end;
	writeln('O maior número binário foi ',maior:0:0)
end.